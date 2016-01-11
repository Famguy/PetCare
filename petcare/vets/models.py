# Create your models here.

#from geoposition.fields import GeopositionField
from django.db import models

class VetSpot(models.Model):

	name = models.CharField(max_length=100)
	latitude = models.FloatField()
	longitude = models.FloatField()
	address = models.TextField()
#	phone = models.TextField()
#	opennow = models.BooleanField()


	class Meta:
		verbose_name_plural = 'vet spots'

