
from django.urls import path, include

from . import views


app_name = 'reports'
urlpatterns = [
    path('purchase/', views.Purchases.as_view(), name='purchases'),
    path('purchases/', views.PurchaseApi.as_view(), name='purchase-api'),
    path('credit/', views.Credits.as_view(), name='credits'),
    path('credits/', views.CreditsApi.as_view(), name='credit-api'),
    path('service/', views.ServicesByCompany.as_view(), name='services'),
    path('services-api/', views.ServicesByCompanyApi.as_view(), name='services-api'),
    path('cea/', views.CeaServices.as_view(), name='cea'),
    path('cea-api/', views.CeaServicesApi.as_view(), name='cea-api'),
    path('crc/', views.CeaServices.as_view(), name='crc'),
    path('crc-api/', views.CrcServicesApi.as_view(), name='crc-api'),
    
]