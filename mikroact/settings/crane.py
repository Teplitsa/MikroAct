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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('..', '..', 'shared', 'mikroact.db'),
    }
}

INTERNAL_IPS = ('127.0.0.1',)

EMAIL_PORT = 1025
