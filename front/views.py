from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from data import models
from api.views import create_building_json

# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        buildings = models.Building.objects.all()
        data = []
    
        for i in buildings:
            data.append(i)


        context = {"data": data}
        return render(request, 'index.html', status=200, context=context)