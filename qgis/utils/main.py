import os
import sys
import pandas as pd
import geopandas as gpd
import argparse

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

from pathlib import Path
import tempfile

# Your modules
from PV_CentroidDso import extract_data
from PV_BoxCentroidScore import runner_PV_Box2Dso, runner_PV_Box2Plant , runner_PV_Box2Railway, runner_PV_Box2Road

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
    QgsProcessingParameterRasterLayer
)

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


### ================================== PV CREATE GRID ================================= ###

class Pv_creategrid(QgsProcessingAlgorithm):
    P_INPUT = "input_vector_layer"
    P_OUT = "CreategridResult"
    P_INPUT_CRS = 'input_crs'
    P_HSPACE = 'input_horizontal_spacing'
    P_VSPACE = 'input_vertical_spacing'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterCrs(self.P_INPUT_CRS, 'input crs', defaultValue='EPSG:4326'))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_INPUT, 'input vector layer',
                                                            types=[QgsProcessing.TypeVectorAnyGeometry],
                                                            defaultValue=None))
        self.addParameter(QgsProcessingParameterNumber(self.P_VSPACE, 'input vertical spacing',
                                                       type=QgsProcessingParameterNumber.Double, defaultValue=None))
        self.addParameter(QgsProcessingParameterNumber(self.P_HSPACE, 'input horizontal spacing',
                                                       type=QgsProcessingParameterNumber.Double, defaultValue=None))
        self.addParameter(
            QgsProcessingParameterFeatureSink(self.P_OUT, 'CreateGrid Result', type=QgsProcessing.TypeVectorAnyGeometry,
                                              createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(4, model_feedback)
        results = {}
        outputs = {}

        # Create grid
        alg_params = {
            'CRS': parameters['input_crs'],
            'EXTENT': parameters['input_vector_layer'],
            'HOVERLAY': 0,
            'HSPACING': parameters['input_horizontal_spacing'],
            'TYPE': 2,  # Rectangle (Polygon)
            'VOVERLAY': 0,
            'VSPACING': parameters['input_vertical_spacing'],
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
            'OVERLAY': parameters['input_vector_layer'],
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
            'OUTPUT': parameters['CreategridResult']
        }
        outputs['AddGeometryAttributes'] = processing.run('qgis:exportaddgeometrycolumns', alg_params, context=context,
                                                          feedback=feedback, is_child_algorithm=True)
        results['CreategridResult'] = outputs['AddGeometryAttributes']['OUTPUT']
        return results

    def name(self):
        return 'PV_CreateGrid'

    def displayName(self):
        return 'PV_CreateGrid'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Pv_creategrid()


def runner_PvCreateGrid(
        input_path: str,
        output_path: str,
        h_space: float,
        v_space: float,
        crs: str = "EPSG:2180"):
    # Example inputs
    input_path = input_path
    output_path = output_path  # or "/tmp/clipped.shp"
    input_crs = crs
    h_spacing = h_space
    v_spacing = v_space

    # Build parameter dict for the algorithm
    params = {
        Pv_creategrid.P_INPUT: input_path,
        Pv_creategrid.P_INPUT_CRS: QgsCoordinateReferenceSystem(input_crs),
        Pv_creategrid.P_HSPACE: h_spacing,
        Pv_creategrid.P_VSPACE: v_spacing,
        Pv_creategrid.P_OUT: output_path,
    }

    # Create a processing context & feedback
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()

    # Important: set a project/transform context for CRS transforms
    project = QgsProject.instance()
    context.setProject(project)

    # Run the algorithm class directly
    alg = Pv_creategrid()
    # Normally the framework calls initAlgorithm; when running directly it's safe to call it once:
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)

    print("Creat Grid is complete ->", result.get(Pv_creategrid.P_OUT))


### ================================== PV CREATE BOX CENTROID ================================= ###

class Pv_createcentroid(QgsProcessingAlgorithm):
    P_INPUT = "input_vector_layer"
    P_OUT = "CentroidResult"
    P_INPUT_CRS = 'input_crs'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_INPUT, 'input vector layer',
                                                            types=[QgsProcessing.TypeVectorAnyGeometry],
                                                            defaultValue=None))
        self.addParameter(QgsProcessingParameterCrs(self.P_INPUT_CRS, 'input crs', defaultValue='EPSG:4326'))
        self.addParameter(
            QgsProcessingParameterFeatureSink(self.P_OUT, 'Centroid Result', type=QgsProcessing.TypeVectorAnyGeometry,
                                              createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(3, model_feedback)
        results = {}
        outputs = {}

        # Centroids
        alg_params = {
            'ALL_PARTS': True,
            'INPUT': parameters['input_vector_layer'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
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
            'TARGET_CRS': parameters['input_crs'],
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
            'OUTPUT': parameters['CentroidResult']
        }
        outputs['AddXyFieldsToLayer'] = processing.run('native:addxyfields', alg_params, context=context,
                                                       feedback=feedback, is_child_algorithm=True)
        results['CentroidResult'] = outputs['AddXyFieldsToLayer']['OUTPUT']
        return results

    def name(self):
        return 'PV_CreateCentroid'

    def displayName(self):
        return 'PV_CreateCentroid'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Pv_createcentroid()


def runner_PvCreateCentroid(
        input_path: str,
        output_path: str,
        crs: str = "EPSG:4326"):
    input_path = input_path
    output_path = output_path
    input_crs = crs

    # Build parameter dict for the algorithm
    params = {
        Pv_createcentroid.P_INPUT: input_path,
        Pv_createcentroid.P_INPUT_CRS: QgsCoordinateReferenceSystem(input_crs),
        Pv_createcentroid.P_OUT: output_path,
    }

    # Create a processing context & feedback
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()

    # Important: set a project/transform context for CRS transforms
    project = QgsProject.instance()
    context.setProject(project)

    # Run the algorithm class directly
    alg = Pv_createcentroid()
    # Normally the framework calls initAlgorithm; when running directly it's safe to call it once:
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)

    print("Created Centroid is Completed ->", result.get(Pv_createcentroid.P_OUT))


### ================================== PV ZONAL STATISTIC ================================= ###

class Pv_zonalstatistic(QgsProcessingAlgorithm):
    P_INPUT_VECTOR = "input_vector_layer"
    P_INPUT_RASTER = "input_raster_layer"
    P_OUT = 'ZonalStatisticResult'

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterRasterLayer(self.P_INPUT_RASTER, 'input raster layer', defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_INPUT_VECTOR, 'input vector layer',
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
            'INPUT': parameters['input_raster_layer'],
            'KEEP_RESOLUTION': False,
            'MASK': parameters['input_vector_layer'],
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
            'INPUT': parameters['input_vector_layer'],
            'INPUT_RASTER': outputs['ClipRasterByMaskLayer']['OUTPUT'],
            'RASTER_BAND': 1,
            'STATISTICS': [0, 1, 2],  # Count,Sum,Mean
            'OUTPUT': parameters['ZonalStatisticResult']
        }
        outputs['ZonalStatistics'] = processing.run('native:zonalstatisticsfb', alg_params, context=context,
                                                    feedback=feedback, is_child_algorithm=True)
        results['ZonalStatisticResult'] = outputs['ZonalStatistics']['OUTPUT']
        return results

    def name(self):
        return 'PV_ZonalStatistic'

    def displayName(self):
        return 'PV_ZonalStatistic'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Pv_zonalstatistic()


def runner_PvZonalStatistic(input_vector: str,
                            raster_vector: str,
                            output_path: str):
    # Example inputs
    input_vector_path = input_vector
    input_raster_path = raster_vector
    output_path = output_path

    # Build parameter dict for the algorithm
    params = {
        Pv_zonalstatistic.P_INPUT_VECTOR: input_vector_path,
        Pv_zonalstatistic.P_INPUT_RASTER: input_raster_path,
        Pv_zonalstatistic.P_OUT: output_path,
    }

    # Create a processing context & feedback
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()

    # Important: set a project/transform context for CRS transforms
    project = QgsProject.instance()
    context.setProject(project)

    # Run the algorithm class directly
    alg = Pv_zonalstatistic()
    # Normally the framework calls initAlgorithm; when running directly it's safe to call it once:
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)

    print("calculated zonal statistic Done ->", result.get(Pv_zonalstatistic.P_OUT))


### ================================== PV LAND USE RATIO ================================= ###

class Pv_landuseratio(QgsProcessingAlgorithm):
    P_INPUT_BOX_GRID = "input_box_grid"
    P_INPUT_LAND_LAYER = "input_land_layer"
    P_OUT = 'LandUseScore'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_INPUT_BOX_GRID, 'input box grid',
                                                            types=[QgsProcessing.TypeVectorAnyGeometry],
                                                            defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_INPUT_LAND_LAYER, 'input land layer',
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
            'INPUT': parameters['input_box_grid'],
            'INPUT_FIELDS': [''],
            'OVERLAY': parameters['input_land_layer'],
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
            'OUTPUT': parameters['LandUseScore']
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context,
                                                    feedback=feedback, is_child_algorithm=True)
        results['LandUseScore'] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self):
        return 'PV_LandUseRatio'

    def displayName(self):
        return 'PV_LandUseRatio'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Pv_landuseratio()


