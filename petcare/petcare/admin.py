from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

admin.site.register(MushroomSpot, LeafletGeoAdmin)