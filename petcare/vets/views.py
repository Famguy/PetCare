from django.shortcuts import render
from django.http import HttpResponse
from googleplaces import GooglePlaces, types, lang

# Create your views here.
YOUR_API_KEY = 'AIzaSyAv52Som47-ps4IOblaZsMWOWB0h8p2mfg'

google_places = GooglePlaces(YOUR_API_KEY)

# You may prefer to use the text_search API, instead (text search vs radar vs nearby).

def index(request):
	return HttpResponse("Shortly open for search")

def search(request):
	query_result = google_places.nearby_search(location='London, England', keyword='dogs', radius=20000, types=[types.TYPE_VETERINARY_CARE])
	output = ', '.join([str(place.name) for place in query_result.places])
	return HttpResponse(output)

def map(request):
	return HttpResponse("map plotting tryout")