def runner_PvLandUseRatio(input_vector: str,
                          input_land_vector: str,
                          output_path: str):
    # Example inputs
    input_box_grid_path = input_vector
    input_land_layer_path = input_land_vector
    output_path = output_path

    # Build parameter dict for the algorithm
    params = {
        Pv_landuseratio.P_INPUT_BOX_GRID: input_box_grid_path,
        Pv_landuseratio.P_INPUT_LAND_LAYER: input_land_layer_path,
        Pv_landuseratio.P_OUT: output_path,
    }

    # Create a processing context & feedback
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()

    # Important: set a project/transform context for CRS transforms
    project = QgsProject.instance()
    context.setProject(project)

    # Run the algorithm class directly
    alg = Pv_landuseratio()
    # Normally the framework calls initAlgorithm; when running directly it's safe to call it once:
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)

    print("calculated land ratio Done ->", result.get(Pv_landuseratio.P_OUT))





### ================================== clipped  ================================= ###


class ModelClip(QgsProcessingAlgorithm):
    P_INPUT_DSO_CENTROID = 'input_dso_centroid'
    P_INPUT_MAP_BOUNDARY = 'input_map_boundary'
    P_OUTPUT = 'DsoClipped'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_INPUT_DSO_CENTROID, 'input dso centroid',
                                                            types=[QgsProcessing.TypeVectorAnyGeometry],
                                                            defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_INPUT_MAP_BOUNDARY, 'input map boundary',
                                                            types=[QgsProcessing.TypeVectorAnyGeometry],
                                                            defaultValue=None))
        self.addParameter(
            QgsProcessingParameterFeatureSink(self.P_OUTPUT, 'dso clipped', type=QgsProcessing.TypeVectorAnyGeometry,
                                              createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Clip
        alg_params = {
            'INPUT': parameters['input_dso_centroid'],
            'OVERLAY': parameters['input_map_boundary'],
            'OUTPUT': parameters['DsoClipped']
        }
        outputs['Clip'] = processing.run('native:clip', alg_params, context=context, feedback=feedback,
                                         is_child_algorithm=True)
        results['DsoClipped'] = outputs['Clip']['OUTPUT']
        return results

    def name(self):
        return 'ModelClip'

    def displayName(self):
        return 'ModelClip'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return ModelClip()


def runner_ModelClip(input_dso,
                     input_map_vector: str,
                     output_path: str):
    # Example inputs
    input_dso_centroid = input_dso
    input_map_vector_path = input_map_vector
    output_path = output_path

    # Build parameter dict for the algorithm
    params = {
        ModelClip.P_INPUT_DSO_CENTROID: input_dso_centroid,
        ModelClip.P_INPUT_MAP_BOUNDARY: input_map_vector_path,
        ModelClip.P_OUTPUT: output_path,
    }

    # Create a processing context & feedback
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()

    # Important: set a project/transform context for CRS transforms
    project = QgsProject.instance()
    context.setProject(project)

    # Run the algorithm class directly
    alg = ModelClip()
    # Normally the framework calls initAlgorithm; when running directly it's safe to call it once:
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)

    print("clip done  ->", result.get(ModelClip.P_OUTPUT))


def gdf_to_qgs_geojson(gdf, name="layer"):
    if gdf.crs is None:
        gdf = gdf.set_crs("EPSG:4326")  # GeoJSON expects WGS84
    tmp = tempfile.NamedTemporaryFile(suffix=".geojson", delete=False)
    gdf.to_file(tmp.name, driver="GeoJSON")
    return QgsVectorLayer(tmp.name, name, "ogr")

# def save_geojson_and_csv(geojson_path: Path, keep_geometry: bool = False, model_name: str = None,
#                          region_name: str = None, id_name: str = None, df_return =False):
#     try:
#         # 1. Read GeoJSON
#         with open(geojson_path, 'r', encoding='utf-8') as f:
#             geojson_data = json.load(f)
#
#         records = []
#         features = geojson_data.get('features', [])
#
#         # 2. Extract properties for CSV/JSON Fixture
#         for feature in features:
#             props = feature.get('properties', {}).copy()  # Copy to avoid mutating original data
#
#             if keep_geometry:
#                 geometry = feature.get('geometry', {})
#                 if geometry:
#                     props['geometry'] = json.dumps(geometry)
#
#             records.append(props)
#
#         if not records:
#             print(f"  ⚠ Warning: No records found in {geojson_path}")
#             return
#
#         # 3. Process Data via DataFrame
#         df = pd.DataFrame(records)
#         if region_name:
#             df['region_name'] = region_name
#         if id_name and 'id' in df.columns:
#             df.rename(columns={'id': id_name}, inplace=True)
#
#         # --- SAVE CSV ---
#         csv_path = geojson_path.with_suffix('.csv')
#         df.to_csv(csv_path, index=False)
#         print(f"  → Saved CSV: {csv_path}")
#
#         # --- SAVE DJANGO FIXTURE (JSON) ---
#         if model_name:
#             # We use a specific suffix to avoid overwriting original json files
#             fixture_path = geojson_path.with_name(f"{geojson_path.stem}_fixture.json")
#             df_records = df.to_dict(orient='records')
#             fixture_result = [
#                 {"model": model_name, "fields": record}
#                 for record in df_records
#             ]
#             with open(fixture_path, 'w', encoding='utf-8') as f:
#                 json.dump(fixture_result, f, indent=2)
#             print(f"  → Saved JSON Fixture: {fixture_path}")
#
#         # --- SAVE UPDATED GEOJSON ---
#         # If you want to save the GeoJSON with the NEW property names (like id_name)
#         # we must update the features in the geojson_data object.
#         for i, feature in enumerate(features):
#             if i < len(df):
#                 feature['properties'] = df.iloc[i].to_dict()
#                 # Remove geometry from properties if it was added there for the CSV
#                 if 'geometry' in feature['properties']:
#                     del feature['properties']['geometry']
#
#         output_geojson_path = geojson_path.with_name(f"{geojson_path.stem}_updated.geojson")
#         with open(output_geojson_path, 'w', encoding='utf-8') as f:
#             json.dump(geojson_data, f, indent=2)
#         print(f"  → Saved Modified GeoJSON: {output_geojson_path}")
#
#     except Exception as e:
#         print(f"  ⚠ Error: Could not process {geojson_path}: {e}")
#
#     if df_return:
#         return df

def save_geojson_and_csv(geojson_path: Path, keep_geometry: bool = False, model_name: str = None,
                         region_name: str = None, id_name: str = None, id_prefix: str = "", df_return=False):
    try:
        # 1. Read GeoJSON
        with open(geojson_path, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)

        records = []
        features = geojson_data.get('features', [])

        # 2. Extract properties
        for feature in features:
            props = feature.get('properties', {}).copy()

            if keep_geometry:
                geometry = feature.get('geometry', {})
                if geometry:
                    props['geometry'] = json.dumps(geometry)
            records.append(props)

        if not records:
            print(f"  ⚠ Warning: No records found in {geojson_path}")
            return

        # 3. Process Data via DataFrame
        df = pd.DataFrame(records)
        

        # --- APPLY PREFIX AND RENAME ID ---
        # If 'id' exists, rename it first to the target id_name (e.g., 'osm_box_id')
        if id_name and 'id' in df.columns:
            df.rename(columns={'id': id_name}, inplace=True)

        # Apply the prefix to the ID column if provided
        target_id_col = id_name if id_name in df.columns else 'id'
        if id_prefix and target_id_col in df.columns:
            df[target_id_col] = df[target_id_col].apply(
                lambda x: f"{id_prefix}{x}" if x is not None and str(x).lower() != 'nan' else x
            )

        if region_name:
            df['region_name'] = region_name

        # --- SAVE CSV ---
        csv_path = geojson_path.with_suffix('.csv')
        df.to_csv(csv_path, index=False)
        print(f"  → Saved CSV: {csv_path}")

        # --- SAVE DJANGO FIXTURE (JSON) ---
        if model_name:
            fixture_path = geojson_path.with_name(f"{geojson_path.stem}_fixture.json")
            df_records = df.to_dict(orient='records')

            fixture_result = []
            for record in df_records:
                # Use the updated ID (with prefix) as the primary key for Django
                pk_val = record.get(target_id_col)
                fixture_result.append({
                    "model": model_name,
                    "pk": pk_val,
                    "fields": record
                })

            with open(fixture_path, 'w', encoding='utf-8') as f:
                json.dump(fixture_result, f, indent=2)
            print(f"  → Saved JSON Fixture: {fixture_path}")

        # --- SAVE UPDATED GEOJSON ---
        for i, feature in enumerate(features):
            if i < len(df):
                # This dict now contains the prefixed ID and renamed columns
                feature['properties'] = df.iloc[i].to_dict()
                if 'geometry' in feature['properties']:
                    del feature['properties']['geometry']

        output_geojson_path = geojson_path.with_name(f"{geojson_path.stem}_updated.geojson")
        with open(output_geojson_path, 'w', encoding='utf-8') as f:
            json.dump(geojson_data, f, indent=2)
        print(f"  → Saved Modified GeoJSON: {output_geojson_path}")

    except Exception as e:
        print(f"  ⚠ Error: Could not process {geojson_path}: {e}")

    if df_return:
        return  df
    
    
def save_final_score(df_final, output_path: Path, model_name: str, region_name: str):
    """
    Saves the merged df_final into:
    1. .geojson (Spatial data)
    2. .csv (Flat table)
    3. _fixture.json (Django-ready format)
    """
    try:
        # --- 1. Preparation ---
        # Ensure it's a GeoDataFrame and fill missing values
        if not isinstance(df_final, gpd.GeoDataFrame):
            df_final = gpd.GeoDataFrame(df_final, geometry='geometry')

        df_final = df_final.fillna(0)
        df_final['region_name'] = region_name

        # --- 2. Save GeoJSON ---
        geojson_out = output_path.with_suffix('.geojson')
        df_final.to_file(geojson_out, driver='GeoJSON')
        print(f"  → Saved GeoJSON: {geojson_out}")

        # --- 3. Prepare for Text-based Formats (CSV/JSON) ---
        # We must convert the geometry object to a string (WKT)
        # so it doesn't crash the JSON serializer.
        df_text = df_final.copy()
        if 'geometry' in df_text.columns:
            df_text['geometry'] = df_text['geometry'].apply(lambda x: x.wkt if x else None)

        # --- 4. Save CSV ---
        csv_out = output_path.with_suffix('.csv')
        df_text.to_csv(csv_out, index=False)
        print(f"  → Saved CSV: {csv_out}")

        # --- 5. Save Django JSON Fixture ---
        fixture_out = output_path.with_name(f"{output_path.stem}_fixture.json")
        records = df_text.to_dict(orient='records')

        fixture_data = []
        for record in records:
            # Try to find the primary key dynamically
            pk_val = record.get('osm_final_score_id') or record.get('osm_box_id')

            fixture_data.append({
                "model": model_name,
                "pk": pk_val,
                "fields": record
            })

        with open(fixture_out, 'w', encoding='utf-8') as f:
            json.dump(fixture_data, f, indent=2)
        print(f"  → Saved JSON Fixture: {fixture_out}")

    except Exception as e:
        print(f"  ⚠ Error saving results: {e}")

def runner_FinalScore(*args):
    # args[0] is df_box (the base with geometry)
    df_final = args[0].copy()
    geometry = df_final['geometry']
    df_final = df_final[['osm_box_id','area','perimeter']]
    
  

    # Mapping of (DataFrame, Source_ID, Source_Value, Target_Name)
    categories = [
        (args[1], 'osm_land_id', 'ratio', 'land_score'),
        (args[2], 'osm_box2dso_id', 'score', 'dso_score'),
        (args[3], 'osm_box2plant_id', 'score', 'plant_score'),
        (args[4], 'osm_box2railway_id', 'score', 'railway_score'),
        (args[5], 'osm_box2road_id', 'score', 'road_score'),
        (args[6], 'osm_dni_id', '_mean', 'dni_score'),
        (args[7], 'osm_dem_id', '_mean', 'dem_score'),
        (args[8], 'osm_pvout_id', '_mean', 'pvout_score'),
        (args[9], 'osm_temp_id', '_mean', 'temp_score'),
        (args[2], 'osm_box2dso_id', 'score', 'dsomocy_score')
        
    ]

    for df_cat, id_col, val_col, new_name in categories:
        temp_df = df_cat[[id_col, val_col]].rename(columns={
            id_col: 'osm_box_id',
            val_col: new_name
        })
        df_final = pd.merge(df_final, temp_df, on='osm_box_id', how='left')
    

    # # Ensure it is a GeoDataFrame (important for saving GeoJSON)
    # if not isinstance(df_final, gpd.GeoDataFrame):
    #     df_final = gpd.GeoDataFrame(df_final, geometry='geometry', crs="EPSG:4326")
    df_final['geometry'] = geometry

    return df_final


##### run pipeline 


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
    centroid_railway_path = input_path / "railway_station.geojson"
    centroid_road_path = input_path / "road_vertices.geojson"
    centroid_dsomocy_path = input_path / "dolnoslaskie_tauron_moc.geojson" #"dostepnamoc_tauron.geojson"

    h_space = args.h_space
    v_space = args.v_space
    operator_name = args.operator
    region_name = args.region_name
    id_prefix = args.id_prefix

    ### Extract path
    box_path = output_path / "box.geojson"
    land_ratio_path = output_path / "land_ratio.geojson"
    centroid_box_path = output_path / "centroid_box.geojson"
    centroid_dso_path = output_path / "centroid_dso.geojson"
    centroid_score_box2dso = output_path / "centroid_score_box2dso.geojson"
    centroid_score_box2plant = output_path / "centroid_score_box2plant.geojson"
    centroid_score_box2railway = output_path / "centroid_score_box2railway.geojson"
    centroid_score_box2road = output_path / "centroid_score_box2road.geojson"
    dni_zonal_path = output_path / "dni_zonal.geojson"
    pvout_zonal_path = output_path / "pvout_zonal.geojson"
    temp_zonal_path = output_path / "temp_zonal.geojson"
    dem_zonal_path = output_path / "dem_zonal.geojson"
    final_mcdm_score_path = output_path / "final_mcdm_score.csv"
    # additional work on tauron dso
    centroid_score_box2dsomocy = output_path / "centroid_score_box2dsomocy.geojson"


    # allow choosing steps (0..8) or 'all'
    steps_to_run = set()
    if args.steps:
        for s in args.steps:
            if s == "all":
                steps_to_run = set(map(str, range(0, 14)))
                break
            steps_to_run.add(str(s))
    else:
        steps_to_run = set(map(str, range(0, 14)))  # default: run all steps

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
        save_geojson_and_csv(centroid_dso_path, keep_geometry=False)

    # 1) Create box
    if should_run(box_path, "1"):
        box_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 1: Creating box grid → {box_path}")
        runner_PvCreateGrid(str(boundary_path), str(box_path), h_space, v_space)
        df_box = save_geojson_and_csv(box_path, keep_geometry=True, model_name='data.Box', region_name=region_name, id_name='osm_box_id',id_prefix=id_prefix ,df_return=True)
        #print(df_box.head(3))

    # 2) Create centroid box
    if should_run(centroid_box_path, "2"):
        centroid_box_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 2: Creating centroid box → {centroid_box_path}")
        runner_PvCreateCentroid(str(box_path), str(centroid_box_path))
        save_geojson_and_csv(centroid_box_path,keep_geometry=True, model_name='data.CentroidBox', region_name=region_name, id_name='osm_centroid_box_id')

    # 3) Calculate distance centroid box-dso
    if should_run(centroid_score_box2dso, "3"):
        centroid_score_box2dso.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 3: Creating score centroid box-dso → {centroid_score_box2dso}")
        runner_PV_Box2Dso(str(centroid_box_path), str(centroid_dso_path), str(centroid_score_box2dso))
        df_dso= save_geojson_and_csv(centroid_score_box2dso,keep_geometry=True, model_name='data.CentroidBox2Dso', region_name=region_name, id_name='osm_box2dso_id',df_return=True)

    # 4) calculate distance centroid box-plant
    if should_run(centroid_score_box2plant, "4"):
        centroid_score_box2plant.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 4: Creating score centroid box-plant → {centroid_score_box2plant}")
        runner_PV_Box2Plant(str(centroid_box_path), str(centroid_plant_path),'solar',str(centroid_score_box2plant))
        df_plant=save_geojson_and_csv(centroid_score_box2plant,keep_geometry=True, model_name='data.CentroidBox2Plant', region_name=region_name, id_name='osm_box2plant_id',df_return=True)

    # 5) calculate distance centroid box-railway
    if should_run(centroid_score_box2railway, "5"):
        centroid_score_box2railway.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 5: Creating score centroid box-railway → {centroid_score_box2railway}")
        runner_PV_Box2Railway(str(centroid_box_path), str(centroid_railway_path),str(centroid_score_box2railway))
        df_railway = save_geojson_and_csv(centroid_score_box2railway,keep_geometry=True, model_name='data.CentroidBox2Railway', region_name=region_name, id_name='osm_box2railway_id',df_return=True)

    # 6) calculate distance centroid box-road vertices
    if should_run(centroid_score_box2road, "6"):
        centroid_score_box2road.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 6: Creating score centroid box-road → {centroid_score_box2road}")
        runner_PV_Box2Road(str(centroid_box_path), str(centroid_road_path), str(centroid_score_box2road))
        df_road = save_geojson_and_csv(centroid_score_box2road,keep_geometry=True, model_name='data.CentroidBox2Road', region_name=region_name, id_name='osm_box2road_id',df_return=True)

    # 7) Extracting DNI
    if should_run(dni_zonal_path, "7"):
        dni_zonal_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 7: Extracting DNI → {dni_zonal_path}")
        runner_PvZonalStatistic(str(box_path), str(dni_raster_path), str(dni_zonal_path))
        df_dni = save_geojson_and_csv(dni_zonal_path,keep_geometry=True, model_name='data.Dni', region_name=region_name, id_name='osm_dni_id',df_return=True)

    # 8) Extracting PVOUT
    if should_run(pvout_zonal_path, "8"):
        pvout_zonal_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 8: Extracting PVOUT → {pvout_zonal_path}")
        runner_PvZonalStatistic(str(box_path), str(pvout_raster_path), str(pvout_zonal_path))
        df_pvout = save_geojson_and_csv(pvout_zonal_path,keep_geometry=True, model_name='data.Pvout', region_name=region_name, id_name='osm_pvout_id',df_return=True)

    # 9) Extracting Temperature
    if should_run(temp_zonal_path, "9"):
        temp_zonal_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 9: Extracting TEMP → {temp_zonal_path}")
        runner_PvZonalStatistic(str(box_path), str(temp_raster_path), str(temp_zonal_path))
        df_temp =save_geojson_and_csv(temp_zonal_path,keep_geometry=True, model_name='data.Temp', region_name=region_name, id_name='osm_temp_id',df_return=True)

    # 10) Extracting DEM
    if should_run(dem_zonal_path, "10"):
        dem_zonal_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 10: Extracting DEM → {dem_zonal_path}")
        runner_PvZonalStatistic(str(box_path), str(dem_raster_path), str(dem_zonal_path))
        df_dem = save_geojson_and_csv(dem_zonal_path,keep_geometry=True, model_name='data.Dem', region_name=region_name, id_name='osm_dem_id',df_return=True)

    # 11) Calculate land ratio (kept as separate logical step)
    if should_run(land_ratio_path, "11"):
        land_ratio_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 11: Extracting Land ratio → {land_ratio_path}")
        runner_PvLandUseRatio(str(box_path), str(land_use_path), str(land_ratio_path))
        df_land_ratio = save_geojson_and_csv(land_ratio_path,keep_geometry=True, model_name='data.LandRatio', region_name=region_name, id_name='osm_land_id',df_return=True)
   

    ## additional work
    # 3.1) Calculate distance centroid box to tauron dostepne mocy
    if should_run(centroid_score_box2dsomocy, "12"):
        centroid_score_box2dsomocy.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step : Creating score centroid box-dso → {centroid_score_box2dsomocy}")
        runner_PV_Box2Dso(str(centroid_box_path), str(centroid_dsomocy_path), str(centroid_score_box2dsomocy))
        df_dsomocy= save_geojson_and_csv(centroid_score_box2dsomocy,keep_geometry=True, model_name='data.CentroidBox2DsoMocy', region_name=region_name, id_name='osm_box2dsomocy_id',df_return=True)
    
    # # 12) get the final score
    # if should_run(final_mcdm_score_path, "13"):
    #     final_mcdm_score_path.parent.mkdir(parents=True, exist_ok=True)
    #     print('working on final df')
    #     final_df = runner_FinalScore(df_box, df_land_ratio,df_dso, df_plant,df_railway, df_road, df_dni, df_dem, df_pvout, df_temp,df_dsomocy)
    #     final_df.to_csv(final_mcdm_score_path)

    
    print("Done. The algorithm has finished.")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="main.py",
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

    parser.add_argument("--region-name", type=str,
                        help='region name for the extracting place')

    # steps: allow names/numbers; user can pass multiple e.g. --steps 1 5 6  or --steps all
    parser.add_argument("--steps", nargs="+", help='Steps to run, e.g. 0 1 2 or "all" (default: all)')

    parser.add_argument("--id-prefix", type=str, help='Steps to run, e.g. 0 1 2 or "all" (default: all)')

    parser.add_argument("--force", action="store_true",
                        help="Force running steps even if output files already exist (overwrites)")

    args = parser.parse_args()
    run_pipeline(args)
