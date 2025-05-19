from django.urls import path
from . import views

urlpatterns = [
    path("geolocation/", views.geolocation_all, name="geolocation_info_all"),
    path("geolocation/<str:address>", views.geolocation, name="geolocation_info"),
]
