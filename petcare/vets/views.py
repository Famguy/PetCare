from django.shortcuts import render
from django.http import HttpResponse
from googleplaces import GooglePlaces, types, lang

# Create your views here.
YOUR_API_KEY = ''

google_places = GooglePlaces(YOUR_API_KEY)

# You may prefer to use the text_search API, instead (text search vs radar vs nearby).
#keyword='',

def index(request):
	query_result = google_places.nearby_search(location='London, England', radius=20000, types=[types.TYPE_VETERINARY_CARE])
	output = ', '.join([str(place.name) for place in query_result.places])

	"""if query_result.has_attributions:
    	print query_result.html_attributions

    for place in query_result.places:
	    print place.name
	    print place.geo_location
	    print place.place_id
	    place.get_details()
	    print place.details 
	    print place.local_phone_number
	    print place.international_phone_number
	    print place.website
	    print place.url
	"""
	return HttpResponse(output)