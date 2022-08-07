from django import forms
from .models import donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = donation
        fields = ('donation_recipient', 'donation_amount',)
