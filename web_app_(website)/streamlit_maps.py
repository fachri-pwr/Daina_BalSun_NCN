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

# --- 1. Helper Classes & Styling ---
class ResizeLegend(MacroElement):
    """Custom CSS injector to make the Folium legend look better in Streamlit."""
    def __init__(self):
        super().__init__()
        self._template = Template("""
        {% macro script(this, kwargs) %}
        var bar = document.getElementsByClassName('legend')[0];
        if(bar){
            bar.style.width = '550px';
            bar.style.margin = '0 auto';
        }
        {% endmacro %}
        """)

st.set_page_config(layout="wide", page_title="GeoSpatial Rank Dashboard")

st.markdown("""
    <style>
    .number-icon {
        background-color: white; border: 2px solid #228B22; border-radius: 50%;
        color: black; font-weight: bold; text-align: center; font-size: 11px;
        line-height: 24px; width: 25px; height: 25px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    .top-rank-card {
        padding: 15px; border-radius: 10px; border-left: 5px solid #FFD700;
        background-color: #f0f2f6; margin-bottom: 10px; height: 110px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 PV Location Rank Dashboard | Daina NCN ")

# --- 2. Configuration & State ---
API_BASE_URL = "http://127.0.0.1:8000"
SCORE_COLUMNS = ["box_id", "topsis_rank", "dni_score", "pvout_score", "dem_score", "dso_score", "temp_score", "solar_score", "land_score", "road_score", "station_score"]

if "gdf" not in st.session_state:
    st.session_state["gdf"] = None
if "boundary_data" not in st.session_state:
    st.session_state["boundary_data"] = None

# --- 3. Sidebar: Data Management ---
st.sidebar.header("🌍 Data Management")
region_name = st.sidebar.selectbox("Enter Region Name",("wroclaw", 'dolnoslaskie'))

if st.sidebar.button("Fetch Data from API"):
    with st.spinner(f"Fetching data for {region_name}..."):
        try:
            score_res = requests.get(f"{API_BASE_URL}/geojson/all/final_score/{region_name}")
            boundary_res = requests.get(f"{API_BASE_URL}/geojson/all/boundary/{region_name}")

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
                    gdf_4326 = gdf.to_crs(epsg=4326)
                    gdf_4326['lat'] = gdf_4326.geometry.centroid.y
                    gdf_4326['lon'] = gdf_4326.geometry.centroid.x
                    st.session_state["gdf"] = gdf_4326

            if boundary_res.status_code == 200:
                b_list = boundary_res.json()
                st.session_state["boundary_data"] = b_list[0].get("geometry") if isinstance(b_list, list) and b_list else b_list.get("geometry")
            
            st.sidebar.success(f"Loaded {region_name}!")
        except Exception as e:
            st.sidebar.error(f"Error connecting to API: {e}")

# --- 4. Main Dashboard Logic ---
if st.session_state["gdf"] is not None:
    gdf_web = st.session_state["gdf"]
    boundary_geom = st.session_state["boundary_data"]
    
    st.sidebar.markdown("---")
    min_r, max_r = int(gdf_web['topsis_rank'].min()), int(gdf_web['topsis_rank'].max())
    rank_range = st.sidebar.slider("Rank Range Filter", min_r, max_r, (min_r, min(min_r+20, max_r)))
    
    show_top_labels_only = st.sidebar.checkbox("Show Labels for Top 5 Only", value=True)
    show_boundary = st.sidebar.checkbox("Show Region Boundary", value=True)

    filtered_gdf = gdf_web[(gdf_web['topsis_rank'] >= rank_range[0]) & (gdf_web['topsis_rank'] <= rank_range[1])].copy()

    if not filtered_gdf.empty:
        st.subheader(f"🏆 Spotlight: Top 5 in Selected Range")
        dynamic_top_5 = filtered_gdf.nsmallest(5, 'topsis_rank')
        top_5_ids = dynamic_top_5['box_id'].tolist()
        
        cols = st.columns(5)
        for i, (idx, row) in enumerate(dynamic_top_5.iterrows()):
            with cols[i]:
                st.markdown(f"""
                    <div class="top-rank-card">
                        <strong>Rank #{int(row['topsis_rank'])}</strong><br>
                        <small>ID: {row['box_id']}</small><br>
                        <small>{row['lat']:.4f}, {row['lon']:.4f}</small>
                    </div>
                """, unsafe_allow_html=True)
                gmaps_url = f"https://www.google.com/maps/search/?api=1&query={row['lat']},{row['lon']}"
                st.link_button(f"📍 View on Google Map", gmaps_url, use_container_width=True)

        st.markdown("---")
        score_type = st.selectbox("Color Polygons By:", [c for c in SCORE_COLUMNS if c != 'box_id'])

        # --- 5. Folium Map Creation (FIXED FOR OSM DEFAULT) ---
        m = folium.Map(
            location=[filtered_gdf['lat'].mean(), filtered_gdf['lon'].mean()], 
            zoom_start=14, 
            tiles=None  # Start with nothing to control the order
        )

        # First TileLayer added with overlay=False becomes the DEFAULT active radio button
        folium.TileLayer(
            'openstreetmap', 
            name='openstreetmap', 
            overlay=False, 
            control=True
        ).add_to(m)

        # Second radio button option
        folium.TileLayer(
            tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
            attr='Google', 
            name='Google Satellite', 
            overlay=False,
            control=True
        ).add_to(m)

        # Add the polygons - tiles=None is CRITICAL here
        filtered_gdf.explore(
            m=m,
            column=score_type,
            cmap="viridis_r" if score_type == "topsis_rank" else "viridis",
            tooltip=["box_id", "topsis_rank"],
            popup=SCORE_COLUMNS,
            style_kwds=dict(weight=1, color="white", fillOpacity=0.5),
            legend=False,
            name="Property Scores",
            tiles=None  # Stops explore() from overriding your radio button selection
        )
        
        # Color Scale Legend
        minv, maxv = float(filtered_gdf[score_type].min()), float(filtered_gdf[score_type].max())
        cmap = linear.viridis.scale(minv, maxv).to_step(6)
        cmap.caption = score_type.replace("_", " ").title()
        cmap.add_to(m)
        m.get_root().add_child(ResizeLegend())

        # Top 5 Neon Property Lines Highlight
        folium.GeoJson(
            dynamic_top_5,
            name="Top 5 Highlight Lines",
            style_function=lambda x: {'fillColor': 'none', 'color': '#f7d702', 'weight': 3, "dashArray": "3,5"}
        ).add_to(m)

        # Markers Logic
        for _, row in filtered_gdf.iterrows():
            rank_val = int(row['topsis_rank'])
            if row['box_id'] in top_5_ids:
                folium.Marker(
                    location=[row['lat'], row['lon']],
                    icon=folium.Icon(color='red', icon='star'),
                    tooltip=f"Rank {rank_val}"
                ).add_to(m)
                
                if show_top_labels_only:
                    bg = "#FFD700" if rank_val <= 3 else "white"
                    icon_html = f'<div class="number-icon" style="background-color: {bg};">{rank_val}</div>'
                    folium.Marker(
                        location=[row['lat'], row['lon']], 
                        icon=folium.DivIcon(html=icon_html, icon_anchor=(12, 12))
                    ).add_to(m)

        if show_boundary and boundary_geom:
            folium.GeoJson(
                boundary_geom, name="Region Boundary",
                style_function=lambda x: {"fillColor": "none", "color": "#FF0000", "weight": 4, "dashArray": "5, 5"}
            ).add_to(m)
        
        # LayerControl shows the radio buttons
        folium.LayerControl(collapsed=False).add_to(m)
        st_folium(m, width="100%", height=600, returned_objects=[])

        # --- 6. Table & Export ---
        st.subheader("📊 Detailed Data Table")
        display_df = filtered_gdf.drop(columns=['geometry']).sort_values("topsis_rank")
        st.dataframe(display_df, use_container_width=True, hide_index=True)
        
        csv = display_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=csv,
            file_name=f"{region_name}_filtered_ranks.csv",
            mime="text/csv",
            use_container_width=True
        )
    else:
        st.warning("No properties found in this range.")