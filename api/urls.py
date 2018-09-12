from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls

app_name = 'api'
urlpatterns = [
    path('jet/', include('jet.urls', namespace='jet'), name='jet'),  # Django JET URLS
    path('docs/', include_docs_urls(title='TuLicencia Apis', public=False)),
    path('admin/', admin.site.urls),
]