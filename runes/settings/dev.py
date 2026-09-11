from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ENABLE_DEBUG_TOOLBAR = True

# SECURITY WARNING: define the correct hosts in production!
# ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('DB_LOCAL_NAME'),
        'USER': os.getenv('DB_LOCAL_USER'),
        'PASSWORD': os.getenv('DB_LOCAL_PASS'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

