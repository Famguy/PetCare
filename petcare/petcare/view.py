from django.shortcuts import render
from django.template import RequestContext
from petcare.models import MushroomSpot

def home(request):
	mushroomspot = MushroomSpot.objects.all()
	print mushroomspot
	return render(request, 'index.html', {'mushroomspot': mushroomspot})