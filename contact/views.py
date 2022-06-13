from django.shortcuts import render
from django.views import View
from .forms import ContactForm


class Contact(View):

    """
    A view to return the contact form page
    """
    def get(self, request, *args, **kwargs):
            
        context = {
            'contact_form': ContactForm(),
        }

        return render(request, 'contact/contact_form.html', context)
    
    def post(self, request, *args, **kwargs):

        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.instance.email = request.user.email
            contact_form.instance.author = request.user
        
        context = {
            'contact_form': ContactForm(),
        }
        
        return render(request, 'contact/contact_form.html', context)
