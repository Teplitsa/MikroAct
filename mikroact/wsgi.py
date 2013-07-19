"""
WSGI config for mikroact project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys
import site

# remember original sys.path.
prev_sys_path = list(sys.path)

site.addsitedir('/usr/local/virtualenvs/mikroact/lib/python2.6/site-packages/')

# reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
	if item not in prev_sys_path:
		new_sys_path.append(item)
		sys.path.remove(item)

sys.path[:0] = new_sys_path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
		os.environ['DJANGO_SETTINGS_MODULE'] = environ['DJANGO_SETTINGS_MODULE']
		os.environ['SECRET_KEY'] = environ['SECRET_KEY']
		return _application(environ, start_response)

import os
