from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'companies'
urlpatterns = [
    path('cea', views.CeaList.as_view(), name='cea-list'),
    path('crc', views.CrcList.as_view(), name='crc-list'),
    path('transit', views.TransitList.as_view(), name='transit-list'),
]