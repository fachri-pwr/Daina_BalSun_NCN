import os, sys

# --- QGIS paths (macOS QGIS-LTR) ---
# If you still get import errors, start VS Code with the QGIS env as described earlier.
sys.path.append("/Applications/QGIS-LTR.app/Contents/Resources/python")
sys.path.append("/Applications/QGIS-LTR.app/Contents/Resources/python/plugins")
sys.path.append("/Applications/QGIS-LTR.app/Contents/MacOS/lib/python3.9/site-packages")

# Environment (helps with Qt/GDAL/PROJ on some setups)
os.environ["QGIS_PREFIX_PATH"] = "/Applications/QGIS-LTR.app/Contents/MacOS"
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "/Applications/QGIS-LTR.app/Contents/PlugIns/platforms"
os.environ["GDAL_DATA"] = "/Applications/QGIS-LTR.app/Contents/Resources/gdal"
os.environ["PROJ_LIB"] = "/Applications/QGIS-LTR.app/Contents/Resources/proj"


from qgis.core import (
    QgsApplication, QgsVectorLayer, Qgis,
    QgsProcessing, QgsProcessingAlgorithm, QgsProcessingMultiStepFeedback,
    QgsProcessingParameterVectorLayer, QgsProcessingParameterFeatureSink,
    QgsProcessingParameterCrs, QgsProcessingParameterNumber,
    QgsProcessingContext, QgsProcessingFeedback,
    QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsProject,QgsProcessingParameterRasterLayer
)

# Initialize QGIS (headless)
QgsApplication.setPrefixPath("/Applications/QGIS-LTR.app/Contents/MacOS", True)
qgs = QgsApplication([], False)
qgs.initQgis()
print("QGIS:", Qgis.QGIS_VERSION)

# Init processing
import processing
from processing.core.Processing import Processing
Processing.initialize()
print("processing OK")

# ===================================== main code ================================================

class Pv_landuseratio(QgsProcessingAlgorithm):
    P_INPUT_BOX_GRID = "input_box_grid"
    P_INPUT_LAND_LAYER = "input_land_layer"
    P_OUT = 'LandUseScore'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_INPUT_BOX_GRID , 'input box grid', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer( self.P_INPUT_LAND_LAYER, 'input land layer', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink(self.P_OUT, 'land use score', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

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
        outputs['Intersection'] = processing.run('native:intersection', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Add geometry attributes
        alg_params = {
            'CALC_METHOD': 0,  # Layer CRS
            'INPUT': outputs['Intersection']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['AddGeometryAttributes'] = processing.run('qgis:exportaddgeometrycolumns', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

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
        outputs['FieldCalculator'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
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


# ===================================== runner ================================================

if __name__ == "__main__":
    # Example inputs
    input_box_grid_path = "../output/Grid_VSCODE.geojson"
    input_land_layer_path= '../input/landUsed-Lower Silesian.gpkg'
    output_path = "../output/LandScore_VSCODE.geojson"   

     # Build parameter dict for the algorithm
    params = {
        Pv_landuseratio.P_INPUT_BOX_GRID: input_box_grid_path ,
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
    alg =  Pv_landuseratio()
    # Normally the framework calls initAlgorithm; when running directly it's safe to call it once:
    alg.initAlgorithm()
    result = alg.processAlgorithm(params, context, feedback)

    print("calculated zonal statistic Done ->", result.get(Pv_landuseratio.P_OUT))

