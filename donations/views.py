from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .forms import DonationForm

def donation(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    donation_form = DonationForm()
    template = 'donations/donations.html'

    context = {
        'donation_form': donation_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': stripe_secret_key,
    }

    return render(request, template, context)
