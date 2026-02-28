import pandas as pd
import geopandas as gpd
from pathlib import Path
from functools import reduce
import matplotlib.pyplot as plt
import os
import sys
import argparse
import json
from shapely.geometry import shape, mapping


def read_geojson(path: str) -> gpd.GeoDataFrame:
    """Read a GeoJSON into a GeoDataFrame in WGS84 (EPSG:4326)."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {p.resolve()}")

    # Read the GeoJSON as raw JSON first
    with open(p, 'r') as f:
        geojson_data = json.load(f)

    # Explode multi-part geometries at the feature level
    exploded_features = []
    for feature in geojson_data['features']:
        geom = shape(feature['geometry'])
        props = feature.get('properties', {})

        # Check if it's a multi-part geometry
        if geom.geom_type.startswith('Multi'):
            # Explode into individual parts
            for part in geom.geoms:
                new_feature = {
                    'type': 'Feature',
                    'geometry': mapping(part),
                    'properties': props.copy()
                }
                exploded_features.append(new_feature)
        else:
            exploded_features.append(feature)

    # Create new GeoJSON structure
    exploded_geojson = {
        'type': 'FeatureCollection',
        'features': exploded_features
    }

    # Now read with geopandas
    gdf = gpd.GeoDataFrame.from_features(exploded_geojson['features'])

    # Set CRS
    if 'crs' in geojson_data:
        gdf.crs = geojson_data['crs']

    # Ensure WGS84
    if gdf.crs is None or gdf.crs.to_string().upper() != "EPSG:4326":
        gdf = gdf.to_crs(4326)

    return gdf


def landuse_score(path):
    df = read_geojson(path)
    df = df[df['fclass'].isin(['meadow', 'grass', 'farmland', 'scrub', 'farmyard', 'heath'])]
    sum_cols = ['area_2', 'area', 'ratio']
    # sums per id
    sums = df.groupby('id', as_index=False)[sum_cols].mean()
    # mode fclass per id (handles ties)
    modes = (df.groupby('id')['fclass']
             .agg(lambda s: s.mode().iat[0])
             .reset_index())
    # keep first row per id for other cols, then attach sums and mode fclass
    out = (df.drop_duplicates('id', keep='first')
           .drop(columns=sum_cols + ['fclass'], errors='ignore')
           .merge(sums, on='id')
           .merge(modes, on='id'))
    out = out[['id', 'ratio']]
    out = out.rename(columns={'ratio': 'land_score'})
    return out


def centroid_score(path, score_name):
    df = read_geojson(path)
    df_best = (df.sort_values(['id', 'score'], ascending=[True, False])
               .drop_duplicates('id', keep='first'))
    df_best = df_best[['id', 'score']]
    df_best = df_best.rename(columns={'score': f'{score_name}_score'})
    return df_best


def zonal_score(path, score_name):
    df = read_geojson(path)
    df = df[['id', '_mean']]
    df['_mean'] = pd.to_numeric(df['_mean'], errors='coerce').fillna(0)
    df = df.rename(columns={'_mean': f'{score_name}_score'})
    return df


def fill_nulls_with_zero(df: pd.DataFrame, numeric_only: bool = False, inplace: bool = False):
    """
    Fill NaNs with 0 only in columns that contain NaNs.
    If numeric_only=True, only consider numeric columns.
    Returns (df_filled, cols_filled) when inplace=False; otherwise returns cols_filled.
    """
    work = df if inplace else df.copy()

    cols = work.columns
    if numeric_only:
        cols = work.select_dtypes(include='number').columns

    cols_with_na = cols[work[cols].isna().any()]

    if len(cols_with_na) > 0:
        work[cols_with_na] = work[cols_with_na].fillna(0)

    return (work, list(cols_with_na)) if not inplace else list(cols_with_na)


def convert_geojson(gdf, out_path):
    if gdf.crs is None or gdf.crs.to_string().upper() != "EPSG:4326":
        gdf = gdf.to_crs(4326)
    gdf.to_file(out_path, driver="GeoJSON")  # writes a GeoJSON file


def run_pipeline(args):
    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    ## ouput_path
    final_score_geojson = output_path / "final_score_geojson.geojson"
    final_score_csv = output_path / "final_score_csv.csv"

    ## input path centroid score
    centroid_score_box2dso = input_path / "centroid_score_box2dso.geojson"
    centroid_score_box2plant = input_path / "centroid_score_box2plant.geojson"
    centroid_score_box2railway = input_path / "centroid_score_box2railway.geojson"
    centroid_score_box2road = input_path / "centroid_score_box2road.geojson"

    ## input path - zonal
    dni_zonal_path = input_path / "dni_zonal.geojson"
    pvout_zonal_path = input_path / "pvout_zonal.geojson"
    temp_zonal_path = input_path / "temp_zonal.geojson"
    dem_zonal_path = input_path / "dem_zonal.geojson"

    ## input path land ratio and box path
    land_ratio_path = input_path / "land_ratio.geojson"
    box_path = input_path / "box.geojson"

    print('reading box path')
    box_score = read_geojson(box_path)

    print('reading land ratio path')
    land_score = landuse_score(land_ratio_path)

    print('reading centroid score path')
    box2dso_score = centroid_score(centroid_score_box2dso, 'dso')
    box2pv_score = centroid_score(centroid_score_box2plant, 'pv')
    box2railway_score = centroid_score(centroid_score_box2railway, 'railway')
    box2road_score = centroid_score(centroid_score_box2road, 'road')

    print('reading zonal score path')
    dem_score = zonal_score(dem_zonal_path, 'dem')
    dni_score = zonal_score(dni_zonal_path, 'dni')
    temp_score = zonal_score(temp_zonal_path, 'temp')
    pvout_score = zonal_score(pvout_zonal_path, 'pvout')

    print('combining all scores data')
    dfs = [land_score, dem_score, dni_score, temp_score, pvout_score, box2dso_score, box2pv_score, box2railway_score,
           box2road_score]
    out = reduce(lambda l, r: l.merge(r, on='id', how='left'), [box_score] + dfs)
    final_result, changed = fill_nulls_with_zero(out)

    print('save the final score into geojson')
    convert_geojson(final_result, final_score_geojson)

    print('save the final score into csv')
    final_result.to_csv(final_score_csv)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Run PV analysis pipeline. Provide input/output folders, spacing, operator, and steps to run."
    )

    parser.add_argument("--input-path", type=str, default="../../data/input",
                        help="Folder that contains input rasters / vectors (default: ../../data/input)")
    parser.add_argument("--output-path", type=str, default="../../data/output",
                        help="Output folder (default: ../../data/output)")

    args = parser.parse_args()
    run_pipeline(args)