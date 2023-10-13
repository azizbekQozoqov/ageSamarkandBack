from django.urls import path
from .views import Index, MapAdminPage


urlpatterns = [
    path('', Index.as_view()),
    path('map-admin/', MapAdminPage.as_view())
]
