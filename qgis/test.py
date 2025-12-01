import argparse
from pathlib import Path

# --- keep your existing function imports above ---
# from mymodule import (extract_data, gdf_to_qgs_geojson, runner_ModelClip,
#                       runner_PvCreateGrid, runner_PvCreateCentroid,
#                       runner_PV_Box2Dso, runner_PV_Box2Plant,
#                       runner_PvZonalStatistic, runner_PvLandUseRatio)

def run_pipeline(args):
    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    ### Input path
    boundary_path = input_path / "map_boundary.geojson"
    dni_raster_path = input_path / "DNI.tif"
    pvout_raster_path = input_path / "PVOUT.tif"
    temp_raster_path = input_path / "TEMP.tif"
    dem_raster_path = input_path / "DEM-Lower Silesian.tif"
    dso_path = input_path / "KSE_2019.kmz"
    land_use_path = input_path / "landUsed-Lower Silesian.gpkg"
    centroid_plant_path = input_path / "power_plant_dolnoslaskie.geojson"

    h_space = 250
    v_space = 250
    operator_name = "tauron"

    ### Extract path
    box_path = output_path / "box.geojson"
    land_ratio_path = output_path / "land_ratio.geojson"

    centroid_box_path = output_path / "centroid_box.geojson"
    centroid_dso_path = output_path / "centroid_dso.geojson"
    centroid_score_box2dso = output_path / "centroid_score_box2dso.geojson"
    centroid_score_box2plant = output_path / "centroid_score_box2plant.geojson"

    dni_zonal_path = output_path / "dni_zonal.geojson"
    pvout_zonal_path = output_path / "pvout_zonal.geojson"
    temp_zonal_path = output_path / "temp_zonal.geojson"
    dem_zonal_path = output_path / "dem_zonal.geojson"

    # allow choosing steps (0..8) or 'all'
    steps_to_run = set()
    if args.steps:
        for s in args.steps:
            if s == "all":
                steps_to_run = set(map(str, range(0, 9)))
                break
            steps_to_run.add(str(s))
    else:
        steps_to_run = set(map(str, range(0, 9)))  # default: run all steps

    # util to check existence + force flag
    def should_run(path: Path, step_id: str):
        if step_id not in steps_to_run:
            return False
        if args.force:
            return True
        return not path.exists()

    # --- 0) extract centroid dso
    if should_run(centroid_dso_path, "0"):
        print("Step 0: Extracting DSO centroid →", centroid_dso_path)
        dso_df = extract_data(str(dso_path), str(centroid_dso_path), operator_name)
        dso_vector = gdf_to_qgs_geojson(dso_df, 'dso_centroid')
        runner_ModelClip(dso_vector, str(boundary_path), str(centroid_dso_path))

    # 1) Create box
    if should_run(box_path, "1"):
        box_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 1: Creating box grid → {box_path}")
        runner_PvCreateGrid(str(boundary_path), str(box_path), h_space, v_space)

    # 2) Create centroid box
    if should_run(centroid_box_path, "2"):
        centroid_box_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 2: Creating centroid box → {centroid_box_path}")
        runner_PvCreateCentroid(str(box_path), str(centroid_box_path))

    # 3) Calculate distance centroid box-dso
    if should_run(centroid_score_box2dso, "3"):
        centroid_score_box2dso.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 3: Creating score centroid box-dso → {centroid_score_box2dso}")
        runner_PV_Box2Dso(str(centroid_box_path), str(centroid_dso_path), str(centroid_score_box2dso))

    # 4) calculate distance centroid box-plant
    if should_run(centroid_score_box2plant, "4"):
        centroid_score_box2plant.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 4: Creating score centroid box-plant → {centroid_score_box2plant}")
        runner_PV_Box2Plant(str(centroid_box_path), str(centroid_plant_path), 'solar', str(centroid_score_box2plant))

    # 5) Extracting DNI
    if should_run(dni_zonal_path, "5"):
        dni_zonal_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 5: Extracting DNI → {dni_zonal_path}")
        runner_PvZonalStatistic(str(box_path), str(dni_raster_path), str(dni_zonal_path))

    # 6) Extracting PVOUT
    if should_run(pvout_zonal_path, "6"):
        pvout_zonal_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 6: Extracting PVOUT → {pvout_zonal_path}")
        runner_PvZonalStatistic(str(box_path), str(pvout_raster_path), str(pvout_zonal_path))

    # 7) Extracting Temperature
    if should_run(temp_zonal_path, "7"):
        temp_zonal_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 7: Extracting TEMP → {temp_zonal_path}")
        runner_PvZonalStatistic(str(box_path), str(temp_raster_path), str(temp_zonal_path))

    # 8) Extracting DEM
    if should_run(dem_zonal_path, "8"):
        dem_zonal_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 8: Extracting DEM → {dem_zonal_path}")
        runner_PvZonalStatistic(str(box_path), str(dem_raster_path), str(dem_zonal_path))

    # 9) Calculate land ratio (kept as separate logical step)
    if should_run(land_ratio_path, "9"):
        land_ratio_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 9: Extracting Land ratio → {land_ratio_path}")
        runner_PvLandUseRatio(str(box_path), str(land_use_path), str(land_ratio_path))

    print("Done. The algorithm has finished.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="main_1.py",
        description="Run PV analysis pipeline. Provide input/output folders, spacing, operator, and steps to run."
    )

    parser.add_argument("--input-path", type=str, default="../../data/input",
                        help="Folder that contains input rasters / vectors (default: ../../data/input)")
    parser.add_argument("--output-path", type=str, default="../../data/output",
                        help="Output folder (default: ../../data/output)")
    parser.add_argument("--h-space", type=float, default=250.0, help="Horizontal spacing for grid (default: 250.0)")
    parser.add_argument("--v-space", type=float, default=250.0, help="Vertical spacing for grid (default: 250.0)")
    parser.add_argument("--operator", type=str, default="tauron",
                        help='Operator name when extracting DSO centroids (default: "tauron")')

    # steps: allow names/numbers; user can pass multiple e.g. --steps 1 5 6  or --steps all
    parser.add_argument("--steps", nargs="+", help='Steps to run, e.g. 0 1 2 or "all" (default: all)')

    parser.add_argument("--force", action="store_true",
                        help="Force running steps even if output files already exist (overwrites)")

    args = parser.parse_args()
    run_pipeline(args)
