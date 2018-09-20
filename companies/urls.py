from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'companies'
urlpatterns = [
    path('cea', views.CeaList.as_view(), name='cea-list'),
]