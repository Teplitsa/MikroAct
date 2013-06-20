# vim: fileencoding=utf-8 ai ts=4 sts=4 et sw=4
from __future__ import with_statement
from contextlib import contextmanager as _contextmanager
from datetime import datetime
import os
from tempfile import mkdtemp

from fabric.api import *
from fabric.contrib import console
from fabric.contrib import files


HOSTS = {
    'crane': (
        ['192.168.122.22', ],
        '/var/www/django/'
    ),
    'supervacuo': (
        ['supervacuo.com', ],
        '/var/www/django/'
    ),
    'hippolito': (
        ['hippolito.supervacuo.com', ],
        '/var/www/django/'
    ),
}

env.project_name = "mikroact"
env.virtual_env = "/usr/local/virtualenvs/mikroact"
env.tmp_dir = mkdtemp()


@_contextmanager
def virtualenv():
    if files.exists(env.virtual_env):
        with prefix('source ' + os.path.join(env.virtual_env, 'bin', 'activate')):
            yield
    else:
        # fall back to per-user virtualenv for local activities
        with prefix('source ~/.virtualenvs/%s/bin/activate' % env.project_name):
            yield


def _check_for_bin(executable, abort_if_not_found=False):
    with settings(hide('warnings', 'running', 'stdout', 'stderr'),
                  warn_only=True,):
        result = run('which %s' % executable)

    if result.succeeded or not abort_if_not_found:
        return result.succeeded

    abort("`%s` not available on the remote host" % executable)


def _package(branch_name, filename):
    local('git archive --format tar %s | gzip > %s' % (branch_name, filename))
    return filename


def host(host_key):
    try:
        env.hosts = HOSTS[host_key][0]
        env.path = HOSTS[host_key][1]
        env.host_name = host_key
    except KeyError:
        abort("Host '%s' not found. Options are: %s" % (host_key, HOSTS.keys()))


def manage(args):
    require('hosts', provided_by=[host])
    require('path')

    with virtualenv():
        sudo('SECRET_KEY="notsosecret" django-admin.py %s --settings=mikroact.settings.%s --pythonpath=%s' % (
            args, env.host_name, os.path.join(env.path, env.project_name, 'releases', 'current')
        ))


def test():
    with settings(
        hide('warnings', 'running', 'stdout', 'stderr'),
        warn_only=True
    ):
        result = local("django-admin.py test farm")

    if result.succeeded:
        return True

    return False


def setup():
    require('hosts', provided_by=[host])
    require('path')

    _check_for_bin('virtualenv', True)

    if not files.exists(env.virtual_env):
        # this will fail if `dirname env.virtual_env` doesn't exist
        sudo('cd `dirname %s` && virtualenv --distribute --no-site-packages `basename %s`' % (env.virtual_env, env.virtual_env))

    with virtualenv():
        _check_for_bin('pip', True)

    if not files.exists(os.path.join(env.path, env.project_name)):
        sudo('mkdir %s' % os.path.join(env.path, env.project_name))

    with cd(os.path.join(env.path, env.project_name)):
        sudo('mkdir packages releases shared')


def deploy(release_name=None):
    require('hosts', provided_by=[host])
    require('tmp_dir')
    require('path')

    with settings(hide('warnings', 'running', 'stdout', 'stderr'),
                  warn_only=True,):
        branch_name = local('git rev-parse --abbrev-ref HEAD', capture=True)
    if not branch_name.succeeded:
        abort("Branch name `%s` appears to be invalid" % branch_name)

    if not release_name:
        with settings(hide('warnings', 'running', 'stdout', 'stderr'),
                      warn_only=True,):
            release_name = local('git rev-parse %s' % branch_name, capture=True)[:8]

    filename = '%s_%s_%s.tar.gz' % (
        env.project_name,
        release_name,
        datetime.now().strftime('%Y-%m-%dT%H%M%S')
    )
    package = _package(branch_name, os.path.join(env.tmp_dir, filename))

    project_root = os.path.join(env.path, env.project_name)
    package_root = os.path.join(project_root, 'packages')
    release_root = os.path.join(project_root, 'releases', release_name)

    if files.exists(release_root):
        warn("Release directory `%s` already exists on %s" % (release_root, env.hosts))
    else:
        sudo('mkdir %s' % release_root)

    put(package, package_root, True)
    local('rm -r %s' % env.tmp_dir)

    with cd(release_root), settings(hide('warnings', 'stdout')):
        sudo('tar -xzf %s' % os.path.join(package_root, filename))

    with cd(os.path.join(project_root, 'releases')):
        with settings(hide('stdout', 'stderr'), warn_only=True):
            sudo('rm -f previous')
            sudo('mv current previous')
        sudo('ln -s %s current' % release_name)

    with cd(release_root), virtualenv():
        sudo('pip install -q -r requirements.txt')

    manage('collectstatic --noinput -v0')
    manage('syncdb --noinput --migrate')

    with cd(project_root):
        sudo('chown -R apache:apache *')
