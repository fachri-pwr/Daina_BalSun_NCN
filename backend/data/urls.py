from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoxViewSet, DemViewSet, MapBoundaryViewSet, BazamocyViewSet

app_name = "data"  # important if you include using namespace="data"

router = DefaultRouter()
router.register(r'box', BoxViewSet, basename='box')
router.register(r'dem', DemViewSet, basename='dem')
router.register(r'map', MapBoundaryViewSet, basename='map')
router.register(r'bazamocy', BazamocyViewSet, basename='bazamocy')

urlpatterns = [
    path('api/', include(router.urls)),
]
