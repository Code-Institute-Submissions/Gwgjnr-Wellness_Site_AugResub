from django.shortcuts import render
from django.contrib import messages

from .forms import DonationForm


def donation(request):
    donation_form = DonationForm()
    template = 'donations/donations.html'

    context = {
        'donation_form': donation_form
    }

    return render(request, template, context)
