# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mikroact',
        'USER': 'postgres',
        'PASSWORD': None,
        'HOST': '',
        'PORT': '',
    }
}