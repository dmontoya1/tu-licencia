from .base import *

DEBUG = False

ALLOWED_HOSTS = ['http://3.16.156.133/', '3.16.156.133']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tulicencia',
        'USER': 'tulicencia',
        'PASSWORD': 'tulicencia-pass',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'tulicencia/static'),
]
STATIC_ROOT = '/var/www/tulicencia/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/tulicencia/media/'
FILE_UPLOAD_PERMISSIONS = 0o644

MEDIA_ROOT = 'media'

EMAIL_ADMIN = 'tulicencia.apptitud@gmail.com'