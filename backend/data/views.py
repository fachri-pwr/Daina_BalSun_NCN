import json
from django.http import StreamingHttpResponse
from rest_framework import viewsets, permissions,pagination
from rest_framework.response import Response
from django.db.models import F
from .models import *
from .serializers import *
from .utils import sanitize_for_json


class StandardResultsSetPagination(pagination.LimitOffsetPagination):
    default_limit = 1000  # Number of rows per chunk
    max_limit = 5000     # Maximum the frontend can request

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    pagination_class = StandardResultsSetPagination # Enable pagination

    def get_queryset(self):
        # Using .only() or .defer() here can also speed up the query
        # by not loading heavy fields you don't need immediately
        queryset = Box.objects.all()
        region_filter = self.request.query_params.get('region_name', None)
        if region_filter:
            queryset = queryset.filter(region_name__iexact=region_filter)
        return queryset


class MapBoundaryViewSet(viewsets.ModelViewSet):
    # Use the queryset directly here
    queryset = MapBoundary.objects.all()
    serializer_class = MapBoundarySerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        # 1. Start with all objects
        queryset = MapBoundary.objects.all()

        # 2. Get the category from URL params
        category_filter = self.request.query_params.get('category', None)

        if category_filter:
            # FIXED: Changed 'region_name' to 'category' to match your model
            queryset = queryset.filter(category__iexact=category_filter)

        return queryset

# working with dso point in bazamocy
class BazamocyViewSet(viewsets.ModelViewSet):
    # Use the queryset directly here
    queryset = Bazamocy.objects.all()
    serializer_class = BazamocySerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        # 1. Start with all objects
        queryset = Bazamocy.objects.all()

        # 2. Get the category from URL params
        layer_filter = self.request.query_params.get('layer', None)

        if layer_filter:
            # FIXED: Changed 'region_name' to 'category' to match your model
            queryset = queryset.filter(layer__iexact=layer_filter)

        return queryset

class DemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dem.objects.all()
    serializer_class = DemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            sanitized = sanitize_for_json(serializer.data)
            return self.get_paginated_response(sanitized)

        serializer = self.get_serializer(queryset, many=True)
        sanitized = sanitize_for_json(serializer.data)
        return Response(sanitized)

