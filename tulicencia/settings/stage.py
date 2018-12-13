from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tulicencia',
        'USER': 'dev',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_ROOT = '/var/www/tulicencia/static/'
MEDIA_ROOT = '/var/www/tulicencia/media/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]



MEDIA_ROOT = 'media'

EMAIL_ADMIN = 'tulicencia.apptitud@gmail.com'