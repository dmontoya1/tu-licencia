
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', namespace='jet'), name='jet'),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', namespace='jet-dashboard'), name='jet-dashboard'),
    path('reports/', include('reports.urls', namespace='reports'), name='reports'),
    path('api/', include('api.urls', namespace='api'), name='api'),
    path('payments/', include('payments.urls', namespace='payments'), name='payments'),
    path('', include('webclient.urls', namespace='webclient'), name='webclient'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)