from django.contrib import admin
from .models import Building, BuildingType
from osgeo import gdal

# Register your models here.
admin.site.register([Building, BuildingType])