import json
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from data import models
from api.views import create_building_json
from django.http import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from data.models import Building, BuildingType
from data.form import ImageModelForm

# Create your views here.


class Index(View):
    def get(self, request, *args, **kwargs):
        buildings = models.Building.objects.all()
        data = []

        for i in buildings:
            data.append(i)

        context = {"data": data}
        return render(request, 'index.html', status=200, context=context)


class MapAdminPage(View):
    def get(self, request, *args, **kwargs):
        print(Building.objects.filter(id = 'way/168848628')[0].poly)
        buildings = models.Building.objects.all()
        all_building_types = models.BuildingType.objects.all()
        data = []

        for i in buildings:
            data.append(i)

        context = {"data": data, 'all_building_types':all_building_types}
        return render(request, 'admin.html', context=context)
    
    def post(sef, request: HttpRequest, *args, **kwargs):
        
        # req = request.body.decode("utf-8").split('&')
        building = Building.objects.filter(id = request.POST.get('id'))
        building_types = BuildingType.objects.filter(name = request.POST.get('type'))

        if not building:
            return JsonResponse({'success': False, 'message': 'Building was not found'})
        else:
            print(building[0].address)

                
            building[0].year=request.POST.get('year')  if request.POST.get('year') else building[0].year
            building[0].floors=request.POST.get('floors')  if request.POST.get('floors') else building[0].floors
            building[0].address= request.POST.get('address')  if request.POST.get('address') else building[0].address
            building[0].type=building_types[0]
            print(building[0].address)

            building[0].save()
            print(building[0])
        
            return HttpResponseRedirect('/map-admin/')
        
