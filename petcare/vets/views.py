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
	info = detail_result['result']	
	display_info = {}
	display_info['Name'] = info['name']
	display_info['Address'] = info['formatted_address']
	if 'formatted_phone_number' in info.keys():
		display_info['Phone'] = info['formatted_phone_number']
	if 'international_phone_number' in info.keys():
		display_info['International'] = info['international_phone_number']
	if 'opening_hours' in info.keys():
		display_info['Hours'] = info['opening_hours']		
	if 'permanently_closed' in info.keys():
		display_info['permanently_closed'] = info['permanently_closed']	
	if 'photos' in info.keys():
		display_info['photos'] = info['photos']	
	if 'price_level' in info.keys():
		display_info['expense'] = info['price_level']	
	if 'rating' in info.keys():
		display_info['rating'] = info['rating']	
	if 'reviews' in info.keys():
		display_info['reviews'] = info['reviews']
	if 'website' in info.keys():
		display_info['website'] = info['website']
	if 'vicinity' in info.keys():
		display_info['vicinity'] = info['vicinity']
	if 'url' in info.keys():
		display_info['url'] = info['url']
		
	return render(request, 'place_details.html', {'details': display_info})