MikroAct
========

Private repository for the MikroAct project.

Getting started
--------

  ```none
  $ git clone git@github.com:Teplitsa/MikroAct.git
  ...
  $ cd MikroAct.git
  $ pip install -r requirements.txt
  $ cp mikroact/local_settings.py.example mikroact/local_settings.py
  $ python manage.py syncdb --migrate
  $ python manage.py runserver
  ```

Then navigate to http://localhost:8000

Contributing
--------

Please ensure that all submissions (commits or pull requests) to this repository adhere to relveant best practices:

* Valid, semantic HTML (ideally conforming to [Web Content Accessibility Guidelines](http://www.w3.org/WAI/WCAG20/quickref/Overview.php))
* Python code adhering to [PEP-8](http://www.python.org/dev/peps/pep-0008/), and checked with [pyflakes](http://pypi.python.org/pypi/pyflakes)
