from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'vehicle'
urlpatterns = [
    path('vehicles/', views.VehicleList.as_view(), name='vehicle-list'),
]