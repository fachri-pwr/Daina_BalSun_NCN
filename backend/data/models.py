from django.db import models
from django.contrib.gis.db import models

class Landuse(models.Model):
    # Change BigIntegerField to CharField because the DB sees it as text
    osm_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255, null=True, blank=True)
    fclass = models.CharField(max_length=255, null=True, blank=True)
    geometry = models.GeometryField(srid=4326,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True) # Add null=True
    class Meta:
        db_table = 'data_landuse'
        managed = True

class Box(models.Model):
    osm_box_id = models.CharField(primary_key=True, max_length=100,editable=True)
    left = models.FloatField()
    top = models.FloatField()
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    geometry = models.GeometryField(srid=4326,null=True, blank=True)
    region_name= models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True) # Add null=True
    class Meta:
        db_table = 'data_box'
        managed = True

class Dem(models.Model):
    osm_dem_id = models.CharField(primary_key=True, max_length=100)
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    _count = models.FloatField(null=True,blank=True)
    _sum= models.FloatField(null=True,blank=True)
    _mean = models.FloatField(null=True,blank=True)
    geometry = models.GeometryField(srid=4326, null=True, blank=True)
    region_name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True) # Add null=True
    class Meta:
        db_table = 'data_dem'
        managed = True

class Dni(models.Model):
    osm_dni_id = models.CharField(primary_key=True, max_length=100)
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    _count = models.FloatField(null=True,blank=True)
    _sum= models.FloatField(null=True,blank=True)
    _mean = models.FloatField(null=True,blank=True)
    geometry = models.GeometryField(srid=4326, null=True, blank=True)
    region_name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)  # Add null=True
    class Meta:
        db_table = 'data_dni'
        managed = True

class Pvout(models.Model):
    osm_pvout_id = models.CharField(primary_key=True, max_length=100)
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    _count = models.FloatField(null=True,blank=True)
    _sum= models.FloatField(null=True,blank=True)
    _mean = models.FloatField(null=True,blank=True)
    geometry = models.GeometryField(srid=4326, null=True, blank=True)
    region_name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)  # Add null=True
    class Meta:
        db_table = 'data_pvout'
        managed = True

class Temp(models.Model):
    osm_temp_id = models.CharField(primary_key=True, max_length=100)
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    _count = models.FloatField(null=True,blank=True)
    _sum= models.FloatField(null=True,blank=True)
    _mean = models.FloatField(null=True,blank=True)
    geometry = models.GeometryField(srid=4326, null=True, blank=True)
    region_name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)  # Add null=True
    class Meta:
        db_table = 'data_temp'
        managed = True

class CentroidBox(models.Model):
    osm_centroid_box_id = models.CharField(primary_key=True, max_length=100)
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    geometry = models.GeometryField(srid=4326, null=True, blank=True)
    region_name= models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)  # Add null=True
    class Meta:
        db_table = 'data_centroid_box'
        managed = True

class CentroidBox2Dso(models.Model):
    osm_box2dso_id = models.CharField(primary_key=True, max_length=100)
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    nearest_dso_id = models.IntegerField()
    nearest_dso_x = models.FloatField()
    nearest_dso_y = models.FloatField()
    distance_km = models.FloatField()
    score = models.FloatField()
    geometry = models.GeometryField(srid=4326, null=True, blank=True)
    region_name= models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)  # Add null=True
    class Meta:
        db_table = 'data_centroid_box2dso'
        managed = True

class CentroidBox2Plant(models.Model):
    osm_box2plant_id = models.CharField(primary_key=True, max_length=100)
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    nearest_plant_id = models.IntegerField()
    nearest_plant_x = models.FloatField()
    nearest_plant_y = models.FloatField()
    distance_km = models.FloatField()
    score = models.FloatField()
    geometry = models.GeometryField(srid=4326, null=True, blank=True)
    region_name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)  # Add null=True
    class Meta:
        db_table = 'data_centroid_box2plant'
        managed = True

class CentroidBox2Railway(models.Model):
    osm_box2railway_id = models.CharField(primary_key=True, max_length=100)
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    nearest_railway_id = models.IntegerField()
    nearest_railway_x = models.FloatField()
    nearest_railway_y = models.FloatField()
    distance_km = models.FloatField()
    score = models.FloatField()
    geometry = models.GeometryField(srid=4326, null=True, blank=True)
    region_name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)  # Add null=True
    class Meta:
        db_table = 'data_centroid_box2railway'
        managed = True

class CentroidBox2Road(models.Model):
    osm_box2road_id = models.CharField(primary_key=True, max_length=100)
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    x = models.FloatField()
    y = models.FloatField()
    nearest_road_id = models.IntegerField()
    nearest_road_x = models.FloatField()
    nearest_road_y = models.FloatField()
    distance_km = models.FloatField()
    score = models.FloatField()
    geometry = models.GeometryField(srid=4326, null=True, blank=True)
    region_name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)  # Add null=True
    class Meta:
        db_table = 'data_centroid_box2road'
        managed = True

class LandRatio(models.Model):
    osm_land_id = models.CharField(primary_key=True, max_length=100)
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    fid = models.IntegerField()
    osm_id = models.IntegerField()
    code = models.IntegerField()
    fclass = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)
    geometry = models.GeometryField(srid=4326, null=True, blank=True)
    area_2 = models.FloatField()
    perimeter_2 = models.FloatField()
    ratio = models.FloatField()
    region_name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)  # Add null=True
    class Meta:
        db_table = 'data_land_ratio'
        managed = True

class FinalScore(models.Model):
    osm_final_score_id = models.CharField(primary_key=True, max_length=100)
    left = models.FloatField()
    top = models.FloatField()
    right = models.FloatField()
    bottom = models.FloatField()
    row_index = models.IntegerField()
    col_index = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    #geometry = models.JSONField(blank=True, null=True)
    geometry = models.GeometryField(srid=4326,null=True, blank=True)
    land_score = models.FloatField()
    dso_score = models.FloatField()
    dso_score_distance_km = models.FloatField(null=True, blank=True)
    pv_score = models.FloatField()
    pv_score_distance_km = models.FloatField(null=True, blank=True)
    railway_score = models.FloatField(null=True, blank=True)
    railway_score_distance_km = models.FloatField(null=True, blank=True)
    road_score = models.FloatField()
    road_score_distance_km = models.FloatField(null=True, blank=True)
    dem_score = models.FloatField()
    dni_score = models.FloatField()
    temp_score = models.FloatField()
    pvout_score = models.FloatField()
    region_name = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)  # Add null=True
    class Meta:
        db_table = 'data_final_score'
        managed = True

class MapBoundary(models.Model):
    osm_map_id = models.CharField(primary_key=True, max_length=100)
    name=models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    geometry = models.GeometryField(srid=2180, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'data_map_boundary'
        managed = True

class Bazamocy(models.Model):
    osm_dso_id = models.CharField(primary_key=True, max_length=100)
    oddzial=models.CharField(max_length=100, blank=True, null=True)
    typ = models.CharField(max_length=100, blank=True, null=True)
    layer = models.CharField(max_length=100, blank=True, null=True)
    geometry = models.GeometryField(srid=2180, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'data_bazamocy'
        managed = True