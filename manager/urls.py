

from django.urls import path, include

from . import views

app_name = 'manager'
urlpatterns = [
    path('terms-and-conditions/', views.TermsAndConditions.as_view(), name='terms-and-conditions'),
    path('privacy-policies/', views.PrivacyPolicies.as_view(), name='privacy-policies'),
    path('states/', views.StateList.as_view(), name='states'),
    path('city/<int:stateId>/', views.CityList.as_view(), name='cities'),
]