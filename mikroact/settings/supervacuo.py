# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_STATIC = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MEDIA_ROOT = '/var/www/django/mikroact/shared/media/'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('..', '..', 'shared', 'mikroact.db'),
    }
}

INTERNAL_IPS = ('127.0.0.1',)
