from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.views import View

from .forms import DonationForm

import stripe
import json


class Donation(View):

    def get(self, request, *args, **kwargs):
           
        context = {
            'donation_form': DonationForm(),
        }

        return render(request, 'donations/donations.html', context)

    def post(self, request, *args, **kwargs):
        
        form_data = {
            'donation_recipient': request.POST['donation_recipient'],
            'donation_amount': request.POST['donation_amount'],
        }

        donation_form = DonationForm(form_data)
        if donation_form.is_valid():
            donation_form.instance.email = request.user.email
            donation_form.instance.donater_name = request.user
            donate = donation_form.save(commit=False)
            donate.save()
            request.session['donation_amount'] = str(donation_form.cleaned_data['donation_amount'])
            print(request.session['donation_amount'])
        else:
            donation_form = DonationForm()

        return redirect(reverse('checkout'))


class donationCheckout(View):

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Your donation was succesful')
        return redirect('homepage')

    def get(self, request, *args, **kwargs):
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        donation_amount = request.session['donation_amount']
        stripe_amount = int(donation_amount)*100

        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_amount,
            currency=settings.STRIPE_CURRENCY,
        )

        template = 'donations/donation_checkout.html'

        context = {
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'donation_amount': donation_amount,
        }

        return render(request, template, context)
