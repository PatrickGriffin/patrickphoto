import os
from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = True

DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Static asset configuration
# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = 'mediafiles'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
     os.path.join(BASE_DIR, "static_in_pro", "our_static"),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'