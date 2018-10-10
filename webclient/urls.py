from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'webclient'
urlpatterns = [
    path('', views.Stepper.as_view(), name='stepper'),
    path('crc-detail', views.CRCDetail.as_view(), name='crc-detail'),
    path('cea-detail', views.CEADetail.as_view(), name='cea-detail'),
    path('transit-detail', views.TransitDetail.as_view(), name='transit-detail'),
    path('baucher/<int:pk>/request', views.BaucherView.as_view(), name='baucher-detail'),
]