"""
Example URLConf for a contact form.

Because the ``contact_form`` view takes configurable arguments, it's
recommended that you manually place it somewhere in your URL
configuration with the arguments you want. If you just prefer the
default, however, you can hang this URLConf somewhere in your URL
hierarchy (for best results with the defaults, include it under
``/contact/``).

"""


from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from contact.views import contact


urlpatterns = patterns('',
    url(r'^$',
        contact,
        name = 'contact'
    ),
    url(r'^sent/$',
        direct_to_template,
        { 'template': 'contact/sent.html' },
        name = 'sent'
    ),
)
