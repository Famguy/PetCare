from djgeojson.fields import PointField
from django.db import models

class MushroomSpot(models.Model):

    geom = PointField()