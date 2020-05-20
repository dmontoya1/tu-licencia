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


MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
FILE_UPLOAD_PERMISSIONS = 0o644

EMAIL_ADMIN = 'gerencia@tulicencia.co'

# aws settings
AWS_LOCATION = 'static'
AWS_ACCESS_KEY_ID = 'AKIATUFK4SRUQNRWJPON'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'tulicencia'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_DEFAULT_ACL = None
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# s3 static settings
STATIC_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = "tulicencia.settings.storage_backends.StaticStorage"

# S3 media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, PUBLIC_MEDIA_LOCATION)
DEFAULT_FILE_STORAGE = 'tulicencia.settings.storage_backends.MediaStorage'

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.FileSystemFinder',    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                       )
