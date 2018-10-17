from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'companies'
urlpatterns = [
    path('cea', views.CeaList.as_view(), name='cea-list'),
    path('crc', views.CrcList.as_view(), name='crc-list'),
    path('transit', views.TransitList.as_view(), name='transit-list'),
    path('disable-crc', views.DisableCrcRequest.as_view(), name='disable-crc'),
    path('disable-cea', views.DisableCeaRequest.as_view(), name='disable-cea'),
    path('enable-crc', views.EnableCrcRequest.as_view(), name='enable-crc'),
    path('enable-cea', views.EnableCeaRequest.as_view(), name='enable-cea'),
]