from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import googlemaps
from vets.models import VetSpot

gmaps = googlemaps.Client(key='AIzaSyA0tl-yTrvyi_9UESPKQ27Ny4L0ONoktj8')

def index(request):
	return render_to_response('search_page.html', context_instance=RequestContext(request))

def search_by_place(request):

	keyw= ""
	loc = ""

	if request.method == 'POST':
		loc = request.POST.get('location', '')
		keyw = request.POST.get('what', '')
	geocode_result = gmaps.geocode(loc)
	lat = float(geocode_result[0]['geometry']['location']['lat'])
	lon = float(geocode_result[0]['geometry']['location']['lng'])	

	if keyw :
		search_result = gmaps.places( keyw, location=(lat,lon), types='veterinary_care', radius = 10000)
	else:
		search_result = gmaps.places( 'animal', location=(lat,lon), types='veterinary_care', radius = 10000)

	#return HttpResponse(search_result['results'])

	out = display_map_with_result(request, search_result, loc)
	return HttpResponse(out)


def locate_around_me(request, lat, lon):
	
	lat = float(lat)
	lon = float(lon)
	search_result = gmaps.places('animal', location=(lat,lon), types='veterinary_care', radius = 10000)
	reverse_geocode_result = gmaps.reverse_geocode((lat, lon))
	loc = reverse_geocode_result[0]['formatted_address']
	out = display_map_with_result(request, search_result, loc)
	return HttpResponse(out)


def display_map_with_result(request, search_result, place):
	vslist = []
	for r in search_result['results']:

		vs = VetSpot()
		vs.name = str(r['name'])
		vs.address = r['formatted_address']
		vs.latitude = r['geometry']['location']['lat']
		vs.longitude = r['geometry']['location']['lng']
		vs.place_id = r['place_id']

		if 'rating' in r.keys():
			vs.rating = r['rating']

		if 'opening_hours' in r.keys():
			if str(r['opening_hours']['open_now']).lower == "true":
				vs.opennow = True

		vslist.append(vs)

	return render(request, 'poi_list.html', {'pois': vslist, 'place': place})

def details(request, p_id):
	detail_result = gmaps.place(p_id)	
	return HttpResponse(str(detail_result['result']))