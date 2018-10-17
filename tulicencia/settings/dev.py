from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tulicencia',
    }
}

STATIC_ROOT = 'static'
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static")
]

MEDIA_ROOT = 'media'

EMAIL_ADMIN = 'dmontoya@apptitud.com.co'