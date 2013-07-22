# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from .base import *
#Set to change language locale
#LANGUAGE_CODE="ru"
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mikroact.db',
    }
}

INTERNAL_IPS = ('127.0.0.1',)

EMAIL_PORT = 1025

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}
