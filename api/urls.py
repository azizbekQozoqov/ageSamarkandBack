from .views import GetBuilding, GetAllBuildings, CreateBuilding, UpdateBuilding, Tile
from django.urls import path


urlpatterns = [
    path('get_building/all/', GetAllBuildings.as_view()),
    path('get_building/<lat>/<lan>/', GetBuilding.as_view()),
    path('create_building/', CreateBuilding.as_view()),
    path('update_building/', UpdateBuilding.as_view()),
    path('<int:z>/<int:x>/<int:y>.png', Tile),
    path('<int:z>/<int:x>/<int:y>.png/<int:start>/<int:end>', Tile),
]
