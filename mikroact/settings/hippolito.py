# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Carl van Tonder', 'carl@supervacuo.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('..', '..', 'shared', 'mikroact.db'),
    }
}

INTERNAL_IPS = ('127.0.0.1',)

ALLOWED_HOSTS = ('.mikroact.org',)
MEDIA_ROOT = '/var/www/django/mikroact/shared/media/'
