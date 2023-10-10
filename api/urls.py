from .views import GetBuilding, GetAllBuildings, CreateBuilding, UpdateBuilding
from django.urls import path


urlpatterns = [
    path('get_building/all/', GetAllBuildings.as_view()),
    path('get_building/<lat>/<lan>/', GetBuilding.as_view()),
    path('create_building/', CreateBuilding.as_view()),
    path('update_building/', UpdateBuilding.as_view()),
]
