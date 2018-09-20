from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'request'
urlpatterns = [
    path('', views.RequestCreate.as_view(), name='request-create'),
]