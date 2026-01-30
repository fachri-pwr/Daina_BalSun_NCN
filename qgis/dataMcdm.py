import pandas as pd
import geopandas as gpd
from functools import reduce
from pathlib import Path
import argparse

def final_score(extraction_path, final_score_out, region):
    """
    Merges all spatial score layers for a specific region into one GeoJSON.
    """
    base_path = Path(extraction_path) / 'score' / region
    
    # 1. Initialize with main grid geometry
    grid_path = base_path / f'grid_box_{region}.geojson'
    if not grid_path.exists():
        raise FileNotFoundError(f"Base grid not found at {grid_path}")
        
    grid_box = gpd.read_file(grid_path)
    grid_box['box_id'] = grid_box['box_id'].astype(str) # Ensure string for merging
    processed_dfs = [grid_box]

    # 2. Configuration: {file_suffix: (old_column_name, new_column_name)}
    # Standard layers (box2...)
    standard_layers = {
        'box2dso':     ('score', 'dso_score'),
        'box2solar':   ('score', 'solar_score'),
        'box2station': ('score', 'station_score'),
        'box2road':    ('score', 'road_score'),
    }
    
    # Zonal layers (dni, pvout, etc.)
    zonal_layers = {
        'dni':   ('_mean', 'dni_score'),
        'pvout': ('_mean', 'pvout_score'),
        'temp':  ('_mean', 'temp_score'),
        'dem':   ('_mean', 'dem_score'),
    }

    # 3. Helper to process and append layers
    def load_and_append(layers_dict):
        for suffix, (old_col, new_col) in layers_dict.items():
            f_path = base_path / f'score_{suffix}_{region}.geojson'
            if f_path.exists():
                df = gpd.read_file(f_path)
                df['box_id'] = df['box_id'].astype(str)
                # Select only necessary columns
                df = df[['box_id', old_col]].rename(columns={old_col: new_col})
                processed_dfs.append(df)
            else:
                print(f"Warning: File missing -> {f_path.name}")

    load_and_append(standard_layers)
    load_and_append(zonal_layers)

    # 4. Handle Land Ratio (Requires aggregation)
    land_path = base_path / f'score_landRatio_{region}.geojson'
    if land_path.exists():
        land_df = gpd.read_file(land_path)
        land_df['box_id'] = land_df['box_id'].astype(str)
        land_agg = land_df.groupby('box_id', as_index=False).agg({
            'ratio': 'sum',
            'fclass': lambda x: x.value_counts().index[0]
        }).rename(columns={'ratio': 'land_score'})
        processed_dfs.append(land_agg)

    # 5. Execute Sequential Merge
    df_merged = reduce(lambda left, right: pd.merge(left, right, on='box_id', how='left'), processed_dfs)

    # 6. Final Column Ordering
    cols_order = [
        'box_id', 'dni_score', 'pvout_score', 'temp_score', 'dem_score',
        'dso_score', 'solar_score', 'station_score', 'road_score', 
        'land_score', 'fclass', 'area', 'perimeter', 'region_name', 'geometry'
    ]
    
    # Keep only columns that exist in the dataframe
    final_cols = [c for c in cols_order if c in df_merged.columns]
    final_df = df_merged[final_cols].copy()

    # 7. Save to GeoJSON
    final_df.to_file(final_score_out, driver='GeoJSON')
    print(f"Done! Final file saved: {final_score_out}")




def run_pipeline(args):
   # 1. Initialize Paths
    input_path = Path(args.input_path)
    extraction_path = input_path
    region = args.region_name
    
    # 2. output path 
    final_score_out = extraction_path / 'score' / region / f'final_score_{region}.geojson'
    
    print(f'================= creating final score for {region} =====================')
    final_score(extraction_path, final_score_out, region)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Extraction Pipeline")
    parser.add_argument("--input-path", type=str, required=True, help="Root input directory")
    parser.add_argument("--region-name", type=str, required=True, help="Name of the region (e.g., dolnoslaskie)")
    
    
    regions_list = [
        'wroclaw'
    ]
    

    for region in regions_list:
        print(f'========================== {region} ================================')
        simulated_args = parser.parse_args([
            "--region-name", region, 
            "--input-path", "/Users/sell/SynologyDrive/Dataset/daina",

            
        ])
        run_pipeline(simulated_args)
    
