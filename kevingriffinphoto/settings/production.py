import os
from django.conf import settings
from custom_storages import StaticStorage, MediaStorage

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['calm-ocean-6555.herokuapp.com']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Static asset configuration
# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_ROOT = 'staticfiles'
#MEDIA_ROOT = 'mediafiles'

#STATIC_URL = '/static/'
#MEDIA_URL = '/media/'

STATICFILES_DIRS = (
     os.path.join(BASE_DIR, "static_in_pro", "our_static"),
)

# AWS_STORAGE_BUCKET_NAME = 'patrickgriffinphoto'
# AWS_ACCESS_KEY_ID = 'AKIAJPBE675RBH3RZJJQ'
# AWS_SECRET_ACCESS_KEY = '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'

    # Tell django-storages that when coming up with the URL for an item in S3 storage, keep
    # it simple - just use this domain plus the path. (If this isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
    # We also use it in the next setting.
#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    # This is used by the `static` template tag from `static`, if you're using that. Or if anything else
    # refers directly to STATIC_URL. So it's safest to always set it.
#STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

    # Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
    # you run `collectstatic`).
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'