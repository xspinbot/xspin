import os
from data.config import DjangoSettings
from data.config import BASE_DIR

django = DjangoSettings()

SECRET_KEY = django.secret_key
DEBUG = django.debug

ALLOWED_HOSTS = django.allowed_hosts_list

CSRF_TRUSTED_ORIGINS = django.csrf_trusted_origins_list

ROOT_URLCONF = 'conf.urls'
WSGI_APPLICATION = 'conf.wsgi.application'

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

