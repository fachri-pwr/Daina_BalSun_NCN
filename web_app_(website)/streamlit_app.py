import streamlit as st
import requests
import pandas as pd
import geopandas as gpd
from shapely.geometry import shape
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
from branca.colormap import linear
from branca.element import MacroElement
from jinja2 import Template

# --- Configuration ---
st.set_page_config(layout="wide", page_title="GeoSpatial Rank Dashboard")

st.markdown("""
    <style>
    .number-icon {
        background-color: white;
        border: 2px solid #228B22;
        border-radius: 50%;
        color: black;
        font-weight: bold;
        text-align: center;
        font-size: 11px;
        line-height: 24px;
        width: 25px;
        height: 25px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 PV Location Rank Dashboard")

API_BASE_URL = "http://127.0.0.1:8000"
SCORE_COLUMNS = ["box_id", "topsis_rank", "dni_score", "pvout_score",'dem_score','dso_score' ,"temp_score", "solar_score", "land_score",'road_score','station_score']

# --- Sidebar ---
st.sidebar.header("Data Management")
region_name = st.sidebar.text_input("Enter Region Name", value="wroclaw")

if st.sidebar.button("Fetch Data from API"):
    with st.spinner(f"Fetching data for {region_name}..."):
        score_url = f"{API_BASE_URL}/geojson/all/final_score/{region_name}"
        boundary_url = f"{API_BASE_URL}/geojson/all/boundary/{region_name}"
        
        try:
            # 1. Fetch Scores
            score_res = requests.get(score_url)
            # 2. Fetch Boundary
            boundary_res = requests.get(boundary_url)

            # --- Handle Scores ---
            if score_res.status_code == 200:
                data = score_res.json()
                if data:
                    df = pd.DataFrame(data)
                    df = df.dropna(subset=['geometry'])
                    df['geometry'] = df['geometry'].apply(lambda x: shape(x))
                    
                    for col in SCORE_COLUMNS:
                        if col in df.columns and col != "box_id":
                            df[col] = pd.to_numeric(df[col], errors='coerce')

                    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:2180")
                    gdf = gdf.to_crs(epsg=4326)
                    gdf['lat'] = gdf.geometry.centroid.y
                    gdf['lon'] = gdf.geometry.centroid.x
                    st.session_state["gdf"] = gdf

            # --- Handle Boundary (FIXED FOR LIST RESPONSE) ---
            if boundary_res.status_code == 200:
                boundary_list = boundary_res.json()
                # Check if the list is not empty before accessing index 0
                if isinstance(boundary_list, list) and len(boundary_list) > 0:
                    # Your API returns a list, so we take the first item
                    st.session_state["boundary_data"] = boundary_list[0].get("geometry")
                elif isinstance(boundary_list, dict):
                    # Fallback if you later change API to return a single dict
                    st.session_state["boundary_data"] = boundary_list.get("geometry")
                else:
                    st.session_state["boundary_data"] = None
            else:
                st.session_state["boundary_data"] = None
                st.sidebar.warning("Boundary geometry not found.")

            st.sidebar.success(f"Loaded {region_name}!")
        except Exception as e:
            st.sidebar.error(f"Error: {e}")

# --- Main Logic ---
if "gdf" in st.session_state:
    gdf_web = st.session_state["gdf"]
    boundary_geom = st.session_state.get("boundary_data")
    
    st.sidebar.markdown("---")
    min_r, max_r = int(gdf_web['topsis_rank'].min()), int(gdf_web['topsis_rank'].max())
    rank_range = st.sidebar.slider("Rank Range Filter", min_r, max_r, (min_r, min(min_r+20, max_r)))
    
    show_numbers = st.sidebar.checkbox("Show All Rank Numbers", value=True)
    show_top_markers = st.sidebar.checkbox("Show Top 5 Pins (Red)", value=False)
    use_clustering = st.sidebar.checkbox("Cluster Markers", value=True)
    show_boundary = st.sidebar.checkbox("Show Region Boundary", value=True)

    filtered_gdf = gdf_web[
        (gdf_web['topsis_rank'] >= rank_range[0]) & 
        (gdf_web['topsis_rank'] <= rank_range[1])
    ].copy()

    top_5_in_range = filtered_gdf.nsmallest(5, 'topsis_rank')['topsis_rank'].tolist()
    score_type = st.selectbox("Color Map By:", SCORE_COLUMNS[1:]) 

    if not filtered_gdf.empty:
        # 1. Base Map with Grid
        m = filtered_gdf.explore(
            column=score_type,
            cmap="viridis_r" if score_type == "topsis_rank" else "viridis",
            tooltip=["box_id", "topsis_rank"],
            popup=SCORE_COLUMNS,
            tiles="CartoDB positron",
            style_kwds=dict(weight=0.5, color="black", fillOpacity=0.2),
            legend=False
        )
        minv,maxv=float(filtered_gdf[score_type].min()),float(filtered_gdf[score_type].max())
        cmap=linear.viridis.scale(minv,maxv).to_step(6)
        cmap.caption=score_type
        cmap.add_to(m)
        
        class ResizeLegend(MacroElement):
            def __init__(self):
                super().__init__()
                self._template=Template("""
                {% macro script(this, kwargs) %}
                var bar=document.getElementsByClassName('legend')[0];
                if(bar){
                    bar.style.width='550px';
                    bar.style.margin='0 auto';
                }
                {% endmacro %}
                """)

        m.get_root().add_child(ResizeLegend())

        # 2. OVERLAP BOUNDARY
        if show_boundary and boundary_geom:
            folium.GeoJson(
                boundary_geom,
                name=f"{region_name} Boundary",
                style_function=lambda x: {
                    "fillColor": "none",
                    "color": "#FF0000",
                    "weight": 4,
                    "dashArray": "5, 5"
                }
            ).add_to(m)

        # 3. Markers
        marker_target = MarkerCluster().add_to(m) if use_clustering else m
        for _, row in filtered_gdf.iterrows():
            rank_val = int(row['topsis_rank'])
            if show_top_markers and rank_val in top_5_in_range:
                folium.Marker(
                    location=[row['lat'], row['lon']],
                    icon=folium.Icon(color='red', icon='info-sign'),
                    tooltip=f"Top Rank: {rank_val}"
                ).add_to(m)
            if show_numbers:
                bg_color = "#FFD700" if rank_val <= 3 else "white"
                icon_html = f'''<div class="number-icon" style="background-color: {bg_color};">{rank_val}</div>'''
                folium.Marker(location=[row['lat'], row['lon']], icon=folium.DivIcon(html=icon_html)).add_to(marker_target)
        
        st_folium(m, width=1200, height=600, returned_objects=[])
    # --- Table View ---
        st.markdown("---")
        st.subheader(f"📊 Detailed Data for {region_name}")
        
        # We sort by rank by default so the best locations are at the top
        display_df = filtered_gdf.drop(columns=['geometry']).sort_values("topsis_rank")
        display_df = display_df[['topsis_rank','id','box_id','lat','lon','area','perimeter','fclass','region_name','dni_score','dem_score','pvout_score','temp_score','dso_score','solar_score','station_score','road_score','land_score','topsis_score']]
        
        # Display the interactive dataframe
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            # column_config={
            #     "topsis_rank": st.column_config.NumberColumn("Rank 🏆", format="%d"),
            #     "box_id": "ID",
            #     "dni_score": st.column_config.ProgressColumn("DNI Score", min_value=0, max_value=1),
            #     "pvout_score": st.column_config.ProgressColumn("PVOUT Score", min_value=0, max_value=1),
            # }
        )

        # Optional: Add a download button for the filtered data
        csv = display_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=csv,
            file_name=f"{region_name}_rankings.csv",
            mime="text/csv",
        )
    else:
        st.warning("No data found for this rank range.")
        
        
        

# import streamlit as st
# import requests
# import pandas as pd
# import geopandas as gpd
# from shapely.geometry import shape
# from streamlit_folium import st_folium
# import folium
# from folium.plugins import MarkerCluster
# from branca.colormap import linear
# from branca.element import MacroElement
# from jinja2 import Template

# # --- 1. Helper Classes ---
# class ResizeLegend(MacroElement):
#     """Custom CSS injector to make the Folium legend look better in Streamlit."""
#     def __init__(self):
#         super().__init__()
#         self._template = Template("""
#         {% macro script(this, kwargs) %}
#         var bar = document.getElementsByClassName('legend')[0];
#         if(bar){
#             bar.style.width = '550px';
#             bar.style.margin = '0 auto';
#         }
#         {% endmacro %}
#         """)

# # --- 2. Configuration ---
# st.set_page_config(layout="wide", page_title="GeoSpatial Rank Dashboard")

# st.markdown("""
#     <style>
#     .number-icon {
#         background-color: white; border: 2px solid #228B22; border-radius: 50%;
#         color: black; font-weight: bold; text-align: center; font-size: 11px;
#         line-height: 24px; width: 25px; height: 25px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
#     }
#     .top-rank-card {
#         padding: 15px; border-radius: 10px; border-left: 5px solid #FFD700;
#         background-color: #f0f2f6; margin-bottom: 10px; height: 110px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.title("🌍 PV Location Rank Dashboard")

# API_BASE_URL = "http://127.0.0.1:8000"
# SCORE_COLUMNS = ["box_id", "topsis_rank", "dni_score", "pvout_score",'dem_score','dso_score' ,"temp_score", "solar_score", "land_score",'road_score','station_score']

# # --- 3. Data Management ---
# if "gdf" not in st.session_state:
#     st.session_state["gdf"] = None

# st.sidebar.header("Data Management")
# region_name = st.sidebar.text_input("Enter Region Name", value="wroclaw")

# if st.sidebar.button("Fetch Data from API"):
#     with st.spinner(f"Fetching data for {region_name}..."):
#         try:
#             score_res = requests.get(f"{API_BASE_URL}/geojson/all/final_score/{region_name}")
#             boundary_res = requests.get(f"{API_BASE_URL}/geojson/all/boundary/{region_name}")

#             if score_res.status_code == 200:
#                 data = score_res.json()
#                 if data:
#                     df = pd.DataFrame(data)
#                     df = df.dropna(subset=['geometry'])
#                     df['geometry'] = df['geometry'].apply(lambda x: shape(x))
                    
#                     for col in SCORE_COLUMNS:
#                         if col in df.columns and col != "box_id":
#                             df[col] = pd.to_numeric(df[col], errors='coerce')

#                     # Calculate Centroids in Projected CRS (EPSG:2180) for accuracy
#                     gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:2180")
#                     # Accurate lat/lon for markers/Google links
#                     centroids_4326 = gdf.geometry.centroid.to_crs(epsg=4326)
#                     gdf['lat'] = centroids_4326.y
#                     gdf['lon'] = centroids_4326.x
                    
#                     # Convert whole GDF to WGS84 for Folium
#                     st.session_state["gdf"] = gdf.to_crs(epsg=4326)

#             if boundary_res.status_code == 200:
#                 b_list = boundary_res.json()
#                 st.session_state["boundary_data"] = b_list[0].get("geometry") if isinstance(b_list, list) and b_list else b_list.get("geometry")
            
#             st.sidebar.success(f"Loaded {region_name}!")
#         except Exception as e:
#             st.sidebar.error(f"Error: {e}")

# # --- 4. Main Logic ---
# if st.session_state["gdf"] is not None:
#     gdf_web = st.session_state["gdf"]
#     boundary_geom = st.session_state.get("boundary_data")
    
#     st.sidebar.markdown("---")
#     min_r, max_r = int(gdf_web['topsis_rank'].min()), int(gdf_web['topsis_rank'].max())
#     rank_range = st.sidebar.slider("Rank Range Filter", min_r, max_r, (min_r, min(min_r+20, max_r)))
    
#     show_numbers = st.sidebar.checkbox("Show All Rank Numbers", value=True)
#     show_top_markers = st.sidebar.checkbox("Highlight Top 5 in Range", value=True)
#     use_clustering = st.sidebar.checkbox("Cluster Markers", value=True)
#     show_boundary = st.sidebar.checkbox("Show Region Boundary", value=True)

#     # Filter data based on range
#     filtered_gdf = gdf_web[
#         (gdf_web['topsis_rank'] >= rank_range[0]) & 
#         (gdf_web['topsis_rank'] <= rank_range[1])
#     ].copy()

#     if not filtered_gdf.empty:
#         # --- NEW: Dynamic Top 5 in Range Spotlight ---
#         st.subheader(f"🏆 Spotlight: Top 5 in Selected Range (Rank {rank_range[0]} - {rank_range[1]})")
#         dynamic_top_5 = filtered_gdf.nsmallest(5, 'topsis_rank')
        
#         cols = st.columns(5)
#         for i, (idx, row) in enumerate(dynamic_top_5.iterrows()):
#             with cols[i]:
#                 st.markdown(f"""
#                     <div class="top-rank-card">
#                         <strong>Rank #{int(row['topsis_rank'])}</strong><br>
#                         <small>Box ID: {row['box_id']}</small><br>
#                         <small>Coords: {row['lat']:.4f}, {row['lon']:.4f}</small>
#                     </div>
#                 """, unsafe_allow_html=True)
#                 # Google Maps Link for specific marker
#                 gmaps_single_url = f"https://www.google.com/maps/search/?api=1&query={row['lat']},{row['lon']}"
#                 st.link_button(f"📍 View Location", gmaps_single_url, use_container_width=True)

#         # --- NEW: Bounding Box Sidebar Link ---
#         min_lon, min_lat, max_lon, max_lat = filtered_gdf.total_bounds
#         # Using a bounding box view in Google Maps (requires specific URL parameters)
#         bbox_url = f"https://www.google.com/maps/@{(min_lat+max_lat)/2},{(min_lon+max_lon)/2},15z/data=!3m1!1e3"
#         # Alternative: Search query that forces Google to focus on the area
#         # st.sidebar.markdown("---")
#         # st.sidebar.subheader("🗺️ Area Controls")
#         # st.sidebar.link_button("🔗 View Area in Google Maps", bbox_url, use_container_width=True)

#         st.markdown("---")
#         score_type = st.selectbox("Color Map By:", SCORE_COLUMNS[1:]) 

#         # --- 5. Folium Map Creation ---
#         m = filtered_gdf.explore(
#             column=score_type,
#             cmap="viridis_r" if score_type == "topsis_rank" else "viridis",
#             tooltip=["box_id", "topsis_rank"],
#             popup=SCORE_COLUMNS,
#             tiles="CartoDB positron",
#             style_kwds=dict(weight=0.5, color="black", fillOpacity=0.2),
#             legend=False
#         )
        
#         # Color Scale / Legend
#         minv, maxv = float(filtered_gdf[score_type].min()), float(filtered_gdf[score_type].max())
#         cmap = linear.viridis.scale(minv, maxv).to_step(6)
#         cmap.caption = score_type
#         cmap.add_to(m)
#         m.get_root().add_child(ResizeLegend())

#         if show_boundary and boundary_geom:
#             folium.GeoJson(
#                 boundary_geom,
#                 style_function=lambda x: {"fillColor": "none", "color": "#FF0000", "weight": 4, "dashArray": "5, 5"}
#             ).add_to(m)

#         marker_target = MarkerCluster().add_to(m) if use_clustering else m
#         top_5_ids = dynamic_top_5['box_id'].tolist()
        
#         for _, row in filtered_gdf.iterrows():
#             rank_val = int(row['topsis_rank'])
#             # Red Stars for the Top 5 within the current slider range
#             if show_top_markers and row['box_id'] in top_5_ids:
#                 folium.Marker(
#                     location=[row['lat'], row['lon']],
#                     icon=folium.Icon(color='red', icon='star'),
#                     tooltip=f"IN-RANGE LEADER: Rank {rank_val}"
#                 ).add_to(m)
#             # Standard Rank Number Icons
#             if show_numbers:
#                 bg = "#FFD700" if rank_val <= 3 else "white"
#                 icon_html = f'<div class="number-icon" style="background-color: {bg};">{rank_val}</div>'
#                 folium.Marker(location=[row['lat'], row['lon']], icon=folium.DivIcon(html=icon_html)).add_to(marker_target)
        
#         st_folium(m, width=1200, height=600, returned_objects=[])

#         # --- 6. Table & Export ---
#         st.markdown("---")
#         st.subheader(f"📊 Detailed Data Table")
#         display_df = filtered_gdf.drop(columns=['geometry']).sort_values("topsis_rank")
#         st.dataframe(display_df, use_container_width=True, hide_index=True)
        
#         csv = display_df.to_csv(index=False).encode('utf-8')
#         st.download_button("📥 Download Filtered Data as CSV", csv, f"{region_name}_ranks.csv", "text/csv")
#     else:
#         st.warning("No data found for this range. Adjust the slider filters.")