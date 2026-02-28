import os
import numpy as np
import pandas as pd
import geopandas as gpd
from typing import Optional, Iterable
from pathlib import Path
from scipy.spatial import cKDTree


# 0. Read GeoJSON file
# centroid_box_path = "../data/extract_5km/centroid_box.geojson"
# centroid_dso_path = "../data/extract_5km/tauron_centroid.geojson"
# dso_centroid_score_path = "../data/extract_5km/tauron_centroid_score.geojson"

def read_geojson(path: str) -> gpd.GeoDataFrame:
    """Read a GeoJSON into a GeoDataFrame in WGS84 (EPSG:4326)."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p.resolve()}")
    gdf = gpd.read_file(p)              # <-- read the file (don’t pass the path to GeoDataFrame)
    if gdf.crs is None or gdf.crs.to_string().upper() != "EPSG:4326":
        gdf = gdf.to_crs(4326)
    return gdf

def haversine_vec(lat1, lon1, lat2, lon2):
    # lat1/lon1 shape (N,1), lat2/lon2 shape (1,M) -> result (N,M)
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    return 2 * 6371 * np.arcsin(np.sqrt(a))

def box2dso(main_centroid: gpd.GeoDataFrame, secondary_centroid: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    # main: N boxes; secondary: M DSOs
    lat_g = main_centroid["y"].to_numpy()[:, None]  # (N,1)
    lon_g = main_centroid["x"].to_numpy()[:, None]  # (N,1)
    lat_s = secondary_centroid["y"].to_numpy()[None, :]  # (1,M)
    lon_s = secondary_centroid["x"].to_numpy()[None, :]  # (1,M)

    D = haversine_vec(lat_g, lon_g, lat_s, lon_s)  # (N,M)
    idx_min = np.argmin(D, axis=1)                # (N,)
    dist_min = D[np.arange(D.shape[0]), idx_min]  # (N,)

    # prepare result (don’t mutate original)
    out = main_centroid.copy()
    out["nearest_dso_id"] = secondary_centroid["dso_id"].to_numpy()[idx_min]
    # keep x=lon, y=lat (no swap!)
    out["nearest_dso_x"]  = secondary_centroid["x"].to_numpy()[idx_min]
    out["nearest_dso_y"]  = secondary_centroid["y"].to_numpy()[idx_min]
    out["distance_km"]    = dist_min

    dmin, dmax = float(dist_min.min()), float(dist_min.max())
    out["score"] = 1.0 if dmax == dmin else 1.0 - (dist_min - dmin) / (dmax - dmin)
    
    return out


def box2railway(main_centroid: gpd.GeoDataFrame, secondary_centroid: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    # main: N boxes; secondary: M DSOs
    lat_g = main_centroid["y"].to_numpy()[:, None]  # (N,1)
    lon_g = main_centroid["x"].to_numpy()[:, None]  # (N,1)
    lat_s = secondary_centroid["y"].to_numpy()[None, :]  # (1,M)
    lon_s = secondary_centroid["x"].to_numpy()[None, :]  # (1,M)

    D = haversine_vec(lat_g, lon_g, lat_s, lon_s)  # (N,M)
    idx_min = np.argmin(D, axis=1)  # (N,)
    dist_min = D[np.arange(D.shape[0]), idx_min]  # (N,)

    # prepare result (don’t mutate original)
    out = main_centroid.copy()
    out["nearest_station_id"] = secondary_centroid["station_id"].to_numpy()[idx_min]
    # keep x=lon, y=lat (no swap!)
    out["nearest_station_x"] = secondary_centroid["x"].to_numpy()[idx_min]
    out["nearest_station_y"] = secondary_centroid["y"].to_numpy()[idx_min]
    out["distance_km"] = dist_min

    dmin, dmax = float(dist_min.min()), float(dist_min.max())
    out["score"] = 1.0 if dmax == dmin else 1.0 - (dist_min - dmin) / (dmax - dmin)

    return out

def box2road(main_centroid: gpd.GeoDataFrame, secondary_centroid: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    # main: N boxes; secondary: M DSOs
    lat_g = main_centroid["y"].to_numpy()[:, None]  # (N,1)
    lon_g = main_centroid["x"].to_numpy()[:, None]  # (N,1)
    lat_s = secondary_centroid["y"].to_numpy()[None, :]  # (1,M)
    lon_s = secondary_centroid["x"].to_numpy()[None, :]  # (1,M)

    D = haversine_vec(lat_g, lon_g, lat_s, lon_s)  # (N,M)
    idx_min = np.argmin(D, axis=1)  # (N,)
    dist_min = D[np.arange(D.shape[0]), idx_min]  # (N,)

    # prepare result (don’t mutate original)
    out = main_centroid.copy()
    out["nearest_road_id"] = secondary_centroid["road_id"].to_numpy()[idx_min]
    # keep x=lon, y=lat (no swap!)
    out["nearest_road_x"] = secondary_centroid["x"].to_numpy()[idx_min]
    out["nearest_road_y"] = secondary_centroid["y"].to_numpy()[idx_min]
    out["distance_km"] = dist_min

    dmin, dmax = float(dist_min.min()), float(dist_min.max())
    out["score"] = 1.0 if dmax == dmin else 1.0 - (dist_min - dmin) / (dmax - dmin)

    return out


def box2road_optimized(
        main_centroid: gpd.GeoDataFrame,
        secondary_centroid: gpd.GeoDataFrame,
        chunk_size: int = 10000
) -> gpd.GeoDataFrame:
    """
    Memory-efficient nearest neighbor search using chunking.

    Args:
        main_centroid: N boxes (300k rows)
        secondary_centroid: M roads (500k rows)
        chunk_size: Process main data in chunks to limit memory
    """
    N = len(main_centroid)
    M = len(secondary_centroid)

    # Pre-extract secondary data once
    lat_s = secondary_centroid["y"].to_numpy()  # (M,)
    lon_s = secondary_centroid["x"].to_numpy()  # (M,)
    osm_ids = secondary_centroid["osm_id"].to_numpy()

    # Pre-allocate result arrays
    nearest_ids = np.empty(N, dtype=osm_ids.dtype)
    nearest_x = np.empty(N, dtype=np.float64)
    nearest_y = np.empty(N, dtype=np.float64)
    distances = np.empty(N, dtype=np.float64)

    # Process in chunks
    for i in range(0, N, chunk_size):
        end = min(i + chunk_size, N)
        chunk_lat = main_centroid["y"].iloc[i:end].to_numpy()[:, None]  # (chunk,1)
        chunk_lon = main_centroid["x"].iloc[i:end].to_numpy()[:, None]  # (chunk,1)

        # Compute distances for this chunk: (chunk, M)
        D = haversine_vec(chunk_lat, chunk_lon, lat_s[None, :], lon_s[None, :])

        # Find nearest for each row in chunk
        idx_min = np.argmin(D, axis=1)
        dist_min = D[np.arange(D.shape[0]), idx_min]

        # Store results
        nearest_ids[i:end] = osm_ids[idx_min]
        nearest_x[i:end] = lon_s[idx_min]
        nearest_y[i:end] = lat_s[idx_min]
        distances[i:end] = dist_min

        # Optional: print progress
        if (i // chunk_size) % 10 == 0:
            print(f"Processed {end}/{N} rows ({100 * end / N:.1f}%)")

    # Build output
    out = main_centroid.copy()
    out["nearest_road_id"] = nearest_ids
    out["nearest_road_x"] = nearest_x
    out["nearest_road_y"] = nearest_y
    out["distance_km"] = distances

    # Compute score
    dmin, dmax = distances.min(), distances.max()
    out["score"] = 1.0 if dmax == dmin else 1.0 - (distances - dmin) / (dmax - dmin)

    return out

# ============================================================
# FASTER ALTERNATIVE: Use spatial indexing (KDTree)
# ============================================================

def box2road_kdtree(
        main_centroid: gpd.GeoDataFrame,
        secondary_centroid: gpd.GeoDataFrame
) -> gpd.GeoDataFrame:
    """
    Ultra-fast nearest neighbor using KDTree.
    Note: Uses Euclidean approximation, not exact haversine.
    Good for local distances (<100km).
    """
    # Build KDTree on secondary data
    coords_secondary = np.column_stack([
        secondary_centroid["x"].to_numpy(),
        secondary_centroid["y"].to_numpy()
    ])
    tree = cKDTree(coords_secondary)

    # Query nearest neighbor for each main point
    coords_main = np.column_stack([
        main_centroid["x"].to_numpy(),
        main_centroid["y"].to_numpy()
    ])
    distances, indices = tree.query(coords_main, k=1)

    # Convert Euclidean degrees to approximate km
    # (rough approximation: 1 degree ≈ 111 km at equator)
    distances_km = distances * 111.0

    # Build output
    out = main_centroid.copy()
    out["nearest_road_id"] = secondary_centroid["road_id"].iloc[indices].to_numpy()
    out["nearest_road_x"] = secondary_centroid["x"].iloc[indices].to_numpy()
    out["nearest_road_y"] = secondary_centroid["y"].iloc[indices].to_numpy()
    out["distance_km"] = distances_km

    # Compute score
    dmin, dmax = distances_km.min(), distances_km.max()
    out["score"] = 1.0 if dmax == dmin else 1.0 - (distances_km - dmin) / (dmax - dmin)

    return out

def box2plant(main_centroid: gpd.GeoDataFrame, secondary_centroid: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    # main: N boxes; secondary: M DSOs
    lat_g = main_centroid["y"].to_numpy()[:, None]  # (N,1)
    lon_g = main_centroid["x"].to_numpy()[:, None]  # (N,1)
    lat_s = secondary_centroid["y"].to_numpy()[None, :]  # (1,M)
    lon_s = secondary_centroid["x"].to_numpy()[None, :]  # (1,M)

    D = haversine_vec(lat_g, lon_g, lat_s, lon_s)  # (N,M)
    idx_min = np.argmin(D, axis=1)                # (N,)
    dist_min = D[np.arange(D.shape[0]), idx_min]  # (N,)

    # prepare result (don’t mutate original)
    out = main_centroid.copy()
    out["nearest_solar_id"] = secondary_centroid["solar_id"].to_numpy()[idx_min]
    # keep x=lon, y=lat (no swap!)
    out["nearest_solar_x"]  = secondary_centroid["x"].to_numpy()[idx_min]
    out["nearest_solar_y"]  = secondary_centroid["y"].to_numpy()[idx_min]
    out["distance_km"]    = dist_min

    dmin, dmax = float(dist_min.min()), float(dist_min.max())
    out["score"] = 1.0 if dmax == dmin else 1.0 - (dist_min - dmin) / (dmax - dmin)
    out['score'] = 1- out["score"]
    
    return out

def convert_geojson(gdf, out_path):
    if gdf.crs is None or gdf.crs.to_string().upper() != "EPSG:4326":
        gdf = gdf.to_crs(4326)
    gdf.to_file(out_path, driver="GeoJSON")  # writes a GeoJSON file




def power_plant_filter(centroid_plant_path: str, source_name) -> gpd.GeoDataFrame:

    gdf = read_geojson(centroid_plant_path)  # your existing loader

    # make sure the column exists (some datasets use 'source' instead)
    col = 'generator:source'
    if col not in gdf.columns:
        if 'source' in gdf.columns:
            col = 'source'
        else:
            raise KeyError("Neither 'generator:source' nor 'source' column found.")

    # normalize to lowercase strings
    col_vals = gdf[col].astype(str).str.strip().str.lower()

    # handle single or multiple targets
    if isinstance(source_name, (str, bytes)):
        targets = {source_name.strip().lower()}
    elif isinstance(source_name, Iterable):
        targets = {str(s).strip().lower() for s in source_name}
    else:
        raise TypeError("source_name must be a string or an iterable of strings.")

    mask = col_vals.isin(targets)
    gdf = gdf.loc[mask].copy()
    gdf = gdf.reset_index(drop=True)
    gdf["id"] = gdf.index.astype(int)
    return gdf

def runner_PV_Box2Dso(centroid_box_path, centroid_dso_path, output_path):
    box_gdf = read_geojson(centroid_box_path)
    dso_gdf = read_geojson(centroid_dso_path)
    dso_score = box2dso(box_gdf , dso_gdf)
    convert_geojson(dso_score, output_path)

def runner_PV_Box2Railway(centroid_box_path, centroid_railway_path, output_path):
    box_gdf = read_geojson(centroid_box_path)
    railway_gdf = read_geojson(centroid_railway_path)
    railway_score = box2railway(box_gdf , railway_gdf)
    convert_geojson(railway_score, output_path)

def runner_PV_Box2Road(centroid_box_path, centroid_road_path, output_path):
    box_gdf = read_geojson(centroid_box_path)
    road_gdf = read_geojson(centroid_road_path)
    road_score = box2road_kdtree(box_gdf , road_gdf)
    convert_geojson(road_score, output_path)

def runner_PV_Box2Plant(centroid_box_path, centroid_plant_path,output_path): #source_name
    box_gdf = read_geojson(centroid_box_path)
    plant_gdf = read_geojson(centroid_plant_path)# power_plant_filter(centroid_plant_path, source_name)
    plant_score =  box2plant(box_gdf , plant_gdf)
    convert_geojson(plant_score, output_path)
    
# def runner_PV_Box2DsoMocy(centroid_box_path, centroid_dso_path, output_path):
#     box_gdf = read_geojson(centroid_box_path)
#     dso_gdf = read_geojson(centroid_dso_path)
#     dso_score = box2dso(box_gdf , dso_gdf)
#     convert_geojson(dso_score, output_path)


# if __name__ == "__main__" :
   
#     centroid_plant_path = "../data/input/power_plant_dolnoslaskie.geojson"
#     centroid_box_path = "../data/extract_5km/centroid_box.geojson"
#     plant_source ="solar"
#     output_path = "../data/extract_5km/centroid_score_box2plant.geojson"


#     runner_PV_Box2Plant(centroid_box_path, centroid_plant_path, plant_source,output_path)

    # print(solar_plants.head(3))




