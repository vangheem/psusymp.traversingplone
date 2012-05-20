Introduction
============

Code emamples for "Traversing Plone" Penn State Plone Symposium Presentation.

Running the buildout
--------------------

Just the normal thing::

    git clone git://github.com/vangheem/psusymp.traversingplone.git
    cd psusymp.hardenedplone
    python2.6 bootstrap.py
    ./bin/buildout


Running Django
--------------

Buildout sets up an interpreter::

    ./bin/django manage.py runserver --noreload

Need to reload because django doesn't know how to start
with reload in a buildout environment.
