from rest_framework import serializers
from .models import *

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'  # or list fields explicitly: ['id', 'score', 'user', ...]

class DemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dem
        fields = '__all__'

class MapBoundarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MapBoundary
        fields = '__all__'

class BazamocySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bazamocy
        fields = '__all__'

