from .base import *

DEBUG = False

ALLOWED_HOSTS = ['www.solicitud.tulicencia.co', 'solicitud.tulicencia.co']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tulicencia',
        'USER': 'tulicencia',
        'PASSWORD': 'tulicencia-pass',
        'HOST': 'tulicencia.cgzekfotfrd1.us-east-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]
STATIC_ROOT = '/var/www/tulicencia/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/tulicencia/media/'
FILE_UPLOAD_PERMISSIONS = 0o644

EMAIL_ADMIN = 'tulicencia.apptitud@gmail.com'
