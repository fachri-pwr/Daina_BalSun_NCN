# streamlit_app.py
import json
import requests
import pandas as pd
import streamlit as st

# Geospatial libraries
import geopandas as gpd
from shapely.geometry import shape
import folium
# NOTE: Using st_folium instead of deprecated folium_static
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("Streamlit — Visualize Geospatial Boxes from Django API")
st.divider()


# --- 1. Efficient Data Loading Function ---

@st.cache_data
def load_data(url):
    """
    Fetches data from the API, requesting the NDJSON stream,
    and processes it line-by-line to handle large datasets efficiently.
    """
    st.info(f"Fetching data from: {url}")

    try:
        # CRITICAL: Request the NDJSON format and stream the response
        response = requests.get(
            url,
            headers={'Accept': 'application/x-ndjson'},
            stream=True
        )
        response.raise_for_status()  # Check for HTTP errors (4xx or 5xx)

        # Process the streamed response line by line
        data = []
        for line in response.iter_lines():
            if line:
                try:
                    # Parse the JSON object from the line
                    json_obj = json.loads(line.decode('utf-8'))
                    data.append(json_obj)
                except json.JSONDecodeError as e:
                    st.warning(f"Skipping malformed JSON line: {e}")

        if not data:
            st.warning("No data found for the selected region.")
            return None

        # Create a single DataFrame from the list of dictionary records
        df = pd.DataFrame(data)
        return df

    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the API: {e}. Check if Django server is running and accessible.")
        return None


# --- 2. Visualization Function ---

def visualize_data(df):
    """Converts DataFrame to GeoDataFrame and plots the boxes on a map using Folium."""
    try:
        # A. Geometry Conversion
        # Convert the GeoJSON string in the 'geometry' column into Shapely objects
        df['geometry'] = df['geometry'].apply(lambda x: shape(json.loads(x)) if isinstance(x, str) else shape(x))

        # Create a GeoDataFrame
        gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")

        # B. Map Center (Fixed Deprecation)
        # Use union_all().centroid to calculate the center of all geometries
        center = gdf.geometry.union_all().centroid

        # C. Map Initialization
        m = folium.Map(
            location=[center.y, center.x],
            zoom_start=9,
            tiles='cartodbpositron'
        )

        # D. Add Geometries to Map
        for _, row in gdf.iterrows():
            folium.GeoJson(
                row.geometry.__geo_interface__,
                name=row['region_name'],
                tooltip=f"ID: {row['id']} | Region: {row['region_name']}"
            ).add_to(m)

        # E. Display Map (Fixed Deprecation)
        m.fit_bounds(m.get_bounds())
        st_folium(m, width=725, height=500)  # Use st_folium

    except Exception as e:
        st.error(f"Could not visualize data (Mapping error): {e}")


# --- 3. Streamlit App Layout ---

# A. Region Selection
selected_region = st.selectbox(
    'Select region you want to visualize',
    ('poland', 'opole', 'dolnoslaskie'),
    key='region_select'
)

# B. Dynamic URL Construction
if selected_region == 'poland':
    constructed_url = "http://127.0.0.1:8000/api/box/"
else:
    constructed_url = f"http://127.0.0.1:8000/api/box/?region_name={selected_region}"

# C. URL Display/Edit
API_URL = st.text_input(
    "Django API URL",
    value=constructed_url,
    help="This URL is dynamically generated based on your selection. You can edit it manually."
)

if not API_URL:
    st.stop()

# D. Load Button
if st.button(f"Load Data for {selected_region.capitalize()}"):
    # 1. Fetch data efficiently
    box_data_df = load_data(API_URL)

    # 2. Process and visualize the data
    if box_data_df is not None and not box_data_df.empty:
        if 'geometry' in box_data_df.columns:
            st.subheader(f"Map Visualization ({selected_region.capitalize()})")
            visualize_data(box_data_df)

            # 3. Add data table and download section
            st.subheader("Attribute table (first 200 rows)")
            st.dataframe(box_data_df.drop(columns='geometry', errors='ignore').head(200))

            csv = box_data_df.to_csv(index=False)
            st.download_button("Download Full Data CSV", csv, file_name=f"{selected_region}_boxes_raw.csv",
                               mime="text/csv")
        else:
            st.error(
                "The fetched data does not contain the required 'geometry' column for mapping. Check your Django serializer fields.")
    else:
        st.warning("Visualization failed: Data could not be loaded or was empty.")