from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'webclient'
urlpatterns = [
    path('', views.Stepper.as_view(), name='stepper')
    # path('jet/', include('jet.urls', namespace='jet'), name='jet'),  # Django JET URLS
    # path('admin/', admin.site.urls),
    # path('api/', include('api.urls', namespace='api'), name='api'),
]