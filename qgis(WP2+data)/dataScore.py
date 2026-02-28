import os
import sys
import pandas as pd
import geopandas as gpd
import argparse
from pathlib import Path
import tempfile
import fiona
from functools import reduce
import numpy as np
from pymcdm.methods import TOPSIS

# from backend.notebook.src.runner import df_box

# Point Shapely to GEOS inside the QGIS app bundle (you found this path)
os.environ["SHAPELY_LIBRARY_PATH"] = "/Applications/QGIS-LTR.app/Contents/MacOS/lib/libgeos_c.dylib"
# Point PROJ and GDAL data to QGIS bundle
os.environ["PROJ_LIB"] = "/Applications/QGIS-LTR.app/Contents/Resources/proj"
os.environ["GDAL_DATA"] = "/Applications/QGIS-LTR.app/Contents/Resources/gdal"
# Help macOS dynamic loader find QGIS libraries
os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/Applications/QGIS-LTR.app/Contents/MacOS/lib:" + os.environ.get(
    "DYLD_FALLBACK_LIBRARY_PATH", "")
# Add QGIS Python paths (keep these before importing QGIS/geopandas)
PYTHON_PATH = "/Applications/QGIS-LTR.app/Contents/Resources/python"
PLUGIN_PATH = "/Applications/QGIS-LTR.app/Contents/Resources/python/plugins"
SITE_PACKAGES = "/Applications/QGIS-LTR.app/Contents/MacOS/lib/python3.9/site-packages"
sys.path[:0] = [PYTHON_PATH, PLUGIN_PATH, SITE_PACKAGES]  # prepend to avoid accidental shadowing
# --------------------------------------------------------------------------------
# --- QGIS paths (macOS QGIS-LTR) ---
QGIS_PATH = "/Applications/QGIS-LTR.app/Contents/MacOS"
PYTHON_PATH = "/Applications/QGIS-LTR.app/Contents/Resources/python"
PLUGIN_PATH = "/Applications/QGIS-LTR.app/Contents/Resources/python/plugins"
SITE_PACKAGES = "/Applications/QGIS-LTR.app/Contents/MacOS/lib/python3.9/site-packages"
# Add QGIS Python paths
sys.path.extend([PYTHON_PATH, PLUGIN_PATH, SITE_PACKAGES])

# # Environment variables
# os.environ["QGIS_PREFIX_PATH"] = QGIS_PATH
# os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Applications/QGIS-LTR.app/Contents/PlugIns/platforms"
# os.environ["GDAL_DATA"] = "/Applications/QGIS-LTR.app/Contents/Resources/gdal"
# os.environ["PROJ_LIB"] = "/Applications/QGIS-LTR.app/Contents/Resources/proj"

# --- Import QGIS ---
from qgis.core import (
    QgsApplication, QgsVectorLayer, Qgis,
    QgsProcessing, QgsProcessingAlgorithm, QgsProcessingMultiStepFeedback,
    QgsProcessingParameterVectorLayer, QgsProcessingParameterFeatureSink,
    QgsProcessingParameterCrs, QgsProcessingParameterNumber,
    QgsProcessingContext, QgsProcessingFeedback,
    QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsProject,
    QgsProcessingParameterRasterLayer,QgsProcessingParameterString,QgsExpression,
    QgsProcessingParameterRasterDestination, QgsProcessingParameterRasterLayer)

# Initialize QGIS (headless)
QgsApplication.setPrefixPath(QGIS_PATH, True)
qgs = QgsApplication([], False)
qgs.initQgis()
print("QGIS version:", Qgis.QGIS_VERSION)

# Initialize processing framework
import processing
from processing.core.Processing import Processing
import json

Processing.initialize()
print("Processing framework OK")
import geopandas as gpd
from shapely.geometry import shape
from utils.PV_BoxCentroidScore import runner_PV_Box2Dso, runner_PV_Box2Plant , runner_PV_Box2Railway, runner_PV_Box2Road
from utils.mcdm_score import mcdm_score_calculation


### ============================== EXTRACT THE SCORE ============================== ###

