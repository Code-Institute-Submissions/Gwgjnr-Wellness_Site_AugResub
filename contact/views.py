from datetime import date
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import ContactForm


class Contact(LoginRequiredMixin, View):
    '''
    A view for rendering and submitting a contact form to the database.
    '''

    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        """
        A view to return the contact form page
        """

        context = {
            'contact_form': ContactForm(),
        }

        return render(request, 'contact/contact_form.html', context)

    def post(self, request, *args, **kwargs):
        """
        A view to post the contact form to the database
        """

        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.instance.email = request.user.email
            contact_form.instance.name = request.user.username
            contact_form.instance.created_date = date.today()
            contact_form.save()
            messages.success(request, 'Thank you for your feedback!')
            return HttpResponseRedirect('/')
        else:
            contact_form = ContactForm()

        context = {
            'contact_form': ContactForm(),
        }

        return render(request, 'contact/contact_form.html', context)
