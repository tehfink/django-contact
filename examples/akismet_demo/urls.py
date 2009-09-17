from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from contact.views import contact
from contact.forms import AkismetContactForm


urlpatterns = patterns('',
    url(r'^contact/$',
        contact,
        {'form_class': AkismetContactForm},
    ),
    url(r'^contact/sent/$',
        direct_to_template,
        {'template': 'contact/sent.html' },
        name = 'sent',
    ),
)
