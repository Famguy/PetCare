from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from googleplaces import GooglePlaces, types, lang
import googlemaps

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
		#keyw = request.POST.get('what', '')
	query_result = google_places.nearby_search(location='London, England', keyword='dogs', radius=20000, types=[types.TYPE_VETERINARY_CARE])
	output = ', '.join([str(place.name) for place in query_result.places])
	return HttpResponse(output)

def map(request):
	gmaps = googlemaps.Client(key='AIzaSyA0tl-yTrvyi_9UESPKQ27Ny4L0ONoktj8')
	search_result = gmaps.places('dogs', location='London, England',types='veterinary_care')
	return HttpResponse("google map plotting tryout")