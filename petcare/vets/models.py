# Create your models here.

from djgeojson.fields import PointField
from django.db import models

class VetSpot(models.Model):

	geom = PointField()
	description = models.TextField()
