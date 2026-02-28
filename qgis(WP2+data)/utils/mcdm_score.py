import geopandas as gpd
import pandas as pd
import numpy as np
from pymcdm.methods import TOPSIS

def mcdm_score_calculation(input_path):
    # 1. LOAD GEOJSON DATA
    gdf = gpd.read_file(input_path)
    
    # 2. Define Criteria
    criteria = [
        'dni_score', 'temp_score', 'pvout_score', 'dem_score', 
        'road_score', 'station_score', 'solar_score', 'dso_score', 'land_score'
    ]
    
    # +1 for benefit, -1 for cost
    types = np.array([+1, +1, +1, -1, +1, +1, -1, +1, +1]) 
    
    # 3. Processing (Fixing the inplace=True issue)
    # Create a copy for calculation to avoid modifying the original 'gdf' unexpectedly
    gdf_reduced = gdf.copy().set_index('box_id')
    gdf_reduced = gdf_reduced[criteria].dropna(subset=criteria)
    
    # Columns already scaled to [0,1]
    already_scaled = {'land_score', 'dso_score', 'road_score', 'station_score', 'solar_score'}

    # 4. Build normalized matrix Xn
    X = gdf_reduced[criteria].to_numpy(float)
    Xn = np.empty_like(X, float)

    for j, colname in enumerate(criteria):
        col = X[:, j]
        if colname in already_scaled:
            # Invert only if it is a cost criterion (-1)
            Xn[:, j] = 1 - col if types[j] == -1 else col
        else:
            cmin, cmax = np.nanmin(col), np.nanmax(col)
            if np.isclose(cmax, cmin):
                Xn[:, j] = 0.0
            else:
                # Min-max with cost handling
                Xn[:, j] = (col - cmin) / (cmax - cmin) if types[j] == +1 else (cmax - col) / (cmax - cmin)

    # 5. CRITIC weights calculation
    # Add tiny noise to prevent correlation errors with constant columns
    sigma = np.nanstd(Xn, axis=0, ddof=1)
    R = np.corrcoef(Xn + 1e-12 * np.random.randn(*Xn.shape), rowvar=False)
    R = np.clip(R, -1.0, 1.0)
    C = sigma * np.sum(1.0 - np.abs(R), axis=1)

    # Normalize weights
    w = np.ones_like(C)/len(C) if np.allclose(C.sum(), 0.0) else C / C.sum()
    
    # 6. TOPSIS Calculation
    # Since Xn already has costs inverted (higher is better), pass all +1 to TOPSIS
    types_for_methods = np.ones(len(criteria), dtype=int)
    
    topsis = TOPSIS()
    topsis_scores = topsis(Xn, w, types=types_for_methods)
    
    # Ranks: 1 = highest score (best)
    topsis_ranks = (-topsis_scores).argsort().argsort() + 1

    # 7. Collect results into a temporary DataFrame
    res_topsis = pd.DataFrame({
        "box_id": gdf_reduced.index,
        "topsis_score": topsis_scores,
        "topsis_rank": topsis_ranks
    })

    # 8. THE MERGE: Join the results back to the original GeoDataFrame
    # We use 'left' join so we don't lose boxes that might have had NaNs
    final_gdf = gdf.merge(res_topsis, on='box_id', how='left')

 
    
    return final_gdf