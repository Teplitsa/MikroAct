# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from os import environ
from os.path import join, abspath, dirname

ugettext = lambda s: s

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

# .. as, hopefully, is global_settings -- see:
#   http://blog.madpython.com/2010/04/07/django-context-processors-best-practice/
import django.conf.global_settings as DEFAULT_SETTINGS


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)

here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..", "..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

# Local time zone for this installation.
TIME_ZONE = 'America/New_York'

# Language code for this installation.
#LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en-us', 'English (US)'),
    ('ru', 'Russian'),
    ('xx', 'XX')
)
LOCALE_PATHS = (root('locale'),)

USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 1

MEDIA_URL = '/media/'
MEDIA_ROOT = root('media')

STATIC_URL = '/static/'
STATIC_ROOT = root('collected_static')
STATICFILES_DIRS = (
    root('mikroact', 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
SERVE_STATIC = True

TEMPLATE_DIRS = (
    root('mikroact', 'templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'mikroact.context.stream',
)

SECRET_KEY = get_env_variable("SECRET_KEY")

ROOT_URLCONF = 'mikroact.urls'

WSGI_APPLICATION = 'mikroact.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'bootstrap_toolkit',
    'south',
    'acts',
    'accounts',
    'guardian',
    'stream',
    'follow',
    'fluent_comments',
    'crispy_forms',
    'django.contrib.comments',
    'micawber.contrib.mcdjango'
)

STREAM_VERBS = (
    ('default', ugettext('Stream Item')),
    ('edited', ugettext('edited')),
    ('created', ugettext('created')),
    ('deleted', ugettext('deleted')),
    ('followed', ugettext('followed')),
    ('commented', ugettext('left a comment')),  # ".. on"
    ('added', ugettext('added')),  # ".. to"
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTHENTICATION_BACKENDS = (
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)
AUTH_PROFILE_MODULE = 'accounts.UserProfile'
ANONYMOUS_USER_ID = -1
DEFAULT_PERMISSIONS = [
    # users can always change & delete their own content...
    'acts.add_mikroact',
    'acts.add_campaign',
    'accounts.add_collective',
]

LOGIN_URL = '/user/login/'
LOGOUT_URL = '/user/logout/'
LOGIN_REDIRECT_URL = '/'

FLUENT_COMMENTS_EXCLUDE_FIELDS = ('name', 'email', 'url')
COMMENTS_APP = 'fluent_comments'
