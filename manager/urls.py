from django.conf.urls import url, include
from django.contrib import admin

from . import views

app_name = 'manager'
urlpatterns = [
    url(r'^terms-and-conditions/$', views.TermsAndConditions.as_view(), name='terms-and-conditions'),
    url(r'^privacy-policies/$', views.PrivacyPolicies.as_view(), name='privacy-policies'),
    url(r'^states/$', views.StateList.as_view(), name='list-states'),
    url(r'^city/(?P<stateId>.*)/$', views.CityList.as_view(), name='list-cities'),
    url(r'^location/$', views.GetLocation.as_view(), name='get-location'),
    url(r'^update-location/(?P<pk>[0-9]+)/$', views.UpdateLocation.as_view(), name='update-location'),
    url(r'^notifications/$', views.NotificationHistoryList.as_view(), name='notifications-list'),
    url(r'^upload-csv/$', views.process_xlsx, name='upload_csv'),
]