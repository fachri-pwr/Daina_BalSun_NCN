import json
import requests
import pandas as pd
import streamlit as st
import geopandas as gpd
from shapely import wkt
from shapely.geometry import shape
import pydeck as pdk

st.set_page_config(layout="wide")
st.title("Streamlit — Full Dataset Visualizer")

# --- 1. Selection Logic ---
api_choice = st.selectbox('Select Data Mode', ('box', 'tauron'))

if api_choice == 'box':
    urls_to_fetch = ["http://127.0.0.1:8000/api/box/"]
else:
    urls_to_fetch = [
        "http://127.0.0.1:8000/api/map/",
        "http://127.0.0.1:8000/api/bazamocy/"
    ]


# --- 2. Helper Functions ---
def parse_geometry_field(val):
    if not val: return None
    try:
        if isinstance(val, str) and ";" in val:
            return wkt.loads(val.split(";", 1)[1])
        if isinstance(val, (dict, list)): return shape(val)
        return wkt.loads(val)
    except:
        return None


@st.cache_data(show_spinner=False)
def collect_all_data(urls):
    combined_records = []
    for url in urls:
        next_url = url
        while next_url:
            try:
                resp = requests.get(next_url)
                if resp.status_code != 200: break
                data = resp.json()
                results = data.get("results", [])

                # Fix for the 'osm_box_id' vs 'osm_dso_id' error
                for record in results:
                    if 'osm_box_id' not in record and 'osm_dso_id' in record:
                        record['osm_box_id'] = record['osm_dso_id']

                combined_records.extend(results)
                next_url = data.get("next")
            except Exception as e:
                st.error(f"Error: {e}")
                break
    return combined_records


# --- 3. Main Execution ---
if st.button("Load All Data from API"):
    raw_data = collect_all_data(urls_to_fetch)

    if raw_data:
        # Create Dataframe
        df = pd.DataFrame(raw_data)

        with st.spinner("Processing Dataset..."):
            geoms = df["geometry"].apply(parse_geometry_field)
            gdf = gpd.GeoDataFrame(df.drop(columns=["geometry"]), geometry=geoms, crs="EPSG:2180")
            gdf = gdf.to_crs(epsg=4326)
            features = json.loads(gdf.to_json())

        # --- Map Section ---
        st.subheader(f"Map Visualization: {len(gdf)} records")
        avg_lon = gdf.geometry.centroid.x.mean()
        avg_lat = gdf.geometry.centroid.y.mean()

        layer_color = [50, 150, 255, 160] if api_choice == 'box' else [255, 80, 0, 160]

        st.pydeck_chart(pdk.Deck(
            layers=[pdk.Layer(
                "GeoJsonLayer",
                features,
                pickable=True,
                stroked=True,
                filled=True,
                get_fill_color=layer_color,
                get_line_color=[255, 255, 255],
                line_width_min_pixels=1,
                point_radius_min_pixels=5,
            )],
            initial_view_state=pdk.ViewState(latitude=avg_lat, longitude=avg_lon, zoom=7),
            tooltip={"text": "ID: {osm_box_id}"}
        ))

        # --- 4. Data Table Section (Pagination) ---
        st.divider()
        st.subheader("📋 Raw Data Records")

        # Define page size and calculation
        page_size = 15
        total_rows = len(df)
        total_pages = (total_rows // page_size) + (1 if total_rows % page_size > 0 else 0)

        # Pagination UI
        col1, col2 = st.columns([1, 4])
        with col1:
            page_num = st.number_input(f"Page (1-{total_pages})", min_value=1, max_value=total_pages, step=1)

        # Calculate slices
        start_idx = (page_num - 1) * page_size
        end_idx = start_idx + page_size

        # Show the slice of data
        st.write(f"Showing results {start_idx + 1} to {min(end_idx, total_rows)} of {total_rows}")
        st.dataframe(df.iloc[start_idx:end_idx], use_container_width=True)

        # Option to download full data
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Full CSV", data=csv, file_name=f"{api_choice}_data.csv", mime='text/csv')

    else:
        st.warning("No data found.")