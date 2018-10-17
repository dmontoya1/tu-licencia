from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'request'
urlpatterns = [
    path('', views.RequestCreate.as_view(), name='request-create'),
    path('validate-document/', views.ValidRequestDocument.as_view(), name='validate-document'),
    path('crc-pending/', views.CRCPendingRequestList.as_view(), name='crc-pending-requests'),
    path('cea-pending/', views.CEAPendingRequestList.as_view(), name='cea-pending-requests'),
]