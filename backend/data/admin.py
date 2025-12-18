from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from .models import *

class LanduseAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('name', 'fclass')
    search_fields = ('fclass',)
    # Optional: Set the default map settings
    default_zoom = 12
admin.site.register(Landuse,LanduseAdmin)

class BoxAdmin(gis_admin.GISModelAdmin):
    # This makes 'created' appear in the admin change form
    #readonly_fields = ('created',)
    # This makes 'created' appear in the list view (the table)
    list_display = ('osm_box_id', 'region_name','created')
    search_fields = ('osm_box_id', 'region_name','created')
    default_zoom = 12
admin.site.register(Box, BoxAdmin)

class DemAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('osm_dem_id', 'region_name','created')
    default_zoom = 12
admin.site.register(Dem,DemAdmin)

class DniAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('osm_dni_id', 'region_name','created')
    default_zoom = 12
admin.site.register(Dni,DniAdmin)

class TempAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('osm_temp_id', 'region_name','created')
    default_zoom = 12
admin.site.register(Temp,TempAdmin)

class PvoutAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('osm_pvout_id', 'region_name','created')
    default_zoom = 12
admin.site.register(Pvout,PvoutAdmin)

class CentroidBoxAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('osm_centroid_box_id', 'region_name','created')
    default_zoom = 12
admin.site.register(CentroidBox,CentroidBoxAdmin)

class CentroidBox2DsoAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('osm_box2dso_id', 'region_name','created')
    default_zoom = 12
admin.site.register(CentroidBox2Dso,CentroidBox2DsoAdmin)

class CentroidBox2PlantAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('osm_box2plant_id', 'region_name','created')
    default_zoom = 12
admin.site.register(CentroidBox2Plant,CentroidBox2PlantAdmin)

class CentroidBox2RailwayAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('osm_box2railway_id', 'region_name','created')
    default_zoom = 12
admin.site.register(CentroidBox2Railway,CentroidBox2RailwayAdmin)

class CentroidBox2RoadAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('osm_box2road_id', 'region_name','created')
    default_zoom = 12
admin.site.register(CentroidBox2Road,CentroidBox2RoadAdmin)

class LandRatioAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('osm_land_id', 'region_name','created')
    default_zoom = 12
admin.site.register(LandRatio,LandRatioAdmin)

class FinalScoreAdmin(gis_admin.GISModelAdmin):
    # This enables an OpenStreetMap background in the admin
    list_display = ('osm_final_score_id', 'region_name','created')
    default_zoom = 12
admin.site.register(FinalScore,FinalScoreAdmin)

class MapBoundaryAdmin(gis_admin.GISModelAdmin):
    list_display = ('name','category','created')
    default_zoom = 12
admin.site.register(MapBoundary,MapBoundaryAdmin)

class BazamocyAdmin(gis_admin.GISModelAdmin):
    list_display = ('oddzial','layer','created')
    default_zoom = 12
admin.site.register(Bazamocy,BazamocyAdmin)

