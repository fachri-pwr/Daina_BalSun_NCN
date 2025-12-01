
"""
Model exported as python.
Name : PV_CreateCentroid
Group : 
With QGIS : 33414
"""

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

class Pv_createcentroid(QgsProcessingAlgorithm):
    P_INPUT = "input_vector_layer"
    P_OUT = "CentroidResult"
    P_INPUT_CRS = 'input_crs'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_INPUT, 'input vector layer', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterCrs(self.P_INPUT_CRS, 'input crs', defaultValue='EPSG:4326'))
        self.addParameter(QgsProcessingParameterFeatureSink(self.P_OUT, 'Centroid Result', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

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
        outputs['Centroids'] = processing.run('native:centroids', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

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
        outputs['ReprojectLayer'] = processing.run('native:reprojectlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

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
        outputs['AddXyFieldsToLayer'] = processing.run('native:addxyfields', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
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

# ===================================== runner ================================================
if __name__ == "__main__":
    # Example inputs
    input_path = "../output/Grid_VSCODE.geojson"
    output_path = "../output/Centroid_VSCODE.geojson"   
    input_crs = "EPSG:4326"

     # Build parameter dict for the algorithm
    params = {
        Pv_createcentroid.P_INPUT: input_path,
        Pv_createcentroid.P_INPUT_CRS : QgsCoordinateReferenceSystem(input_crs),
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

    print("Created Centroid Done ->", result.get(Pv_createcentroid.P_OUT))
