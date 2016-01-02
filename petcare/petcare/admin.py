from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from petcare.models import MushroomSpot

admin.site.register(MushroomSpot, LeafletGeoAdmin)