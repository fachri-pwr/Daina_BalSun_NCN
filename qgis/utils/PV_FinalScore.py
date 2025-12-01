import pandas as pd
from pathlib import Path
import argparse
import json


def read_csv_safe(path: Path, id_col='id'):
    """Read CSV file safely, return empty DataFrame if file doesn't exist."""
    if not path.exists():
        print(f"        ⚠ Warning: File not found: {path}")
        return pd.DataFrame({id_col: []})
    try:
        df = pd.read_csv(path)
        print(f"        ✓ Loaded: {path.name} ({len(df)} rows)")
        return df
    except Exception as e:
        print(f"        ⚠ Error reading {path.name}: {e}")
        return pd.DataFrame({id_col: []})


def landuse_score(df, id_col='id'):
    """Extract land use score from land ratio DataFrame."""
    if df.empty:
        return pd.DataFrame({id_col: [], 'land_score': []})

    # Filter for relevant land classes
    df = df[df['fclass'].isin(['meadow', 'grass', 'farmland', 'scrub', 'farmyard', 'heath'])]

    if df.empty:
        return pd.DataFrame({id_col: [], 'land_score': []})

    sum_cols = ['area_2', 'area', 'ratio']
    # Average per id
    sums = df.groupby(id_col, as_index=False)[sum_cols].mean()

    # Keep only id and ratio
    out = sums[[id_col, 'ratio']]
    out = out.rename(columns={'ratio': 'land_score'})
    return out


def centroid_score(df, score_name, id_col='id'):
    """Extract best centroid-based distance score per id."""
    if df.empty:
        return pd.DataFrame({id_col: [], f'{score_name}_score': [], f'{score_name}_distance_km': []})

    df_best = (df.sort_values([id_col, 'score'], ascending=[True, False])
               .drop_duplicates(id_col, keep='first'))
    df_best = df_best[[id_col, 'score','distance_km']]
    df_best = df_best.rename(columns={'score': f'{score_name}_score','distance_km': f'{score_name}_score_distance_km'})
    return df_best


def zonal_score(df, score_name, id_col='id'):
    """Extract zonal statistics score."""
    if df.empty:
        return pd.DataFrame({id_col: [], f'{score_name}_score': []})

    df = df[[id_col, '_mean']].copy()
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

def save_csv(df, out_path):
    """Save DataFrame as CSV."""
    df.to_csv(out_path, index=False)
    print(f"  ✓ Saved CSV: {out_path}")

