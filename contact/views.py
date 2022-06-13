from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    """
    A view to return the contact form page
    """

    context = {
        'contact_form': ContactForm(),
    }

    return render(request, 'contact/contact_form.html', context)
