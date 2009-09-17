============
INSTALLATION
============

There are two ways to install this application for use by your
projects. The easiest in most cases is to do a git clone into a directory
that is on your Python path::

    git clone git://github.com/rcoyner/django-contact.git

The other method is to download a packaged version and use Python's
``distutils`` to install it onto your Python path::

    wget http://github.com/rcoyner/django-contact/tarball/0.3
    tar xzvf rcoyner-django-contact-4f8c3ef5a82b0495018e17643222873bc199cec1.tar.gz
    cd rcoyner-django-contact-4f8c3ef5a82b0495018e17643222873bc199cec1
    python setup.py install

Depending on your system configuration, you may need to prefix the last command
with ``sudo`` and supply your password to perform a system-wide installation.