def run_pipeline(args):
    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    ## Output path
    final_score_csv = output_path / "final_score.csv"

    ## Input paths - CSV files
    box_csv = input_path / "box.csv"
    land_ratio_csv = input_path / "land_ratio.csv"
    centroid_score_box2dso_csv = input_path / "centroid_score_box2dso.csv"
    centroid_score_box2plant_csv = input_path / "centroid_score_box2plant.csv"
    centroid_score_box2railway_csv = input_path / "centroid_score_box2railway.csv"
    centroid_score_box2road_csv = input_path / "centroid_score_box2road.csv"
    dni_zonal_csv = input_path / "dni_zonal.csv"
    pvout_zonal_csv = input_path / "pvout_zonal.csv"
    temp_zonal_csv = input_path / "temp_zonal.csv"
    dem_zonal_csv = input_path / "dem_zonal.csv"

    print("\n" + "=" * 60)
    print("FINAL SCORE CALCULATION PIPELINE (CSV)")
    print("=" * 60)

    print('\n[1/10] Reading box grid data...')
    box_df = read_csv_safe(box_csv)
    if box_df.empty:
        print("ERROR: Box CSV file is required!")
        return

    print('\n[2/10] Processing land use score...')
    land_ratio_df = read_csv_safe(land_ratio_csv)
    land_score = landuse_score(land_ratio_df)

    print('\n[3/10] Processing centroid distance scores...')
    box2dso_df = read_csv_safe(centroid_score_box2dso_csv)
    box2dso_score = centroid_score(box2dso_df, 'dso')

    box2pv_df = read_csv_safe(centroid_score_box2plant_csv)
    box2pv_score = centroid_score(box2pv_df, 'pv')

    box2railway_df = read_csv_safe(centroid_score_box2railway_csv)
    box2railway_score = centroid_score(box2railway_df, 'railway')

    box2road_df = read_csv_safe(centroid_score_box2road_csv)
    box2road_score = centroid_score(box2road_df, 'road')

    print('\n[4/10] Processing zonal statistics scores...')
    dem_df = read_csv_safe(dem_zonal_csv)
    dem_score = zonal_score(dem_df, 'dem')

    dni_df = read_csv_safe(dni_zonal_csv)
    dni_score = zonal_score(dni_df, 'dni')

    temp_df = read_csv_safe(temp_zonal_csv)
    temp_score = zonal_score(temp_df, 'temp')

    pvout_df = read_csv_safe(pvout_zonal_csv)
    pvout_score = zonal_score(pvout_df, 'pvout')

    print('\n[5/10] Merging all scores...')
    # Start with box dataframe
    final_result = box_df.copy()

    # Merge each score dataframe
    score_dfs = {
        'land_score': land_score,
        'dso_score': box2dso_score,
        'pv_score': box2pv_score,
        'railway_score': box2railway_score,
        'road_score': box2road_score,
        'dem_score': dem_score,
        'dni_score': dni_score,
        'temp_score': temp_score,
        'pvout_score': pvout_score
    }

    for name, score_df in score_dfs.items():
        if not score_df.empty:
            final_result = final_result.merge(score_df, on='id', how='left')

    print(f"        Merged {len(final_result)} records with {len(final_result.columns)} columns")

    print('\n[6/10] Filling missing values...')
    # Fill NaN values in score columns with 0
    score_columns = [col for col in final_result.columns if col.endswith('_score')]
    for col in score_columns:
        if col in final_result.columns:
            final_result[col] = final_result[col].fillna(0)
    print(f"        Filled NaN values in {len(score_columns)} score columns")

    # print('\n[7/10] Calculating composite score...')
    # if score_columns:
    #     # Calculate composite score as average of all score columns
    #     final_result['composite_score'] = final_result[score_columns].mean(axis=1)
    #     print(f"        Calculated composite score from {len(score_columns)} components")
    #     print(f"        Score columns: {', '.join(score_columns)}")
    # else:
    #     print(f"        ⚠ Warning: No score columns found")
    #
    # print('\n[8/10] Sorting by composite score (descending)...')
    # if 'composite_score' in final_result.columns:
    #     final_result = final_result.sort_values('composite_score', ascending=False)
    #     print(f"        Sorted {len(final_result)} records by composite_score")

    print('\n[9/10] Saving final CSV output...')
    save_csv(final_result, final_score_csv)

    # print('\n[10/10] Generating summary statistics...')
    # print("\n" + "-" * 60)
    # print("SUMMARY STATISTICS")
    # print("-" * 60)
    # print(f"Total grid cells: {len(final_result)}")
    # print(f"Total columns: {len(final_result.columns)}")
    #
    # if score_columns:
    #     print(f"\nAvailable Score Components:")
    #     for col in score_columns:
    #         mean_val = final_result[col].mean()
    #         print(f"  - {col}: mean = {mean_val:.4f}")
    #
    # if 'composite_score' in final_result.columns:
    #     print(f"\nComposite Score Statistics:")
    #     print(f"  Mean: {final_result['composite_score'].mean():.4f}")
    #     print(f"  Median: {final_result['composite_score'].median():.4f}")
    #     print(f"  Min: {final_result['composite_score'].min():.4f}")
    #     print(f"  Max: {final_result['composite_score'].max():.4f}")
    #     print(f"  Std Dev: {final_result['composite_score'].std():.4f}")
    #
    #     print(f"\nTop 5 Grid Cells by Composite Score:")
    #     top_5 = final_result.nlargest(5, 'composite_score')[['id', 'composite_score'] + score_columns]
    #     print(top_5.to_string(index=False))

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print(f"\nOutput file:")
    print(f"  - CSV: {final_score_csv}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="final_score.py",
        description="Calculate final scores from PV analysis pipeline outputs."
    )

    parser.add_argument("--input-path", type=str, default="../../data/output",
                        help="Folder containing pipeline output files (default: ../../data/output)")
    parser.add_argument("--output-path", type=str, default="../../data/final",
                        help="Output folder for final scores (default: ../../data/final)")

    args = parser.parse_args()
    run_pipeline(args)