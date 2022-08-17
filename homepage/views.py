from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from virtual_sessions.models import Session


from .forms import NewsletterForm


def index(request):
    """
    A view to return the homepage
    """
    seminars = Session.objects.all()

    if request.method == 'POST':

        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, 'Thank you for your siging up to our newsletter!')
            return HttpResponseRedirect('/')

        else:
            newsletter_form = NewsletterForm()
            messages.warning(request, 'There was an error with your sign up, you may have already registered')
            return HttpResponseRedirect('/')

    if request.GET.get('paymentComplete'):
        messages.success(request, 'Your donation was succesful')

    context = {
        'seminars': seminars,
        'newsletter_form': NewsletterForm(),
    }

    return render(request, 'homepage/index.html', context)
