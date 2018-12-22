from .base import *

DEBUG = True

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
MEDIA_ROOT = '/var/www/tulicencia/media/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]


MEDIA_ROOT = 'media'

EMAIL_ADMIN = 'tulicencia.apptitud@gmail.com'