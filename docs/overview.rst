=======================
The contact application
=======================

Providing a contact form for soliciting information from site visitors is a
common need in web development. Writing a contact form and associated handler
view is straightforward and easy to implement with Django, but is an often
tedious and repetitive task. This project aims to remove or reduce that tedium
and repetition by providing an extensible contact form.


Implementation
==============

This application contains a form class called ``ContactForm``, which implements
a useful baseline for contact forms -- collecting a name, email address and
message, and emailing them to site staff -- and which is also designed so as to
allow additional functionality to be added easily in subclasses. For specifics
of how ``ContactForm`` works and what to look at when subclassing it, see the
`forms documentation`_ included with this application.

Also provided is a generic-style view called ``contact``, which is designed to
work out-of-the-box with ``ContactForm`` and subclasses of ``ContactForm``, and
has a number of configurable parameters to allow specification of the form
class to use, whether to require a user to log in before using the form, etc.
For full details on this view and the options it provides, see the
`views_documentation`_ included with this application.

A sample URLConf is included, and can be used "as-is" if the default
``ContactForm`` and default parameters of the ``contact`` view are all that's
required, or studied as an example.

.. _forms documentation: forms.html
.. _views documentation: views.html


Requirements
============

If you will be using the included ``AkismetContactForm`` class, which performs
an Akismet spam check as part of its validation, you will need the `Python
Akismet module`_ and a valid Akismet API key; you can obtain an Akismet API by
following the instructions at `the Akismet web site`_.

.. _Python Akismet module: http://www.voidspace.org.uk/python/modules.shtml#akismet
.. _the Akismet web site: http://akismet.com/


Usage
=====

To get up and running immediately using the default setup, do the following:

    * Add ``contact`` to your project's ``INSTALLED_APPS`` setting. You will
      *not* need to run ``manage.py syncdb``, since this application provides
      no models.

    * In your root URLConf, add the following URL pattern::
          
          (r'^contact/', include('contact.urls'),

    * Create four templates: ``contact/contact_subject.txt`` and
      ``contact/contact.txt``, which will be used to render the email messages
      sent by the form; ``contact/contact.html``, which will be used to display
      the form to users; and ``contact/contact_sent.html``, which will be used
      after the form is successfully submitted.  See the forms and views
      documentation, respectively, for details on the contexts available to the
      first three templates; the fourth is rendered from the
      ``direct_to_template`` generic view, and has no context.

Once this is done, visiting the URL ``/contact/`` on your site will display the
contact form, and submitting it will send an email to each address in the
``MANAGERS`` setting for your project.
