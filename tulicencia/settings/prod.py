from .base import *

DEBUG = False

ALLOWED_HOSTS = ['www.solicitud.tulicencia.co', 'solicitud.tulicencia.co']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tulicencia',
        'USER': 'tulicencia',
        'PASSWORD': '&CbzVNaCcVz*!Bft6yxf',
        'HOST': 'tulicencia.cwbqx3olxwaw.us-east-1.rds.amazonaws.com',
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

EMAIL_ADMIN = 'gerencia@tulicencia.co'
