MikroAct
========

Private repository for the MikroAct project.

Getting started
--------

1. Install dependencies:
    * Python 2.5-2.7 with [pip](http://www.pip-installer.org/en/latest/)
    * Postgresql ([installation guides](http://wiki.postgresql.org/wiki/Detailed_installation_guides))
    * Postgres development headers (`-dev` or `-devel` packages)
    * Postgis (version 2 strongly recommended over version 1)

2. Set up a [Postgres database with Postgis](https://docs.djangoproject.com/en/1.5/ref/contrib/gis/install/postgis/).

3. Check out code and create local configuration:
    
        $ git clone git@github.com:Teplitsa/MikroAct.git
        ...
        $ cd MikroAct.git
        $ pip install -r requirements.txt
        $ cp mikroact/local_settings.py.example mikroact/local_settings.py

4. Edit `local_settings.py` as appropriate (particularly `DATABASES['default']['USER']`), then initialise the database and start the server:
    
        $ python manage.py syncdb --migrate
        $ python manage.py runserver

5. Navigate to `http://localhost:8000`

Contributing
--------

Please ensure that all submissions (commits or pull requests) to this repository follow relevant best practices:

* Valid, semantic HTML (ideally conforming to [Web Content Accessibility Guidelines](http://www.w3.org/WAI/WCAG20/quickref/Overview.php))
* Python code adhering to [PEP-8](http://www.python.org/dev/peps/pep-0008/), and checked with [pyflakes](http://pypi.python.org/pypi/pyflakes)
