from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls

app_name = 'api'
urlpatterns = [
    path('jet/', include('jet.urls', namespace='jet'), name='jet'),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('manager/', include('manager.urls', namespace='manager'), name='manager'),
    path('request/', include('request.urls', namespace='request'), name='request'),
    path('vehicles/', include('vehicles.urls', namespace='vehicles'), name='vehicles'),
    path('companies/', include('companies.urls', namespace='companies'), name='companies'),
    path('users/', include('users.urls', namespace='users'), name='users'),
]