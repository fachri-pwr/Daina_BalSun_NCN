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


class Pv_zonalstatistic(QgsProcessingAlgorithm):
    P_INPUT_VECTOR = "input_vector_layer"
    P_INPUT_RASTER = "input_raster_layer"
    P_OUT = 'ZonalStatisticResult'

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterRasterLayer(self.P_INPUT_RASTER, 'input raster layer', defaultValue=None))
        self.addParameter(QgsProcessingParameterVectorLayer(self.P_INPUT_VECTOR, 'input vector layer', types=[QgsProcessing.TypeVectorAnyGeometry], defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink(self.P_OUT, 'Zonal statistic result', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, supportsAppend=True, defaultValue=None))

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
        outputs['ClipRasterByMaskLayer'] = processing.run('gdal:cliprasterbymasklayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Zonal statistics
        alg_params = {
            'COLUMN_PREFIX': '_',
            'INPUT': parameters['input_vector_layer'],
            'INPUT_RASTER': outputs['ClipRasterByMaskLayer']['OUTPUT'],
            'RASTER_BAND': 1,
            'STATISTICS': [0,1,2],  # Count,Sum,Mean
            'OUTPUT': parameters['ZonalStatisticResult']
        }
        outputs['ZonalStatistics'] = processing.run('native:zonalstatisticsfb', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
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

# ===================================== runner ================================================

if __name__ == "__main__":
    # Example inputs
    input_vector_path = "../data/box.geojson"
    input_raster_path= '../data/DNI.tif'
    output_path = "../data/dni_zonal.geojson"   

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

