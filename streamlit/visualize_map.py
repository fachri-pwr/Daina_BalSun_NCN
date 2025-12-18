import streamlit as st
import requests
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from shapely import wkt

# --- CONFIGURATION ---
st.set_page_config(page_title="Poland Boundary Viewer", layout="wide")
API_URL = "http://127.0.0.1:8000/api/map/"


# --- DATA PROCESSING FUNCTION ---
def get_gdf_from_api(category, name=None):
    """Fetches data from API and converts string geometry to GeoPandas"""
    params = {"category": category}
    if name:
        params["name"] = name

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        json_data = response.json()

        if not json_data:
            return gpd.GeoDataFrame()

        # Convert to DataFrame
        df = pd.DataFrame(json_data)

        # 1. Strip the 'SRID=4326;' prefix from the geometry string
        df['geometry'] = df['geometry'].apply(lambda x: x.split(';')[-1] if ';' in str(x) else x)

        # 2. Convert WKT strings to Shapely objects
        df['geometry'] = df['geometry'].apply(wkt.loads)

        # 3. Create GeoDataFrame and set active geometry
        gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")
        return gdf

    except Exception as e:
        st.error(f"Error: {e}")
        return gpd.GeoDataFrame()


# --- SIDEBAR UI ---
st.sidebar.title("🗺️ Map Controls")

# Selection 1: Choose category
category = st.sidebar.selectbox(
    "Select Category",
    ["country", "wojewodztwa", "powiatm"]
)

# Selection 2: Dynamic Name Filter (Only for provinces/districts)
selected_name = None
if category != "country":
    # Fetch all names for this category to fill the dropdown
    with st.spinner("Fetching list..."):
        full_list_gdf = get_gdf_from_api(category)

    if not full_list_gdf.empty:
        names = sorted(full_list_gdf['name'].unique().tolist())
        selected_name = st.sidebar.selectbox(f"Select specific {category}", ["Show All"] + names)

# --- MAIN LOGIC ---
st.title(f"Visualizing: {category.capitalize()}")

# Fetch the final data based on filters
query_name = None if selected_name == "Show All" else selected_name
gdf = get_gdf_from_api(category, name=query_name)

if not gdf.empty:
    # Create the Map
    # Center map based on data bounds
    bounds = gdf.total_bounds  # [minx, miny, maxx, maxy]
    m = folium.Map(location=[52.0, 19.0], zoom_start=6, tiles="CartoDB Positron")

    # Add Geometry to Map
    folium.GeoJson(
        gdf,
        style_function=lambda x: {
            'fillColor': '#3186cc',
            'color': 'black',
            'weight': 1.5,
            'fillOpacity': 0.5
        },
        tooltip=folium.GeoJsonTooltip(fields=['name', 'osm_map_id'], aliases=['Name:', 'ID:'])
    ).add_to(m)

    # Automatically zoom the map to fit the selected geometry
    m.fit_bounds([[bounds[1], bounds[0]], [bounds[3], bounds[2]]])

    # Display Map
    st_folium(m, width="100%", height=600)

    # Show Data Table
    with st.expander("Show Attribute Table"):
        st.dataframe(gdf.drop(columns='geometry'), use_container_width=True)
else:
    st.warning("No data found. Please check if your Django server is running.")

# --- FOOTER ---
st.sidebar.info(f"Loaded {len(gdf)} features.")