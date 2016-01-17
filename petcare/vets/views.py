from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from googleplaces import GooglePlaces, types, lang
import googlemaps
from vets.models import VetSpot

YOUR_API_KEY = 'AIzaSyAv52Som47-ps4IOblaZsMWOWB0h8p2mfg'
google_places = GooglePlaces(YOUR_API_KEY)

def index(request):
	return render_to_response('search_page.html', context_instance=RequestContext(request))

def search_by_place(request):
	keyw= ""
	loc = ""

	if request.method == 'POST':
		loc = request.POST.get('location', '')
		keyw = request.POST.get('what', '')
	query_result = google_places.nearby_search(location=loc, keyword=keyw, radius=20000, types=[types.TYPE_VETERINARY_CARE])
	output = ', '.join([str(place.name) for place in query_result.places])
	print output
	return HttpResponse(output)

def locate_around_me(request, lat, lon):
	gmaps = googlemaps.Client(key='AIzaSyA0tl-yTrvyi_9UESPKQ27Ny4L0ONoktj8')
	lat = float(lat)
	lon = float(lon)
	search_result = gmaps.places('animal', location=(lat,lon), types='veterinary_care', radius = 10000)
	vslist = []
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

