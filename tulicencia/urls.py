
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', namespace='jet'), name='jet'),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api'), name='api'),
    path('', include('webclient.urls', namespace='webclient'), name='webclient'),
    path('payments/', include('payments.urls', namespace='payments'), name='payments'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)