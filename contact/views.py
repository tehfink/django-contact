"""
View which can render and send email from a contact form.

"""


from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from contact.forms import ContactForm


def contact(request, form_class=ContactForm,
            template_name='contact/contact.html',
            success_url='/contact/sent/', login_required=False,
            fail_silently=False):
    """
    Renders a contact form, validates its input and sends an email
    from it.
    
    """
    if login_required and not request.user.is_authenticated():
        return redirect_to_login(request.path)

    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, request=request)
        if form.is_valid():
            form.save(fail_silently=fail_silently)
            return HttpResponseRedirect(success_url)
    else:
        form = form_class(request=request)

    return render_to_response(template_name,
                              { 'form': form },
                              context_instance=RequestContext(request))
