from djgeojson.fields import PointField
from django.db import models

class MushroomSpot(models.Model):

	geom = PointField()
	description = models.TextField()

	@property
	def popupContent(self):
		return '<p>{}</p>'.format(
			self.description)
