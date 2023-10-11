import json
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, request

from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point, Polygon

from data.models import Building, BuildingType

# Create your views here.


def create_building_json(object: Building):
    obj = {
        "type": "Feature",
        "properties": {
            "@id": object.id,
            "year": object.year,
            "address": object.address,
            "floors": object.floors,
            # "floors": object.floors,
            "type": object.type.__str__()
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [object.poly.coords[0]]
        },
        "id": object.id,
        "success": True

    }

    return obj


class CreateBuilding(View):

    def post(self, request: request.HttpRequest, *args, **kwargs):
        
        body = json.loads(request.body)
        body_props = body['properties']

        building = Building.objects.filter(id=body_props['@id'])
        if building:
            return JsonResponse({'success': False, 'message':'Building already exist'})

        
        
        building_type = BuildingType.objects.all()[0]

        building = Building.objects.create(id=body_props['@id'], year=0, address=body_props['d_address'], type=building_type, poly=Polygon(body['geometry']['coordinates'][0])).save()

        # print(Building.objects.all())
        return JsonResponse({'success': True})


class GetBuilding(View):
    def get(self, request, lat: str, lan: str):
        query_set = Building.objects.filter(
            poly__distance_lte=(Point(float(lat), float(lan)), D(m=1)))
        if query_set:
            return JsonResponse(create_building_json(query_set[0]))
        else:
            return JsonResponse({'success': False, 'message': 'Building was not found'})

class UpdateBuilding(View):
    def post(self, request):
        body = json.loads(request.body)

        building = Building.objects.filter(id = body.get('id'))
        building_types = BuildingType.objects.all()

        if not building:
            return JsonResponse({'success': False, 'message': 'Building was not found'})
        else:
            building[0].year=body.get('year')  if body.get('year') else building[0].year
            building[0].floors=body.get('floors')  if body.get('floors') else building[0].floors
            building[0].address= body.get('address')  if body.get('address') else building[0].address
            building[0].type=building_types[0]

            building[0].save()
            
            return JsonResponse({'success': True, 'buildings':create_building_json(building[0])})

class GetAllBuildings(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'success': True, 'buildings': [create_building_json(i) for i in Building.objects.all()]})