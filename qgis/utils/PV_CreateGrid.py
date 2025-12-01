# """
# Model exported as python (fixed to run in VS Code on macOS with QGIS-LTR).
# Name : model
# Group :
# With QGIS : 3.34 LTR
# """

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
    QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsProject
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

class Pv_creategrid(QgsProcessingAlgorithm):
    P_INPUT = "input_vector_layer"
    P_OUT = "CreategridResult"
    P_INPUT_CRS = 'input_crs'
    P_HSPACE = 'input_horizontal_spacing'
    P_VSPACE = 'input_vertical_spacing'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterCrs(self.P_INPUT_CRS , 'input crs', defaultValue='EPSG:4326'))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_INPUT, 'input vector layer', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterNumber(self.P_VSPACE, 'input vertical spacing', type=QgsProcessingParameterNumber.Double, defaultValue=None))
        self.addParameter(QgsProcessingParameterNumber(self.P_HSPACE, 'input horizontal spacing', type=QgsProcessingParameterNumber.Double, defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink(self.P_OUT, 'CreateGrid Result', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))

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
        outputs['CreateGrid'] = processing.run('native:creategrid', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Create spatial index
        alg_params = {
            'INPUT': outputs['CreateGrid']['OUTPUT']
        }
        outputs['CreateSpatialIndex'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Clip
        alg_params = {
            'INPUT': outputs['CreateSpatialIndex']['OUTPUT'],
            'OVERLAY': parameters['input_vector_layer'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Clip'] = processing.run('native:clip', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Add geometry attributes
        alg_params = {
            'CALC_METHOD': 0,  # Layer CRS
            'INPUT': outputs['Clip']['OUTPUT'],
            'OUTPUT': parameters['CreategridResult']
        }
        outputs['AddGeometryAttributes'] = processing.run('qgis:exportaddgeometrycolumns', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
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


# ===================================== runner ================================================

# -------------------------
# Standalone execution part
# -------------------------
if __name__ == "__main__":
    # Example inputs
    input_path = "../input/dolnoslaskie_boundary_v1.geojson"
    output_path = "../output/Grid_VSCODE.geojson"   # or "/tmp/clipped.shp"
    input_crs = "EPSG:2180"
    h_spacing = 1000.0
    v_spacing = 1000.0




    # Build parameter dict for the algorithm
    params = {
        Pv_creategrid.P_INPUT: input_path,
        Pv_creategrid.P_INPUT_CRS : QgsCoordinateReferenceSystem(input_crs),
        Pv_creategrid.P_HSPACE: h_spacing ,
        Pv_creategrid.P_VSPACE: v_spacing ,
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

    print("OK ->", result.get(Pv_creategrid.P_OUT))

    # Clean up QGIS
    # qgs.exitQgis()