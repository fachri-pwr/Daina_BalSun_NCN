# ## old one

# class Dataextraction_landuse(QgsProcessingAlgorithm):
#     P_boundary_map = 'boundary_map'
#     P_landuse_vector = 'landuse_vector'
#     P_landuse_filter = 'landuse_filter'

#     def initAlgorithm(self, config=None):
#         self.addParameter(QgsProcessingParameterVectorLayer(
#             self.P_boundary_map, 'Boundary Map', [QgsProcessing.TypeVectorAnyGeometry]))
#         self.addParameter(QgsProcessingParameterVectorLayer(
#             self.P_landuse_vector, 'Landuse Vector', [QgsProcessing.TypeVectorAnyGeometry]))
#         self.addParameter(QgsProcessingParameterFeatureSink(
#             self.P_landuse_filter, 'Filtered Landuse Output', QgsProcessing.TypeVectorAnyGeometry))

#     def processAlgorithm(self, parameters, context, model_feedback):
#         feedback = QgsProcessingMultiStepFeedback(5, model_feedback)
#         results = {}
#         outputs = {}

#         # 1. Create spatial index landuse vector
#         alg_params = {'INPUT': parameters[self.P_landuse_vector]}
#         outputs['IndexLanduse'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

#         feedback.setCurrentStep(1)
#         if feedback.isCanceled(): return {}

#         # 2. Fix geometries
#         alg_params = {
#             'INPUT': parameters[self.P_boundary_map],
#             'METHOD': 0,
#             'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
#         }
#         outputs['FixGeoms'] = processing.run('native:fixgeometries', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

#         feedback.setCurrentStep(2)
#         if feedback.isCanceled(): return {}

#         # 3. Create spatial index boundary
#         alg_params = {'INPUT': outputs['FixGeoms']['OUTPUT']}
#         outputs['IndexBoundary'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

#         feedback.setCurrentStep(3)
#         if feedback.isCanceled(): return {}

#         # 4. Clip
#         alg_params = {
#             'INPUT': outputs['IndexLanduse']['OUTPUT'] if 'OUTPUT' in outputs['IndexLanduse'] else parameters[self.P_landuse_vector],
#             'OVERLAY': outputs['IndexBoundary']['OUTPUT'],
#             'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
#         }
#         outputs['Clip'] = processing.run('native:clip', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

#         feedback.setCurrentStep(4)
#         if feedback.isCanceled(): return {}

#         # 5. Extract by expression
#         alg_params = {
#             'EXPRESSION': '"fclass" IN (\'farmland\', \'farmyard\', \'grass\', \'heath\', \'meadow\', \'scrub\')',
#             'INPUT': outputs['Clip']['OUTPUT'],
#             'OUTPUT': parameters[self.P_landuse_filter]
#         }
#         outputs['Extract'] = processing.run('native:extractbyexpression', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        
#         results[self.P_landuse_filter] = outputs['Extract']['OUTPUT']
#         return results

#     def name(self): return 'dataExtraction_landuse'
#     def displayName(self): return 'Data Extraction Landuse'
#     def createInstance(self): return Dataextraction_landuse()
