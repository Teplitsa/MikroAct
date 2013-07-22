MikroAct
========

Private repository for the MikroAct project.

Getting started
--------

1. Install dependencies:
    * Python 2.5-2.7 with [pip](http://www.pip-installer.org/en/latest/)

2. Check out code and create local configuration:
    
        $ git clone git@github.com:Teplitsa/MikroAct.git
        ...
        $ cd MikroAct.git
        $ pip install -r deployment/requirements.txt
        ...

3. If you need to change default settings (such as database connection details),
   copy `mikroact/settings/local.py` to a version suffixed with your name, like
   `mikroact/settings/local_dan.py`, and edit as appropriate.

4. Set required environment variables:

        $ export PYTHONPATH=$PYTHONPATH:$PWD
        $ export DJANGO_SETTINGS_MODULE='mikroact.settings.local_dan'
        $ export SECRET_KEY='A passphrase of your choosing'
   You could save these commands as a script, or add them to
   `virtualenvwrapper`'s `postactivate` hook.

5. Initialise the database and start the server:
    
        $ django-admin.py syncdb --migrate
        ...
        $ django-admin.py runserver

6. Navigate to `http://localhost:8000`

Updating
--------

After every `git pull`, run

      $ pip install -r deployment/requirements.txt
      $ django-admin.py syncdb --migrate

Deployment
--------

### httpd (Apache) / `mod_wsgi`

Requirements (configured and working):

* httpd
* `mod_wsgi`
* [`virtualenv`](http://www.virtualenv.org/en/latest/)
* Python >= 2.6

This git repository includes an [example httpd `VirtualHost` configuration file](https://github.com/Teplitsa/MikroAct/blob/master/deployment/apache.conf.example).

MikroAct uses [Fabric](http://docs.fabfile.org/en/1.6/) for deployment, and assumes various things (configurable by editing [`fabfile.py`](https://github.com/Teplitsa/MikroAct/blob/master/fabfile.py)):

* installed dependences (see above)
* top-level project directory created; `/var/www/django` by default
* virtualenv directory; `/usr/local/virtualenvs`
* sudo available for your user account

To deploy to your own host, add details to `HOSTS` at the top of `fabfile.py`

With all of these in place, set up the server (replace `<yourhost>` with a server name from `HOSTS`) with:

      $ fab host:<yourhost> setup

Then deploy releases with:

      $ fab host:<yourhost> deploy

You can also run `manage.py` commands, e.g. `manage.py shell`, with:

      $ fab host:<yourhost> manage:shell
      # or with arguments
      $ fab host:<yourhost> manage:"migrate --merge"

Contributing
--------

Please ensure that all submissions (commits or pull requests) to this repository follow relevant best practices:

* Valid, semantic HTML (ideally conforming to [Web Content Accessibility Guidelines](http://www.w3.org/WAI/WCAG20/quickref/Overview.php))
* Python code adhering to [PEP-8](http://www.python.org/dev/peps/pep-0008/), and checked with [pyflakes](http://pypi.python.org/pypi/pyflakes)
