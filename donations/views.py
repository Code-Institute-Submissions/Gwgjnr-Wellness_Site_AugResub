from django.shortcuts import render
from django.contrib import messages


from .forms import DonationForm

def donation(request):
    donation_form = DonationForm()
    template = 'donations/donations.html'

    context = {
        'donation_form': donation_form,
        'stripe_public_key': 'pk_test_51Kk3QVBM0LrtAfJPkLcnwhTk9sy0ldK3Hot9MuLZu0Bv8iyAf4L7wzvOscswq0YTmxzURdmOLpfckitXH25KifKL00FZr9mart',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
