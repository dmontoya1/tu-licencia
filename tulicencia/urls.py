
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', namespace='jet'), name='jet'),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api'), name='api'),
]
