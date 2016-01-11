from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from googleplaces import GooglePlaces, types, lang
import googlemaps
from vets.models import VetSpot

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

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def searchtomap(request):
	gmaps = googlemaps.Client(key='AIzaSyA0tl-yTrvyi_9UESPKQ27Ny4L0ONoktj8')
	search_result = gmaps.places('dogs', location=(19.3937262,72.7894004),types='veterinary_care', radius = 100)
	vslist = []
	print get_client_ip(request)
	for r in search_result['results']:
#		print r['name']
#		print r['geometry']['location']
#		print r['opening_hours']['open_now']
#		print r['formatted_address']
#		print r['formatted_phone_number']
		vs = VetSpot()
		vs.name = str(r['name'])
		vs.latitude = r['geometry']['location']['lat']
		vs.longitude = r['geometry']['location']['lng']
		vs.address = r['formatted_address']
		if 'opening_hours' in r.keys():
			if str(r['opening_hours']['open_now']).lower == "true":
				vs.opennow = True
#		vs.phone = r['formatted_phone_number']
#		vs.opennow = False
#		if str(r['opening_hours']['open_now']).lower == "true":
#			vs.opennow = True
		vslist.append(vs)
#	print search_result['results']

	return render(request, 'poi_list.html', {'pois': vslist})
