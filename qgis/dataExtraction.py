import os
import sys
import pandas as pd
import geopandas as gpd
import argparse
from pathlib import Path
import tempfile
import fiona
from shapely.validation import explain_validity

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


### VECTOR DATA #####

# ========================== Fix Geometries Class =======================================

class Dataextraction_fixgeometry(QgsProcessingAlgorithm):
    P_boundary_map = 'boundary_map'
    P_fix_geometries = 'fix_geometries'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_boundary_map , 'boundary_map', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink(self.P_fix_geometries , 'fix_geometries', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(2, model_feedback)
        results = {}
        outputs = {}

        # Create spatial index
        alg_params = {
            'INPUT': parameters[self.P_boundary_map ]
        }
        outputs['CreateSpatialIndex'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Fix geometries
        alg_params = {
            'INPUT': outputs['CreateSpatialIndex']['OUTPUT'],
            'METHOD': 0,  # Linework
            'OUTPUT': parameters[self.P_fix_geometries ]
        }
        outputs['FixGeometries'] = processing.run('native:fixgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results[self.P_fix_geometries ] = outputs['FixGeometries']['OUTPUT']
        return results

    def name(self):
        return 'dataExtraction_fixGeometry'

    def displayName(self):
        return 'dataExtraction_fixGeometry'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Dataextraction_fixgeometry()


def runner_Dataextraction_fixgeometry(boundary_path, fix_geometries_path):
    params={
        Dataextraction_fixgeometry.P_boundary_map : boundary_path,
        Dataextraction_fixgeometry.P_fix_geometries : fix_geometries_path 
    }
    
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    context.setProject(QgsProject.instance())
    
    alg = Dataextraction_fixgeometry()
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)
    print(f"Success: Saved to {Dataextraction_fixgeometry.P_fix_geometries}")
    
def is_layer_valid(file_path):
    path_str = str(file_path)
    layer = QgsVectorLayer(path_str, "check_layer", "ogr")
    
    if not layer.isValid():
        print(f"Layer failed to load: {path_str}")
        return False

    for feature in layer.getFeatures():
        geom = feature.geometry()
        
        if geom.isNull() or geom.isEmpty():
            continue
            
        # Use the explicit validateGeometry call which returns a list of errors
        # If the list is NOT empty, the geometry is invalid.
        errors = geom.validateGeometry()
        if len(errors) > 0:
            print(f"Invalid geometry found at Feature ID {feature.id()}")
            print(f"Reason: {errors[0].what()}")
            return False 
            
    return True


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
        feedback = QgsProcessingMultiStepFeedback(7, model_feedback)
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
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        
        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}
        
        # Rename field
        alg_params = {
            'FIELD': 'osm_id',
            'INPUT': outputs['FieldCalculator']['OUTPUT'],
            'NEW_NAME': 'land_id',
            'OUTPUT': parameters[self.P_landuse_filter]
        }
        outputs['RenameField'] = processing.run('native:renametablefield', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results[self.P_landuse_filter] = outputs['RenameField']['OUTPUT']
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
        Dataextraction_landuse.P_landuse_filter: filter_path }
    
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    context.setProject(QgsProject.instance())
    
    alg = Dataextraction_landuse()
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)



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
        feedback = QgsProcessingMultiStepFeedback(9, model_feedback)
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
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        
        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}
        
        # Rename field
        alg_params = {
            'FIELD': 'osm_id',
            'INPUT': outputs['FieldCalculator']['OUTPUT'],
            'NEW_NAME': 'station_id',
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['RenameField'] = processing.run('native:renametablefield', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}

        # Field calculator x
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'x',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 0,  # Decimal (double)
            'FORMULA': '$x',
            'INPUT': outputs['RenameField']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FieldCalculatorX'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(8)
        if feedback.isCanceled():
            return {}

        # Field calculator y
        alg_params = {
            'FIELD_LENGTH': 0,
            'FIELD_NAME': 'y',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 0,  # Decimal (double)
            'FORMULA': '$y',
            'INPUT': outputs['FieldCalculatorX']['OUTPUT'],
            'OUTPUT': parameters[self.P_railwayStation_filter]
        }
        outputs['FieldCalculatorY'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results[self.P_railwayStation_filter]= outputs['FieldCalculatorY']['OUTPUT']
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
        feedback = QgsProcessingMultiStepFeedback(11, model_feedback)
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
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['FieldCalculatorY'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        
        feedback.setCurrentStep(10)
        if feedback.isCanceled():
            return {}
        
        # Rename field
        alg_params = {
            'FIELD': 'osm_id',
            'INPUT': outputs['FieldCalculatorY']['OUTPUT'],
            'NEW_NAME': 'road_id',
            'OUTPUT': parameters[self.P_roadVertices_filter]
        }
        outputs['RenameField'] = processing.run('native:renametablefield', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        
        results[self.P_roadVertices_filter] = outputs['RenameField']['OUTPUT']
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
    print(f"Success: Saved to {filter_path}")

# ========================== Runner and Pipeline ==============================================

class Dataextraction_clipvector(QgsProcessingAlgorithm):
    
    P_boundary_map = 'boundary_map'
    P_input_vector = 'input_vector'
    P_region_name = 'region_name'
    P_clip_vector = 'clip_vector'


    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_boundary_map, 'boundary_map', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_input_vector, 'input_vector', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterString(self.P_region_name, 'region_name', multiLine=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterFeatureSink(self.P_clip_vector, 'clip_vector', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(3, model_feedback)
        results = {}
        outputs = {}

        # Create spatial index
        alg_params = {
            'INPUT': parameters[self.P_boundary_map]
        }
        outputs['CreateSpatialIndex'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Clip
        alg_params = {
            'INPUT': parameters[self.P_input_vector],
            'OVERLAY': outputs['CreateSpatialIndex']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Clip'] = processing.run('native:clip', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
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
            'INPUT': outputs['Clip']['OUTPUT'],
            'OUTPUT': parameters[self.P_clip_vector]
        }
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results[self.P_clip_vector] = outputs['FieldCalculator']['OUTPUT']
        return results

    def name(self): return 'dataExtraction_clipVector'
    def displayName(self): return 'dataExtraction_clipVector'
    def group(self): return ''
    def groupId(self): return ''
    def createInstance(self): return Dataextraction_clipvector()



def runner_Dataextraction_clipvector(boundary_path, input_vector_path, region_name ,vector_clip_path):
    params = {
        Dataextraction_clipvector.P_boundary_map: boundary_path,
        Dataextraction_clipvector.P_input_vector : input_vector_path,
        Dataextraction_clipvector.P_region_name: region_name,
        Dataextraction_clipvector.P_clip_vector: vector_clip_path,
    }
    
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    context.setProject(QgsProject.instance())
    
    alg = Dataextraction_clipvector()
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)
    print(f"Success: Saved to {vector_clip_path}")

### RASTER DATA #####

class Dataextraction_clipraster(QgsProcessingAlgorithm):
    P_boundary_map = 'boundary_map'
    P_raster_layer = 'raster_layer'
    P_clip_raster ='clip_raster'
    
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_boundary_map, 'boundary_map', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterLayer(self.P_raster_layer, 'raster_layer', defaultValue=None))
        self.addParameter(QgsProcessingParameterRasterDestination(self.P_clip_raster, 'clip_raster', createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(1, model_feedback)
        results = {}
        outputs = {}

        # Clip raster by mask layer
        alg_params = {
            'ALPHA_BAND': False,
            'CROP_TO_CUTLINE': True,
            'DATA_TYPE': 0,  # Use Input Layer Data Type
            'EXTRA': '',
            'INPUT': parameters[self.P_raster_layer],
            'KEEP_RESOLUTION': False,
            'MASK': parameters[self.P_boundary_map],
            'MULTITHREADING': False,
            'NODATA': None,
            'OPTIONS': '',
            'SET_RESOLUTION': False,
            'SOURCE_CRS': None,
            'TARGET_CRS': None,
            'TARGET_EXTENT': None,
            'X_RESOLUTION': None,
            'Y_RESOLUTION': None,
            'OUTPUT': parameters[self.P_clip_raster]
        }
        outputs['ClipRasterByMaskLayer'] = processing.run('gdal:cliprasterbymasklayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results[self.P_clip_raster] = outputs['ClipRasterByMaskLayer']['OUTPUT']
        return results

    def name(self): return 'dataExtraction_clipRaster'
    def displayName(self): return 'dataExtraction_clipRaster'
    def group(self): return ''
    def groupId(self): return ''
    def createInstance(self): return Dataextraction_clipraster()

def runner_Dataextraction_clipraster(boundary_path, raster_path, clip_raster_path):
    params={
        Dataextraction_clipraster.P_boundary_map: boundary_path,
        Dataextraction_clipraster.P_raster_layer: raster_path,
        Dataextraction_clipraster.P_clip_raster: clip_raster_path
    }
    
    context = QgsProcessingContext()
    feedback = QgsProcessingFeedback()
    context.setProject(QgsProject.instance())
    
    alg = Dataextraction_clipraster()
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)
    print(f"Success: Saved to {clip_raster_path}")
    


### PIPELINE WORK ###

def run_pipeline(args):
    # 1. Initialize Paths
    input_path = Path(args.input_path)
    extraction_path = input_path
    region = args.region_name
    
    # 2. Define Input File Paths (Corrected based on your comments)
    # vector
    boundary_map_path = input_path / 'raw' / 'boundary_map' / f'{region}.geojson'
    landuse_vector_path = input_path / 'raw' / 'raw_shp' / region / 'gis_osm_landuse_a_free_1.shp'
    railway_vector_path = input_path / 'raw' / 'raw_shp' / region / 'gis_osm_transport_free_1.shp'
    road_vector_path = input_path / 'raw' / 'raw_shp' / region / 'gis_osm_roads_free_1.shp'
    dso_path = input_path / 'raw' / 'global' / "all_operators_dso.geojson"
    solar_path = input_path / 'raw' / 'global' / "all_centroid_solar.geojson"
    
    # raster
    dem_path = input_path / 'raw' / 'global' / 'DEM.tif'
    dni_path = input_path / 'raw' / 'global' / 'DNI.tif'
    temp_path = input_path / 'raw' / 'global' / 'TEMP.tif'
    pvout_path = input_path / 'raw' / 'global' / 'PVOUT.tif'
    
    # 3. Define Output File Paths
    fixgeometries_out = extraction_path / 'extraction' /region /  f'fixGeometries_{region}.geojson'
    fixgeometries_out_1 = extraction_path / 'extraction' /region /  f'fixGeometries_{region}_1.geojson'
    landuse_out = extraction_path / 'extraction' /region /  f'landUse_filter_{region}.geojson'
    railway_out = extraction_path / 'extraction' /region / f'railwayStation_filter_{region}.geojson'
    road_out = extraction_path / 'extraction' /region / f'roadVertices_filter_{region}.geojson'
    centroid_dso_out = extraction_path / 'extraction' /region /  f'centroid_dso_{region}.geojson'
    centroid_solar_out = extraction_path / 'extraction' /region /  f'centroid_solar_{region}.geojson'
    
    dem_out = extraction_path / 'extraction' /region / f'dem_clip_{region}.tif'
    dni_out = extraction_path / 'extraction' /region / f'dni_clip_{region}.tif'
    temp_out = extraction_path / 'extraction' /region / f'temp_clip_{region}.tif'
    pvout_out = extraction_path / 'extraction' /region / f'pvout_clip_{region}.tif'
    
    # 4. Step Validation Logic
    # Convert list of steps to set for O(1) lookup; default to steps 0-2
    # steps_to_run = set(args.steps) if args.steps and "all" not in args.steps else {"0", "1", "2"}
    
    # allow choosing steps (0..8) or 'all'
    steps_to_run = set()
    if args.steps:
        for s in args.steps:
            if s == "all":
                steps_to_run = set(map(str, range(0, 10)))
                break
            steps_to_run.add(str(s))
    else:
        steps_to_run = set(map(str, range(0, 10)))  # default: run all steps

    def should_run(output_path: Path, step_id: str, input_file: Path):
        if step_id not in steps_to_run: 
            return False
        if not input_file.exists():
            print(f"Error: Input file for Step {step_id} missing at {input_file}")
            return False
        return args.force or not output_path.exists()

    # --- EXECUTION STEPS ---
    
    ### runner vector 
    
    # Step 0: Fix geometries
    if should_run(fixgeometries_out, "0", boundary_map_path):
        fixgeometries_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 0: Fixing geometries boundary map → {fixgeometries_out}")
        runner_Dataextraction_fixgeometry(str(boundary_map_path), str(fixgeometries_out))
        # Usage:
        result = is_layer_valid(fixgeometries_out)
        if not is_layer_valid(fixgeometries_out):
            print("Validation failed. recomputing...")
            fixgeometries_out_1.parent.mkdir(parents=True, exist_ok=True)
            print(f"Recomputing process: Fixing geometries boundary map → {fixgeometries_out_1}")
            runner_Dataextraction_fixgeometry(str(fixgeometries_out), str(fixgeometries_out_1))
            # delete
            fixgeometries_out.unlink()
            #rename
            fixgeometries_out_1.rename(fixgeometries_out)
        else:
            pass
        
    # Step 1: Landuse
    if should_run(landuse_out, "1", landuse_vector_path):
        landuse_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 1: Extracting Landuse → {landuse_out}")
        runner_Dataextraction_landuse(str(boundary_map_path), str(landuse_vector_path), region, str(landuse_out))

    # Step 2: Railway
    if should_run(railway_out, "2", railway_vector_path):
        railway_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 2: Extracting Railway → {railway_out}")
        runner_Dataextraction_railwaystation(str(boundary_map_path), str(railway_vector_path), region, str(railway_out))

    # Step 3: Road Vertices
    if should_run(road_out, "3", road_vector_path):
        road_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Step 3: Extracting Road Vertices → {road_out}")
        runner_Dataextraction_roadvertices(str(boundary_map_path), str(road_vector_path), region, str(road_out))
        
    # Step 4: Get the DSO
    
    if should_run(output_path=centroid_dso_out, step_id="4", input_file= dso_path):
        centroid_dso_out.parent.mkdir(parents=True, exist_ok=True)
        print("Step 4: Extracting DSO centroid →", centroid_dso_out)
        runner_Dataextraction_clipvector(boundary_path=str(boundary_map_path), input_vector_path=str(dso_path), region_name =region, vector_clip_path=str(centroid_dso_out))
        
    # Step 5: Get the RES centroid
    if should_run(output_path=centroid_solar_out, step_id="5", input_file= solar_path):
        centroid_solar_out.parent.mkdir(parents=True, exist_ok=True)
        print("Step 5: Extracting Solar centroid →", centroid_solar_out)
        runner_Dataextraction_clipvector(boundary_path=str(boundary_map_path), input_vector_path=str(solar_path), region_name =region, vector_clip_path=str(centroid_solar_out))
        
    # Step 6: DEM Raster
    if should_run(dem_out, "6", dem_path):
        dem_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"step 6: DEM raster clip")
        runner_Dataextraction_clipraster(str(fixgeometries_out), str(dem_path), str(dem_out))
    
    # Step 7: DNI Raster
    if should_run(dni_out, "7", dni_path):
        dni_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"step 7: DNI raster clip")
        runner_Dataextraction_clipraster(str(fixgeometries_out), str(dni_path), str(dni_out))
    
    # Step 8: Temp Raster
    if should_run(temp_out, "8", temp_path):
        temp_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"step 8: TEMP raster clip")
        runner_Dataextraction_clipraster(str(fixgeometries_out), str(temp_path), str(temp_out))
    
    # Step 9: PVOUT Raster
    if should_run(pvout_out, "9", pvout_path):
        pvout_out.parent.mkdir(parents=True, exist_ok=True)
        print(f"step 9: PVOUT raster clip")
        runner_Dataextraction_clipraster(str(fixgeometries_out), str(pvout_path), str(pvout_out))
        

    print("Pipeline processing finished.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Extraction Pipeline")
    parser.add_argument("--steps", nargs="+", help='Steps to run (e.g., 0 1 or "all")')
    parser.add_argument("--input-path", type=str, required=True, help="Root input directory")
    parser.add_argument("--region-name", type=str, required=True, help="Name of the region (e.g., dolnoslaskie)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing output files")
    #parser.add_argument("--extraction-path", type=str, required=True, help="Root output directory")
    
    # 2. Programmatic execution for multiple regions
    # regions_list = [
    #     'dolnoslaskie', 'kujawsko_pomorskie', 'lodzkie', 'lubelskie', 
    #     'lubuskie', 'malopolskie', 'mazowieckie', 'opolskie',
    #     'podkarpackie', 'podlaskie', 'warminsko_mazurskie', 
    #     'wielkopolskie', 'zachodniopomorskie'
    # ]
    
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
            "--steps", "all"
        ])
        run_pipeline(simulated_args)
    
    # ## Standard execution via CLI
    # args = parser.parse_args()
    # run_pipeline(args)


# python dataExtraction.py \
#     --region-name dolnoslaskie \
#     --input-path "/Users/sell/SynologyDrive/Dataset/daina" \
#     --steps 4


