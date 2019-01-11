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

STATIC_ROOT = '/var/www/tulicencia/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]


MEDIA_ROOT = '/var/www/tulicencia/media/'
MEDIA_URL = '/media/'
FILE_UPLOAD_PERMISSIONS = 0o644

MEDIA_ROOT = 'media'

EMAIL_ADMIN = 'tulicencia.apptitud@gmail.com'