from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'companies'
urlpatterns = [
    path('cea', views.CeaList.as_view(), name='cea-list'),
    path('crc', views.CrcList.as_view(), name='crc-list'),
    path('transit', views.TransitList.as_view(), name='transit-list'),
    path('cea-list', views.CeaCityList.as_view(), name='cea-city-list'),
    path('crc-list', views.CrcCityList.as_view(), name='crc-city-list'),
    path('transit-list', views.TransitCityList.as_view(), name='transit-city-list'),
    path('disable-crc', views.DisableCrcRequest.as_view(), name='disable-crc'),
    path('disable-cea', views.DisableCeaRequest.as_view(), name='disable-cea'),
    path('enable-crc', views.EnableCrcRequest.as_view(), name='enable-crc'),
    path('enable-cea', views.EnableCeaRequest.as_view(), name='enable-cea'),
    path('crc/<int:pk>', views.CRCDetail.as_view(), name='crc-detail'),
    path('cea/<int:pk>', views.CEADetail.as_view(), name='cea-detail'),
    path('transit/<int:pk>', views.TransitDetail.as_view(), name='transit-detail'),
    path('rating/cea/<int:pk>', views.CeaRatingCreate.as_view(), name='cea-rating'),
    path('rating/crc/<int:pk>', views.CrcRatingCreate.as_view(), name='crc-rating'),
    path('rating/transit/<int:pk>', views.TransitRatingCreate.as_view(), name='transit-rating'),
]