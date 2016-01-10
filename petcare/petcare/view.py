from django.shortcuts import render
from django.template import RequestContext
from petcare.models import MushroomSpot

def home(request):

	
	mushroomspot = MushroomSpot.objects.all()
	ms_geom = {
  "type":"Point",
  "coordinates":[
 -33, 150
  ]
}
	ms_desp = "haha"
	ms = MushroomSpot()
	ms.geom = ms_geom
	ms.description = ms_desp
#	qs = MushroomSpot.objects.filter(id__in=custom_list)

	for i in mushroomspot:
		print i.geom
		print i.description
	return render(request, 'index.html', {'mushroomspot': mushroomspot})