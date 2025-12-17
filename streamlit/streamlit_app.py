# streamlit_app.py
import json
from pathlib import Path

import requests
import pandas as pd
import streamlit as st

# geospatial
import geopandas as gpd
from shapely.geometry import shape
import pydeck as pdk
import math

st.set_page_config(layout="wide")
st.title("Streamlit — visualize boxes from Django API")

st.divider()
api_link = st.selectbox('select region you want to visualize', ('poland',"opole", "dolnoslaskie"))
if api_link == 'poland':
    value ="http://127.0.0.1:8000/api/box/"
else:
    value = f"http://127.0.0.1:8000/api/box/?region_name={api_link}"


API_URL = st.text_input("Django API URL", value=value)


if not API_URL:
    st.stop()

resp = requests.get(API_URL)
if resp.status_code != 200:
    st.error(f"Failed to fetch data from {API_URL} (status {resp.status_code})")
    st.stop()

data = resp.json()

# --- Normalize different JSON shapes returned by API ---
def normalize_to_records(api_json):
    if isinstance(api_json, dict):
        if "results" in api_json:
            api_json = api_json["results"]
        else:
            api_json = [api_json]

    records = []
    for item in api_json:
        if isinstance(item, dict) and "fields" in item:
            rec = item["fields"].copy()
            if "pk" in item:
                rec["_pk"] = item["pk"]
            elif "id" in item:
                rec["_pk"] = item["id"]
        else:
            rec = item.copy()
        records.append(rec)
    return records

records = normalize_to_records(data)
if not records:
    st.error("No records returned by API.")
    st.stop()

df = pd.DataFrame(records)
st.sidebar.subheader("Data preview & options")
st.sidebar.write(f"Records loaded: {len(df)}")

# detect geometry column
geom_col = None
for c in df.columns:
    if c.lower() == "geometry" or c.lower() == "geom" or c.lower().endswith("geometry"):
        geom_col = c
        break

# --- Parse geometry into shapely geometries ---
def parse_geometry_field(val):
    if val is None:
        return None
    if isinstance(val, (dict, list)):
        try:
            return shape(val)
        except Exception:
            return None
    if isinstance(val, str):
        try:
            parsed = json.loads(val)
            return shape(parsed)
        except Exception:
            try:
                from shapely import wkt
                return wkt.loads(val)
            except Exception:
                return None
    return None

# build GeoDataFrame
if geom_col:
    st.info(f"Parsing geometry column: {geom_col}")
    geoms = df[geom_col].apply(parse_geometry_field)
    gdf = gpd.GeoDataFrame(df.drop(columns=[geom_col]), geometry=geoms)
else:
    possible = [c for c in df.columns if "geo" in c.lower() or "geom" in c.lower()]
    found = None
    for c in possible:
        sample = df[c].iloc[0]
        if isinstance(sample, (str, dict)) and ("type" in str(sample) or (isinstance(sample, str) and sample.strip().startswith("{"))):
            found = c
            break
    if found:
        st.info(f"Using detected geometry-like column: {found}")
        geoms = df[found].apply(parse_geometry_field)
        gdf = gpd.GeoDataFrame(df.drop(columns=[found]), geometry=geoms)
    else:
        st.warning("No geometry column detected. Showing attribute table only.")
        gdf = None

