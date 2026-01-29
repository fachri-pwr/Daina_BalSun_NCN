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
    QgsProcessingParameterRasterLayer,QgsProcessingParameterString,QgsExpression
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


#### VECTOR DATA EXTRACTION

# ========================== Land use Extraction Class =======================================

class Dataextraction_landuse(QgsProcessingAlgorithm):

    P_boundary_map = 'boundary_map'
    P_landuse_vector = 'landuse_vector'
    P_region_name ='region_name'
    P_landuse_filter = 'landuse_filter'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_boundary_map, 'boundary_map', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_landuse_vector, 'landuse_vector', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterString(self.P_region_name, 'region_name', multiLine=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterFeatureSink(self.P_landuse_filter, 'landuse_filter', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(6, model_feedback)
        results = {}
        outputs = {}

        # Create spatial index landuse vector
        alg_params = {
            'INPUT': parameters[self.P_landuse_vector]
        }
        outputs['CreateSpatialIndexLanduseVector'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Fix geometries
        alg_params = {
            'INPUT': parameters[self.P_boundary_map],
            'METHOD': 0,  # Linework
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FixGeometries'] = processing.run('native:fixgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Create spatial index boundary map
        alg_params = {
            'INPUT': outputs['FixGeometries']['OUTPUT']
        }
        outputs['CreateSpatialIndexBoundaryMap'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Clip
        alg_params = {
            'INPUT': outputs['CreateSpatialIndexLanduseVector']['OUTPUT'],
            'OVERLAY': outputs['CreateSpatialIndexBoundaryMap']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Clip'] = processing.run('native:clip', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Extract by expression
        alg_params = {
            'EXPRESSION': '"fclass" IN (\'farmland\', \'farmyard\', \'grass\', \'heath\', \'meadow\', \'scrub\')',
            'INPUT': outputs['Clip']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByExpression'] = processing.run('native:extractbyexpression', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
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
            'INPUT': outputs['ExtractByExpression']['OUTPUT'],
            'OUTPUT': parameters[self.P_landuse_filter]
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results[self.P_landuse_filter] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self): return 'dataExtraction_landuse'
    def displayName(self): return 'dataExtraction_landuse'
    def group(self): return ''
    def groupId(self): return ''
    def createInstance(self): return Dataextraction_landuse()

def runner_Dataextraction_landuse(boundary_path, landuse_path, region_name ,filter_path):
    params = {
        Dataextraction_landuse.P_boundary_map: boundary_path,
        Dataextraction_landuse.P_landuse_vector: landuse_path,
        Dataextraction_landuse.P_region_name: region_name,
        Dataextraction_landuse.P_landuse_filter: filter_path,
    }
    
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    context.setProject(QgsProject.instance())
    
    alg = Dataextraction_landuse()
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)
    print(f"Success: Saved to {filter_path}")


# ========================== RailwayStation Extraction Class =================================

class Dataextraction_railwaystation(QgsProcessingAlgorithm):
    P_boundary_map = 'boundary_map'
    P_railwayStation_vector = 'railwayStation_vector'
    P_region_name = 'region_name'
    P_railwayStation_filter = 'landuse_filter'
   
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_boundary_map, 'boundary_map', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_railwayStation_vector, 'railwayStation_vector', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterString(self.P_region_name , 'region_name', multiLine=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterFeatureSink(self.P_railwayStation_filter, 'railwayStation_filter', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(6, model_feedback)
        results = {}
        outputs = {}

        # Create spatial index_railwayStation vector
        alg_params = {
            'INPUT': parameters[self.P_railwayStation_vector]
        }
        outputs['CreateSpatialIndex_railwaystationVector'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Fix geometries
        alg_params = {
            'INPUT': parameters[self.P_boundary_map],
            'METHOD': 0,  # Linework
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FixGeometries'] = processing.run('native:fixgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Create spatial index_boundary map
        alg_params = {
            'INPUT': outputs['FixGeometries']['OUTPUT']
        }
        outputs['CreateSpatialIndex_boundaryMap'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Clip
        alg_params = {
            'INPUT': outputs['CreateSpatialIndex_railwaystationVector']['OUTPUT'],
            'OVERLAY': outputs['CreateSpatialIndex_boundaryMap']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Clip'] = processing.run('native:clip', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Extract by expression
        alg_params = {
            'EXPRESSION': '"fclass" IN (\'railway_station\', \'railway_halt\')',
            'INPUT': outputs['Clip']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractByExpression'] = processing.run('native:extractbyexpression', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
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
            'INPUT': outputs['ExtractByExpression']['OUTPUT'],
            'OUTPUT': parameters[self.P_railwayStation_filter]
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results[self.P_railwayStation_filter] = outputs['FieldCalculator']['OUTPUT']
        return results
    
    def name(self): return 'dataExtraction_railwayStation'
    def displayName(self):return 'dataExtraction_railwayStation'
    def group(self): return ''
    def groupId(self):return ''
    def createInstance(self):return Dataextraction_railwaystation()
    

def runner_Dataextraction_railwaystation(boundary_path, railwayStation_path, region_name ,filter_path):
    params = {
        Dataextraction_railwaystation.P_boundary_map: boundary_path,
        Dataextraction_railwaystation.P_railwayStation_vector: railwayStation_path,
        Dataextraction_railwaystation.P_region_name: region_name,
        Dataextraction_railwaystation.P_railwayStation_filter: filter_path,
    }
    
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    context.setProject(QgsProject.instance())
    
    alg = Dataextraction_railwaystation()
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)
    print(region_name)
    print(f"Success: Saved to {filter_path}")
    

# ========================== RoadVertices Extraction Class =================================

class Dataextraction_roadvertices(QgsProcessingAlgorithm):
    
    P_boundary_map = 'boundary_map'
    P_road_vector = 'road_vector'
    P_region_name = 'region_name'
    P_roadVertices_filter = 'roadVertices_filter'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_boundary_map, 'boundary_map', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterString(self.P_region_name, 'region_name', multiLine=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_road_vector, 'road_vector', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink(self.P_roadVertices_filter, 'roadVertices_filter', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Multi-step feedback for 10 steps as defined in your original code
        feedback = QgsProcessingMultiStepFeedback(10, model_feedback)
        results = {}
        outputs = {}

        # 0. Create spatial index_road vector
        alg_params = {
            'INPUT': parameters[self.P_road_vector]
        }
        outputs['CreateSpatialIndex_roadVector'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # 1. Fix geometries
        alg_params = {
            'INPUT': parameters[self.P_boundary_map],
            'METHOD': 0,  
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FixGeometries'] = processing.run('native:fixgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # 2. Create spatial index_boundary map
        alg_params = {
            'INPUT': outputs['FixGeometries']['OUTPUT']
        }
        outputs['CreateSpatialIndex_boundaryMap'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # 3. Clip
        alg_params = {
            'INPUT': parameters[self.P_road_vector],
            'OVERLAY': outputs['FixGeometries']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Clip'] = processing.run('native:clip', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # 4. Drop field(s) road layer column
        # Fixed: COLUMN expects a list of field names
        alg_params = {
            'COLUMN': ['ref', 'oneway', 'maxspeed', 'layer', 'bridge', 'tunnel'],
            'INPUT': outputs['Clip']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['DropFieldsRoadLayerColumn'] = processing.run('native:deletecolumn', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # 5. Field calculator (Region Name)
        region_val = parameters[self.P_region_name]
        alg_params = {
            'FIELD_LENGTH': 100,
            'FIELD_NAME': 'region_name',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 2, # 2 = String
            'FORMULA': f"'{region_val}'", # Wrapped in single quotes for text
            'INPUT': outputs['DropFieldsRoadLayerColumn']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}

        # 6. Extract vertices
        alg_params = {
            'INPUT': outputs['FieldCalculator']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractVertices'] = processing.run('native:extractvertices', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}

        # 7. Drop field(s) road vertices
        # Fixed: COLUMN expects a list of field names
        alg_params = {
            'COLUMN': ['vertex_index', 'vertex_part', 'vertex_part_index', 'distance', 'angle'],
            'INPUT': outputs['ExtractVertices']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['DropFieldsRoadVertices'] = processing.run('native:deletecolumn', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(8)
        if feedback.isCanceled():
            return {}

        # 8. Field calculator x
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'x',
            'FIELD_PRECISION': 8,
            'FIELD_TYPE': 0,  # 0 = Float
            'FORMULA': '$x',
            'INPUT': outputs['DropFieldsRoadVertices']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FieldCalculatorX'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(9)
        if feedback.isCanceled():
            return {}

        # 9. Field calculator y
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'y',
            'FIELD_PRECISION': 8,
            'FIELD_TYPE': 0, # 0 = Float
            'FORMULA': '$y',
            'INPUT': outputs['FieldCalculatorX']['OUTPUT'],
            'OUTPUT': parameters[self.P_roadVertices_filter]
        }
        outputs['FieldCalculatorY'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        
        results[self.P_roadVertices_filter] = outputs['FieldCalculatorY']['OUTPUT']
        return results

    def name(self): return 'dataExtraction_roadVertices'
    def displayName(self): return 'dataExtraction_roadVertices'
    def group(self): return ''
    def groupId(self): return ''
    def createInstance(self): return Dataextraction_roadvertices()

def runner_Dataextraction_roadvertices(boundary_path, road_path, region_name ,filter_path):
    params = {
        Dataextraction_roadvertices.P_boundary_map: boundary_path,
        Dataextraction_roadvertices.P_road_vector: road_path,
        Dataextraction_roadvertices.P_region_name: region_name,
        Dataextraction_roadvertices.P_roadVertices_filter: filter_path,
    }
    
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    context.setProject(QgsProject.instance())
    
    alg = Dataextraction_roadvertices()
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)
    print(f"Region: {region_name}")
    print(f"Success: Saved to {filter_path}")

# ========================== Runner and Pipeline ==============================================

def run_pipeline(args):
    
    # --- 2. PATH LOGIC ---
    # input_base is: /Users/sell/work/code_work/daina_project/data/daina
    input_path = Path(args.input_path)
    print(input_path)


    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GIS Data Extraction Pipeline")

    parser.add_argument("--input-path", type=str, required=True)

    
    args = parser.parse_args()
    run_pipeline(args)
    
    

# python dataExtraction.py --input-path "/Users/sell/work/code_work/daina_project/data/daina" 



