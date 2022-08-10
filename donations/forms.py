from django import forms
from .models import donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = donation
        fields = ('donation_recipient', 'donation_amount',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'donation_recipient': 'Select who you would like to donate margin-left: 1rem;to!',
            'donation_amount': 'Enter the amount you would like to donate',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