# --- CRS handling ---
if gdf is not None:
    st.sidebar.subheader("CRS / reprojection")
    src_crs = st.sidebar.text_input("Source CRS (EPSG or proj string)", value="EPSG:2180")
    reproject_to_4326 = st.sidebar.checkbox("Reproject to EPSG:4326 for mapping", value=True)

    try:
        if gdf.crs is None and src_crs:
            gdf.set_crs(src_crs, inplace=True, allow_override=True)
            st.sidebar.success(f"Set source CRS to {src_crs}")
    except Exception as e:
        st.sidebar.error(f"Error setting CRS: {e}")

    if reproject_to_4326:
        try:
            gdf = gdf.to_crs(epsg=4326)
            st.sidebar.success("Reprojected to EPSG:4326")
        except Exception as e:
            st.sidebar.error(f"Reprojection failed: {e}")

    # drop invalid/empty geometries
    gdf_valid = gdf[~(gdf.geometry.is_empty | gdf.geometry.isna())].copy()
    if gdf_valid.empty:
        st.error("No valid geometries to display on the map.")
    else:
        # let user select column to color by
        st.sidebar.subheader("Styling")
        available_cols = [c for c in gdf_valid.columns if c != "geometry"]
        if not available_cols:
            st.warning("No attribute columns available for styling.")
            color_by = None
        else:
            color_by = st.sidebar.selectbox("Color by column (choose one)", options=["(none)"] + available_cols, index=0)

        alpha = st.sidebar.slider("Alpha (0-255)", min_value=40, max_value=255, value=100)

        # helper color functions
        def _interp(a, b, t):
            return int(round(a + (b - a) * t))

        def color_map_numeric(val, vmin, vmax, low_rgb=(0, 0, 255), high_rgb=(255, 0, 0), alpha=100):
            # handle edge cases
            try:
                if val is None or (isinstance(val, float) and (math.isnan(val))):
                    return [200, 200, 200, alpha]  # gray for missing
                if vmin == vmax:
                    t = 0.5
                else:
                    t = (float(val) - float(vmin)) / float(vmax - vmin)
                    t = max(0.0, min(1.0, t))
                r = _interp(low_rgb[0], high_rgb[0], t)
                g = _interp(low_rgb[1], high_rgb[1], t)
                b = _interp(low_rgb[2], high_rgb[2], t)
                return [r, g, b, int(alpha)]
            except Exception:
                return [200, 200, 200, alpha]

        def color_map_categorical(val, alpha=100):
            # deterministic hash -> color
            if val is None:
                return [200, 200, 200, alpha]
            s = str(val)
            h = abs(hash(s))
            # create distinct-ish colors by extracting bytes
            r = (h & 0xFF0000) >> 16
            g = (h & 0x00FF00) >> 8
            b = h & 0x0000FF
            # ensure not too dark/light
            def _adj(x):
                return int(60 + (x % 140))  # 60..199
            return [_adj(r), _adj(g), _adj(b), int(alpha)]

        # prepare geojson and inject color property into each feature
        gdf_valid = gdf_valid.reset_index(drop=True)
        geojson = json.loads(gdf_valid.to_json())

        # if user selected a column, compute colors
        if color_by and color_by != "(none)":
            col_series = gdf_valid[color_by]
            is_numeric = pd.api.types.is_numeric_dtype(col_series)

            if is_numeric:
                vmin = float(col_series.min(skipna=True))
                vmax = float(col_series.max(skipna=True))
                st.sidebar.write(f"Numeric column detected. min={vmin:.4g}, max={vmax:.4g}")
            else:
                categories = col_series.astype(str).fillna("None").unique().tolist()
                st.sidebar.write(f"Categorical column detected. categories={len(categories)}")

            # iterate features and add properties.color
            for i, feat in enumerate(geojson.get("features", [])):
                try:
                    val = col_series.iloc[i]
                except Exception:
                    val = None
                if is_numeric:
                    feat_color = color_map_numeric(val, vmin, vmax, alpha=alpha)
                else:
                    feat_color = color_map_categorical(val, alpha=alpha)
                # store also a readable property to inspect in hover
                feat.setdefault("properties", {})
                feat["properties"]["color"] = feat_color
                feat["properties"][f"_color_by_{color_by}"] = val
        else:
            # no coloring column chosen -> use default static color
            for feat in geojson.get("features", []):
                feat.setdefault("properties", {})
                feat["properties"]["color"] = [200, 30, 0, alpha]

        # compute centroid for view
        centroid = gdf_valid.geometry.centroid.unary_union.centroid
        center_lat = float(centroid.y)
        center_lon = float(centroid.x)

        st.subheader("Map")
        # pydeck reads colors from properties.color with this string
        layer = pdk.Layer(
            "GeoJsonLayer",
            data=geojson,
            pickable=True,
            stroked=True,
            filled=True,
            get_fill_color="properties.color",
            get_line_color=[0, 0, 0],
            line_width_min_pixels=1,
        )

        view_state = pdk.ViewState(latitude=center_lat, longitude=center_lon, zoom=10)

        r = pdk.Deck(layers=[layer], initial_view_state=view_state)
        st.pydeck_chart(r)

        st.markdown("**Click a polygon in the map to inspect properties (pydeck hover/pick).**")

        # show attribute table including the selected color_by column
        cols_to_show = list(gdf_valid.drop(columns="geometry").columns)
        st.subheader("Attribute table (downloadable)")
        if color_by and color_by != "(none)":
            st.write(f"Colored by: **{color_by}**")
        st.dataframe(gdf_valid.drop(columns="geometry").head(200))

        csv = gdf_valid.drop(columns="geometry").to_csv(index=False)
        st.download_button("Download CSV", csv, file_name="boxes_attributes.csv", mime="text/csv")

# If no geometry, just show dataframe and allow download
if gdf is None:
    st.subheader("Download raw data as CSV")
    st.download_button("Download CSV", df.to_csv(index=False), file_name="boxes_raw.csv", mime="text/csv")
