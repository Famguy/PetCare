from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from googleplaces import GooglePlaces, types, lang
import googlemaps
from vets.models import VetSpot
import json

# Create your views here.
YOUR_API_KEY = 'AIzaSyAv52Som47-ps4IOblaZsMWOWB0h8p2mfg'
google_places = GooglePlaces(YOUR_API_KEY)

# You may prefer to use the text_search API, instead (text search vs radar vs nearby).

def index(request):
	return render_to_response('search_page.html', context_instance=RequestContext(request))
	#return HttpResponse("Shortly open for search")

def search(request):
	keyw= ""
	loc = ""

	if request.method == 'POST':
		loc = request.POST.get('location', '')
		keyw = request.POST.get('what', '')
	query_result = google_places.nearby_search(location=loc, keyword=keyw, radius=20000, types=[types.TYPE_VETERINARY_CARE])
	#a working search-
	#query_result = google_places.nearby_search(location='London, England', keyword='dogs', radius=20000, types=[types.TYPE_VETERINARY_CARE])
	output = ', '.join([str(place.name) for place in query_result.places])
	print output
	return HttpResponse(output)

def map(request):
	gmaps = googlemaps.Client(key='AIzaSyA0tl-yTrvyi_9UESPKQ27Ny4L0ONoktj8')
	search_result = gmaps.places('dogs', location='London, England',types='veterinary_care',radius=20000)
	print search_result
	return HttpResponse(search_result)

def searchtomap(request):
	gmaps = googlemaps.Client(key='AIzaSyA0tl-yTrvyi_9UESPKQ27Ny4L0ONoktj8')
	search_result = gmaps.places('dogs', location=(-33.86746, 151.207090),types='veterinary_care', radius = 100)
	vslist = []
	for r in search_result['results']:
#		print r['name']
#		print r['geometry']['location']
#		print r['opening_hours']['open_now']
#		print r['formatted_address']
#		print r['rating']
		vs = VetSpot()
		vs.geom = { "type":"Point", "coordinates":[r['geometry']['location']['lat'], r['geometry']['location']['lng']] }
		vs.description = str(r['name'])
		print vs.geom
		print vs.description
		vslist.append(vs)
	print vslist

	return render(request, 'index.html', {'mushroomspot': vslist})

