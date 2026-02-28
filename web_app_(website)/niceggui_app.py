import requests
import pandas as pd
import geopandas as gpd
from shapely.geometry import shape
import folium
from folium.plugins import MarkerCluster
from branca.colormap import linear
from nicegui import ui
import base64

# --- State Management ---
class AppState:
    def __init__(self):
        self.gdf = None
        self.boundary_data = None
        self.region_name = "wroclaw"

state = AppState()
API_BASE_URL = "http://127.0.0.1:8000"
SCORE_COLUMNS = ["box_id", "topsis_rank", "dni_score", "pvout_score", "dem_score", 
                 "dso_score", "temp_score", "solar_score", "land_score", "road_score", "station_score"]

ui.add_head_html("""
    <style>
    .number-icon {
        background-color: white; border: 2px solid #228B22; border-radius: 50%;
        color: black; font-weight: bold; text-align: center; font-size: 11px;
        line-height: 24px; width: 25px; height: 25px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    </style>
""")

async def fetch_data():
    with ui.spinner(size='lg'):
        try:
            score_url = f"{API_BASE_URL}/geojson/all/final_score/{state.region_name}"
            boundary_url = f"{API_BASE_URL}/geojson/all/boundary/{state.region_name}"
            
            score_res = requests.get(score_url)
            boundary_res = requests.get(boundary_url)

            if score_res.status_code == 200:
                data = score_res.json()
                if data:
                    df = pd.DataFrame(data)
                    df = df.dropna(subset=['geometry'])
                    df['geometry'] = df['geometry'].apply(lambda x: shape(x))
                    
                    for col in SCORE_COLUMNS:
                        if col in df.columns and col != "box_id":
                            df[col] = pd.to_numeric(df[col], errors='coerce')
                    
                    df = df.dropna(subset=['topsis_rank'])
                    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:2180")
                    
                    # Centroid calculation
                    centroids_4326 = gdf.geometry.centroid.to_crs(epsg=4326)
                    gdf['lat'] = centroids_4326.y
                    gdf['lon'] = centroids_4326.x
                    state.gdf = gdf.to_crs(epsg=4326)

                    # Update slider safely
                    max_r = int(state.gdf['topsis_rank'].max())
                    rank_slider.props(f'max={max_r}')
                    rank_slider.set_value([1, min(50, max_r)])
            
            if boundary_res.status_code == 200:
                b_data = boundary_res.json()
                state.boundary_data = b_data[0].get("geometry") if isinstance(b_data, list) and len(b_data) > 0 else b_data.get("geometry")
            
            ui.notify(f"Loaded {state.region_name}!", type='positive')
            update_ui()
        except Exception as e:
            ui.notify(f"Error: {e}", type='negative')

def update_ui():
    # 1. Guard Clause: Don't run if data isn't ready
    if state.gdf is None:
        return

    # 2. Guard Clause: Ensure slider values are numeric
    try:
        val_min, val_max = rank_slider.value
        # If NiceGUI passes 'min' or strings during init, this will fail gracefully
        low = float(val_min)
        high = float(val_max)
    except (ValueError, TypeError):
        return

    filtered = state.gdf[(state.gdf['topsis_rank'] >= low) & (state.gdf['topsis_rank'] <= high)].copy()
    
    if filtered.empty:
        map_container.content = '<div class="p-4">No data found in this range.</div>'
        return

    score_type = color_dropdown.value
    m = filtered.explore(
        column=score_type,
        cmap="viridis_r" if score_type == "topsis_rank" else "viridis",
        tiles="CartoDB positron",
        tooltip=["box_id", "topsis_rank"],
        popup=SCORE_COLUMNS,
        style_kwds=dict(weight=0.5, color="black", fillOpacity=0.2),
        legend=False
    )
    
    minv, maxv = float(filtered[score_type].min()), float(filtered[score_type].max())
    if minv != maxv:
        linear.viridis.scale(minv, maxv).to_step(6).add_to(m)

    if boundary_toggle.value and state.boundary_data:
        folium.GeoJson(state.boundary_data, style_function=lambda x: {"fillColor": "none", "color": "#FF0000", "weight": 4, "dashArray": "5, 5"}).add_to(m)

    marker_target = MarkerCluster().add_to(m) if cluster_toggle.value else m
    top_5 = filtered.nsmallest(5, 'topsis_rank')['topsis_rank'].tolist()

    for _, row in filtered.iterrows():
        rank = int(row['topsis_rank'])
        if pin_toggle.value and rank in top_5:
            folium.Marker([row['lat'], row['lon']], icon=folium.Icon(color='red')).add_to(m)
        if number_toggle.value:
            bg = "#FFD700" if rank <= 3 else "white"
            icon_html = f'<div class="number-icon" style="background-color: {bg};">{rank}</div>'
            folium.Marker([row['lat'], row['lon']], icon=folium.DivIcon(html=icon_html)).add_to(marker_target)

    # Encode Map
    map_html = m.get_root().render()
    encoded_map = base64.b64encode(map_html.encode()).decode()
    map_container.content = f'<iframe src="data:text/html;base64,{encoded_map}" style="width:100%; height:100%; border:none;"></iframe>'
    
    table.rows = filtered.drop(columns=['geometry']).sort_values("topsis_rank").to_dict('records')

# --- UI ---
with ui.header().classes('bg-blue-grey-10 items-center justify-between'):
    ui.label('🌍 PV Location Rank Dashboard').classes('text-h5 text-white')

with ui.left_drawer(value=True).classes('bg-slate-100'):
    with ui.column().classes('w-full p-2'):
        ui.input('Region Name').bind_value(state, 'region_name').classes('w-full')
        ui.button('Fetch Data', on_click=fetch_data).classes('w-full mt-2')
        ui.separator().classes('my-4')
        
        # Initialize with static numbers to avoid 'min'/'max' string issues
        rank_slider = ui.range(min=1, max=100, value=[1, 50], on_change=update_ui).props('label-always color=green')
        
        color_dropdown = ui.select(SCORE_COLUMNS[1:], value='topsis_rank', label='Color Map By', on_change=update_ui).classes('w-full')
        number_toggle = ui.checkbox('Show Rank Numbers', value=True, on_change=update_ui)
        pin_toggle = ui.checkbox('Show Top 5 Pins', value=False, on_change=update_ui)
        cluster_toggle = ui.checkbox('Cluster Markers', value=True, on_change=update_ui)
        boundary_toggle = ui.checkbox('Show Boundary', value=True, on_change=update_ui)

with ui.column().classes('w-full p-4 items-stretch'):
    map_container = ui.html('<i>Waiting for data...</i>').classes('w-full h-[600px] border rounded shadow-sm overflow-hidden')
    ui.label('📊 Detailed Data').classes('text-h5 mt-6')
    columns = [{'name': col, 'label': col.replace('_', ' ').title(), 'field': col, 'sortable': True} for col in SCORE_COLUMNS]
    table = ui.table(columns=columns, rows=[], row_key='box_id').classes('w-full mt-2')

ui.run(title="PV Rank Dashboard", port=8080)