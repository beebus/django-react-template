import os

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dev-key-for-testing-only'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, os.pardir, 'db.sqlite3'),
    }
}

INTERNAL_IPS = ['192.168.56.1', '127.0.0.1']

STATICFILES_DIRS.append(
    os.path.join(BASE_DIR, os.pardir, 'frontend', 'dist'),
)

STATIC_ROOT = os.path.join(BASE_DIR, os.pardir, 'staticfiles')