### Step: Create Grid Box of Fix geometries

class Pv_creategrid(QgsProcessingAlgorithm):
    P_input_vector_layer = "input_vector_layer"
    P_create_grid_result = "CreategridResult"
    P_input_crs = 'input_crs'
    P_hspace = 'input_horizontal_spacing'
    P_vspace = 'input_vertical_spacing'
    P_region_name = 'region_name'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterCrs(self.P_input_crs, 'input crs', defaultValue='EPSG:4326'))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_input_vector_layer, 'input vector layer',
                                                            types=[QgsProcessing.TypeVectorAnyGeometry],
                                                            defaultValue=None))
        self.addParameter(QgsProcessingParameterNumber(self.P_vspace, 'input vertical spacing',
                                                       type=QgsProcessingParameterNumber.Double, defaultValue=None))
        self.addParameter(QgsProcessingParameterNumber(self.P_hspace , 'input horizontal spacing',
                                                       type=QgsProcessingParameterNumber.Double, defaultValue=None))
        self.addParameter(
            QgsProcessingParameterFeatureSink(self.P_create_grid_result, 'CreateGrid Result', type=QgsProcessing.TypeVectorAnyGeometry,
                                              createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterString(self.P_region_name, 'region_name', multiLine=False, defaultValue=''))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(7, model_feedback)
        results = {}
        outputs = {}

        # Create grid
        alg_params = {
            'CRS': parameters[self.P_input_crs],
            'EXTENT': parameters[self.P_input_vector_layer],
            'HOVERLAY': 0,
            'HSPACING': parameters[self.P_hspace ],
            'TYPE': 2,  # Rectangle (Polygon)
            'VOVERLAY': 0,
            'VSPACING': parameters[self.P_vspace],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['CreateGrid'] = processing.run('native:creategrid', alg_params, context=context, feedback=feedback,
                                               is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Create spatial index
        alg_params = {
            'INPUT': outputs['CreateGrid']['OUTPUT']
        }
        outputs['CreateSpatialIndex'] = processing.run('native:createspatialindex', alg_params, context=context,
                                                       feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Clip
        alg_params = {
            'INPUT': outputs['CreateSpatialIndex']['OUTPUT'],
            'OVERLAY': parameters[self.P_input_vector_layer],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Clip'] = processing.run('native:clip', alg_params, context=context, feedback=feedback,
                                         is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Add geometry attributes
        alg_params = {
            'CALC_METHOD': 0,  # Layer CRS
            'INPUT': outputs['Clip']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['AddGeometryAttributes'] = processing.run('qgis:exportaddgeometrycolumns', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Rename field
        alg_params = {
            'FIELD': 'id',
            'INPUT': outputs['AddGeometryAttributes']['OUTPUT'],
            'NEW_NAME': 'box_id',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['RenameField'] = processing.run('native:renametablefield', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Drop field(s)
        alg_params = {
            'COLUMN': ['left','top','right','bottom','row_index','col_index'],
            'INPUT': outputs['RenameField']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT 
        }
        outputs['DropFields'] = processing.run('native:deletecolumn', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        
        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}
        
        region_val = parameters[self.P_region_name]
         # Field calculator
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'region_name',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2,  # Text (string)
            'FORMULA': f"'{region_val}'", 
            'INPUT': outputs['DropFields']['OUTPUT'],
            'OUTPUT': parameters[self.P_create_grid_result ]
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results[self.P_create_grid_result ] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self):return 'PV_CreateGrid'
    def displayName(self):return 'PV_CreateGrid'
    def group(self): return ''
    def groupId(self): return ''
    def createInstance(self): return Pv_creategrid()

def runner_PvCreateGrid(input_path, create_grid_result_path, h_space: float, v_space: float,region_name, crs: str = "EPSG:2180"):

    # Build parameter dict for the algorithm
    params = {
        Pv_creategrid.P_input_vector_layer: input_path,
        Pv_creategrid.P_create_grid_result:  create_grid_result_path,
        Pv_creategrid.P_hspace: h_space,
        Pv_creategrid.P_vspace: v_space,
        Pv_creategrid.P_input_crs: QgsCoordinateReferenceSystem(crs),
        Pv_creategrid.P_region_name: region_name}

    # Create a processing context & feedback
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    context.setProject(QgsProject.instance())

    # Run the algorithm class directly
    alg = Pv_creategrid()
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)
    print(f"Success: Saved to {create_grid_result_path}")
    
### Step: Create centroid 

class Pv_createcentroid(QgsProcessingAlgorithm):
    P_input_vector_layer  = "input_vector_layer"
    P_centroid_result = "CentroidResult"
    P_input_crs = 'input_crs'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_input_vector_layer, 'input vector layer',
                                                            types=[QgsProcessing.TypeVectorAnyGeometry],
                                                            defaultValue=None))
        self.addParameter(QgsProcessingParameterCrs(self.P_input_crs, 'input crs', defaultValue='EPSG:4326'))
        self.addParameter(
            QgsProcessingParameterFeatureSink(self.P_centroid_result, 'Centroid Result', type=QgsProcessing.TypeVectorAnyGeometry,
                                              createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(4, model_feedback)
        results = {}
        outputs = {}

        # Centroids
        alg_params = {
            'ALL_PARTS': True,
            'INPUT': parameters[self.P_input_vector_layer],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT }
        outputs['Centroids'] = processing.run('native:centroids', alg_params, context=context, feedback=feedback,
                                              is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Reproject layer
        alg_params = {
            'CONVERT_CURVED_GEOMETRIES': False,
            'INPUT': outputs['Centroids']['OUTPUT'],
            'OPERATION': '',
            'TARGET_CRS': parameters[self.P_input_crs],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ReprojectLayer'] = processing.run('native:reprojectlayer', alg_params, context=context,
                                                   feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Add X/Y fields to layer
        alg_params = {
            'CRS': QgsCoordinateReferenceSystem('EPSG:4326'),
            'INPUT': outputs['ReprojectLayer']['OUTPUT'],
            'PREFIX': '',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['AddXyFieldsToLayer'] = processing.run('native:addxyfields', alg_params, context=context,
                                                       feedback=feedback, is_child_algorithm=True)
        
        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}
        
        # Delete duplicates by attribute
        alg_params = {
            'FIELDS': ['box_id'],
            'INPUT': outputs['AddXyFieldsToLayer']['OUTPUT'],
            'OUTPUT': parameters[self.P_centroid_result]
        }
        outputs['DeleteDuplicatesByAttribute'] = processing.run('native:removeduplicatesbyattribute', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        
        results[self.P_centroid_result] = outputs['DeleteDuplicatesByAttribute']['OUTPUT']
        return results

    def name(self): return 'PV_CreateCentroid'
    def displayName(self): return 'PV_CreateCentroid'
    def group(self): return ''
    def groupId(self): return ''
    def createInstance(self): return Pv_createcentroid()
    
def runner_PvCreateCentroid(input_path,centroid_result, crs: str = "EPSG:4326"):
    # Build parameter dict for the algorithm
    params = {
        Pv_createcentroid.P_input_vector_layer: input_path,
        Pv_createcentroid.P_input_crs: QgsCoordinateReferenceSystem(crs),
        Pv_createcentroid.P_centroid_result: centroid_result,
    }

    # Create a processing context & feedback
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    context.setProject(QgsProject.instance())

    alg = Pv_createcentroid()
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)

    print(f"Created Centroid is Completed {centroid_result}")   
    

## Step: zonal statistic
class Pv_zonalstatistic(QgsProcessingAlgorithm):
    P_input_vector_layer = "input_vector_layer"
    P_input_raster = "input_raster_layer"
    P_OUT = 'ZonalStatisticResult'

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterRasterLayer(self.P_input_raster, 'input raster layer', defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_input_vector_layer, 'input vector layer',
                                                            types=[QgsProcessing.TypeVectorAnyGeometry],
                                                            defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink(self.P_OUT, 'Zonal statistic result',
                                                            type=QgsProcessing.TypeVectorAnyGeometry,
                                                            createByDefault=True, supportsAppend=True,
                                                            defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(2, model_feedback)
        results = {}
        outputs = {}

        # Clip raster by mask layer
        alg_params = {
            'ALPHA_BAND': False,
            'CROP_TO_CUTLINE': True,
            'DATA_TYPE': 0,  # Use Input Layer Data Type
            'EXTRA': '',
            'INPUT': parameters[self.P_input_raster],
            'KEEP_RESOLUTION': False,
            'MASK': parameters[self.P_input_vector_layer ],
            'MULTITHREADING': False,
            'NODATA': None,
            'OPTIONS': '',
            'SET_RESOLUTION': False,
            'SOURCE_CRS': None,
            'TARGET_CRS': None,
            'TARGET_EXTENT': None,
            'X_RESOLUTION': None,
            'Y_RESOLUTION': None,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ClipRasterByMaskLayer'] = processing.run('gdal:cliprasterbymasklayer', alg_params, context=context,
                                                          feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Zonal statistics
        alg_params = {
            'COLUMN_PREFIX': '_',
            'INPUT': parameters[self.P_input_vector_layer ],
            'INPUT_RASTER': outputs['ClipRasterByMaskLayer']['OUTPUT'],
            'RASTER_BAND': 1,
            'STATISTICS': [0, 1, 2],  # Count,Sum,Mean
            'OUTPUT': parameters[self.P_OUT]
        }
        outputs['ZonalStatistics'] = processing.run('native:zonalstatisticsfb', alg_params, context=context,
                                                    feedback=feedback, is_child_algorithm=True)
        results[self.P_OUT] = outputs['ZonalStatistics']['OUTPUT']
        return results

    def name(self): return 'PV_ZonalStatistic'
    def displayName(self): return 'PV_ZonalStatistic'
    def group(self): return ''
    def groupId(self): return ''
    def createInstance(self): return Pv_zonalstatistic()

def runner_PvZonalStatistic(vector_path,raster_path,output_path):
    # Example inputs
    # Build parameter dict for the algorithm
    params = {
        Pv_zonalstatistic.P_input_vector_layer:vector_path,
        Pv_zonalstatistic.P_input_raster : raster_path,
        Pv_zonalstatistic.P_OUT: output_path,
    }

    # Create a processing context & feedback
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    context.setProject(QgsProject.instance())

    # Run the algorithm class directly
    alg = Pv_zonalstatistic()
    # Normally the framework calls initAlgorithm; when running directly it's safe to call it once:
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)
    
    print(f"calculated zonal statistic Done -> {output_path}")

## Step: Landuse ratio

class Pv_landuseratio(QgsProcessingAlgorithm):
    P_input_box_grid = "input_box_grid"
    P_input_land_layer = "input_land_layer"
    P_OUT = 'LandUseScore'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_input_box_grid, 'input box grid',
                                                            types=[QgsProcessing.TypeVectorAnyGeometry],
                                                            defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_input_land_layer, 'input land layer',
                                                            types=[QgsProcessing.TypeVectorAnyGeometry],
                                                            defaultValue=None))
        self.addParameter(
            QgsProcessingParameterFeatureSink(self.P_OUT, 'land use score', type=QgsProcessing.TypeVectorAnyGeometry,
                                              createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(3, model_feedback)
        results = {}
        outputs = {}

        # Intersection
        alg_params = {
            'GRID_SIZE': None,
            'INPUT': parameters[self.P_input_box_grid],
            'INPUT_FIELDS': [''],
            'OVERLAY': parameters[self.P_input_land_layer],
            'OVERLAY_FIELDS': [''],
            'OVERLAY_FIELDS_PREFIX': '',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Intersection'] = processing.run('native:intersection', alg_params, context=context, feedback=feedback,
                                                 is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Add geometry attributes
        alg_params = {
            'CALC_METHOD': 0,  # Layer CRS
            'INPUT': outputs['Intersection']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['AddGeometryAttributes'] = processing.run('qgis:exportaddgeometrycolumns', alg_params, context=context,
                                                          feedback=feedback, is_child_algorithm=True)
        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Field calculator
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'ratio',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 0,  # Decimal (double)
            'FORMULA': ' "area_2" / "area" ',
            'INPUT': outputs['AddGeometryAttributes']['OUTPUT'],
            'OUTPUT': parameters[self.P_OUT]
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context,
                                                    feedback=feedback, is_child_algorithm=True)
        results[self.P_OUT] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self): return 'PV_LandUseRatio'
    def displayName(self): return 'PV_LandUseRatio'
    def group(self): return ''
    def groupId(self): return ''
    def createInstance(self): return Pv_landuseratio()


def runner_PvLandUseRatio(input_vector,input_land_vector,output_path):
    
    # Build parameter dict for the algorithm
    params = {
        Pv_landuseratio.P_input_box_grid: input_vector,
        Pv_landuseratio.P_input_land_layer: input_land_vector,
        Pv_landuseratio.P_OUT: output_path,
    }

    # Create a processing context & feedback
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    context.setProject(QgsProject.instance())

    # Run the algorithm class directly
    alg = Pv_landuseratio()
    # Normally the framework calls initAlgorithm; when running directly it's safe to call it once:
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)

    print(f"calculated land ratio Done -> {output_path}")

## ============================ Final score

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

### ======================== MCDM Score

def runnner_mcdm_score(input_path,output_path):
    mcdm_score_gdf = mcdm_score_calculation(input_path)
    mcdm_score_gdf.to_file(output_path, driver='GeoJSON')
    print(f"Successfully saved MCDM score results to {output_path}")
    

# def mcdm_score(input_path,output_path):
#     # 1. LOAD GEOJSON DATA
#     gdf = gpd.read_file(input_path)

#     # 2. PREPROCESSING
#     # Clean up columns not needed for the math
#     cols_to_drop = ['perimeter', 'region_name', 'area', 'fclass']
#     gdf_reduced = gdf.drop(columns=cols_to_drop, errors='ignore')

#     # 3. CONSTRUCT THE DECISION MATRIX
#     # Ensure criteria_cols matches the data in your specific GeoJSON
#     criteria_cols = [
#         'dni_score', 'temp_score', 'pvout_score', 'dem_score', 
#         'road_score', 'station_score', 'solar_score', 'dso_score', 'land_score'
#     ]

#     # Drop rows with missing values in these specific columns
#     gdf_clean = gdf_reduced.dropna(subset=criteria_cols).copy()
#     matrix = gdf_clean[criteria_cols].values

#     # 4. DEFINE WEIGHTS & TYPES (Updated to 9 elements)
#     # We must have exactly 9 weights to match the 9 criteria above
#     weights = np.array([1/9] * 9) 

#     # Types: 1 for Benefit (Higher is better), -1 for Cost (Lower is better)
#     # Mapping based on typical solar MCDM logic:
#     # dni(1), temp(-1), pvout(1), dem(-1), road(1), station(1), solar(1), dso(1), land(1)
#     types = np.array([1, -1, 1, -1, 1, 1, 1, 1, 1]) 

#     # 5. RUN THE MCDM MODEL (TOPSIS)
#     topsis = TOPSIS()
#     pref = topsis(matrix, weights, types)

#     # Attach results
#     gdf_clean['rank_score'] = pref
#     gdf_clean['rank'] = gdf_clean['rank_score'].rank(ascending=False)

#     # 6. SPATIAL VISUALIZATION (Adjusted for Wrocław)
#     top_sites = gdf_clean.nsmallest(50, 'rank')
#     top_sites.to_file(output_path, driver='GeoJSON')

### Run the PIPELINE ###


def run_pipeline(args):
    # 1. Initialize Paths
    input_path = Path(args.input_path)
    extraction_path = input_path
    region = args.region_name
    h_space = args.h_space
    v_space = args.v_space
    
    # 2. input paths
    fixgeometries_path = input_path/ 'extraction' /region /  f'fixGeometries_{region}.geojson'
    centroid_dso_path = extraction_path / 'extraction' /region /  f'centroid_dso_{region}.geojson'
    centroid_solar_path =extraction_path / 'extraction' /region /  f'centroid_solar_{region}.geojson'
    centroid_station_path = extraction_path / 'extraction' /region / f'railwayStation_filter_{region}.geojson'
    centroid_road_path = extraction_path / 'extraction' /region / f'roadVertices_filter_{region}.geojson'
    dni_path = extraction_path / 'extraction' /region / f'dni_clip_{region}.tif'
    pvout_path = extraction_path / 'extraction' /region / f'pvout_clip_{region}.tif'
    temp_path = extraction_path / 'extraction' /region / f'temp_clip_{region}.tif'
    dem_path = extraction_path / 'extraction' /region / f'dem_clip_{region}.tif'
    landuse_path = extraction_path / 'extraction' /region /  f'landUse_filter_{region}.geojson'
    
    
    # 3. output paths
    grid_box_out = extraction_path / 'score'/ region / f'grid_box_{region}.geojson'
    centroid_box_out = extraction_path / 'score'/ region / f'centroid_box_{region}.geojson'
    score_box2dso_out = extraction_path / 'score'/ region / f'score_box2dso_{region}.geojson'
    score_box2solar_out = extraction_path / 'score'/ region / f'score_box2solar_{region}.geojson'
    score_box2station_out = extraction_path / 'score'/ region / f'score_box2station_{region}.geojson'
    score_box2road_out = extraction_path / 'score'/ region / f'score_box2road_{region}.geojson'
    score_dni_out = extraction_path / 'score'/ region / f'score_dni_{region}.geojson'
    score_pvout_out = extraction_path / 'score'/ region / f'score_pvout_{region}.geojson' 
    score_temp_out = extraction_path / 'score'/ region / f'score_temp_{region}.geojson' 
    score_dem_out = extraction_path / 'score'/ region / f'score_dem_{region}.geojson'
    land_ratio_out = extraction_path / 'score'/ region / f'score_landRatio_{region}.geojson'
    final_score_out = extraction_path / 'score'/ region / f'final_score_{region}.geojson'
    mcdm_score_out = extraction_path / 'score'/ region / f'mcdm_score_{region}.geojson'
    
  
   # allow choosing steps (0..etc) or 'all'
    steps_to_run = set()
    if args.steps:
        for s in args.steps:
            if s == "all":
                steps_to_run = set(map(str, range(0, 13)))
                break
            steps_to_run.add(str(s))
    else:
        steps_to_run = set(map(str, range(0, 13)))  # default: run all steps

    def should_run(output_path: Path, step_id: str, input_file: Path):
        if step_id not in steps_to_run: 
            return False
        if not input_file.exists():
            print(f"Error: Input file for Step {step_id} missing at {input_file}")
            return False
        return args.force or not output_path.exists()
    
    
    ## 1) Create box
    if should_run(grid_box_out, "0",fixgeometries_path):
        grid_box_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 0: Creating box grid → {grid_box_out}")
        runner_PvCreateGrid(str(fixgeometries_path), str(grid_box_out), h_space, v_space, region_name=region)
    ## 2) Create centroid-box
        centroid_box_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 1: Creating centroid box → {centroid_box_out} ")
        runner_PvCreateCentroid(str(grid_box_out), str(centroid_box_out))
        
    ## 3) Calculate distance centroid box-dso
    if should_run(score_box2dso_out , "1",centroid_dso_path):
        score_box2dso_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 2: Calculate score box2dso → {score_box2dso_out}")
        runner_PV_Box2Dso(str(centroid_box_out), str(centroid_dso_path), str(score_box2dso_out))
        
     ## 4) calculate distance centroid box-solar
    if should_run(score_box2solar_out , "2",centroid_solar_path):
        score_box2solar_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 3: Calculatescore box2solar → {score_box2solar_out}")
        runner_PV_Box2Plant(str(centroid_box_out), str(centroid_solar_path), str(score_box2solar_out))
     
    ## 5) calculate distance centroid box-station 
    if should_run(score_box2station_out , "3",centroid_station_path):
        score_box2station_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 4: Calculate score box2station → {score_box2station_out}")
        runner_PV_Box2Railway(str(centroid_box_out), str(centroid_station_path), str(score_box2station_out))

    ## 6) calculate distance centroid box-road vertices
    if should_run(score_box2road_out, "4",centroid_road_path):
        score_box2road_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 5: Calculate score box2road → {score_box2road_out}")
        runner_PV_Box2Road(str(centroid_box_out), str(centroid_road_path), str(score_box2road_out))
    
    ## 7) calculate zonal DNI
    if should_run(score_dni_out, "5",dni_path):
        score_dni_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 6: Calculate score dni → {score_dni_out}")
        runner_PvZonalStatistic(str(grid_box_out), str(dni_path), str(score_dni_out))
    
    ## 8) calculate zonal PVOUT
    if should_run(score_pvout_out, "6",pvout_path):
        score_pvout_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 7: Calculate score pvout → {score_pvout_out}")
        runner_PvZonalStatistic(str(grid_box_out), str(pvout_path), str(score_pvout_out))
    
      
    ## 9) calculate zonal TEMP
    if should_run(score_temp_out, "7",temp_path):
        score_temp_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 8: Calculate score temp → {score_temp_out}")
        runner_PvZonalStatistic(str(grid_box_out), str(temp_path), str(score_temp_out))
    
    ## 10) calculate zonal DEM
    if should_run(score_dem_out, "8",dem_path):
        score_dem_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 9: Calculate score dem → {score_dem_out}")
        runner_PvZonalStatistic(str(grid_box_out), str(dem_path), str(score_dem_out))
    
    ## 11) Calculate land ratio 
    if should_run(land_ratio_out, "9",landuse_path):
        land_ratio_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 10: Calcualte Land ratio → {land_ratio_out}")
        runner_PvLandUseRatio(str(grid_box_out), str(landuse_path), str(land_ratio_out))
    
    ## 12) Calculate the final score
    if should_run(final_score_out, "10",extraction_path):
        final_score_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 11: Creating final score for MCDM → {final_score_out}")
        final_score(str(extraction_path), str(final_score_out), region)
    
    ## 12) calcualting mcdm score
    if should_run(mcdm_score_out, "11",final_score_out):
        mcdm_score_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 11: Calculate score for MCDM → {mcdm_score_out}")
        runnner_mcdm_score(str(final_score_out), str(mcdm_score_out))
     
    
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Extraction Pipeline")
    parser.add_argument("--steps", nargs="+", help='Steps to run (e.g., 0 1 or "all")')
    parser.add_argument("--input-path", type=str, required=True, help="Root input directory")
    parser.add_argument("--region-name", type=str, required=True, help="Name of the region (e.g., dolnoslaskie)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing output files")
    parser.add_argument("--h-space", type=float, default=1000.0, help="Horizontal spacing for grid (default: 250.0)")
    parser.add_argument("--v-space", type=float, default=1000.0, help="Vertical spacing for grid (default: 250.0)")
    #parser.add_argument("--extraction-path", type=str, required=True, help="Root output directory")
    
    regions_list = [
        'wroclaw','dolnoslaskie'
    ]
    

    for region in regions_list:
        print(f'========================== {region} ================================')
        # We wrap the variable in literal single quotes
        # The double quotes " " tell Python: "Everything inside here is a string"
        # The single quotes ' ' inside tell QGIS: "This is a value, not a column name"
       

        simulated_args = parser.parse_args([
            "--region-name", region, 
            "--input-path", "/Users/sell/SynologyDrive/Dataset/daina",
            "--steps", "all",
            
        ])
        run_pipeline(simulated_args)
    
    # args = parser.parse_args()
    # run_pipeline(args)
    


    
# python dataScore.py \
#     --region-name dolnoslaskie \
#     --input-path "/Users/sell/SynologyDrive/Dataset/daina" \
#     --steps 0

