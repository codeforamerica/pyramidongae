=========================
Setting up Pyramid on GAE
=========================

This project demonstrates how to use Buildout to set up a sane development
environment for developing and deploying Pyramid apps on Google App Engine.

See http://docs.pylonsproject.org/projects/pyramid/1.0/index.html for
information about Pyramid.

See http://www.buildout.org/ for information on Buildout.

This app is one of the simplest possible, serving up 'Hello, World!' at '/',
and 'Goodbye, World!' at '/goodbye'.

Running the application out of the box
--------------------------------------

Build and run the application::

  $ python2.5 bootstrap.py --distribute
  $ ./bin/buildout
  $ ./bin/dev_appserver parts/pyramidongae

Then access the application using a web browser with the following URL::

  http://localhost:8080/


Uploading and managing
----------------------

To upload application files, run::

  $ ./bin/appcfg update parts/pyramidongae

For a more detailed documentation follow this url::

  http://code.google.com/appengine/docs/python/tools/uploadinganapp.html

