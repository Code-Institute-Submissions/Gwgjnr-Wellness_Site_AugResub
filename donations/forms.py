from django import forms
from .models import donation


class DonationForm(forms.ModelForm):
    """
    Form class to create the Donation form
    """
    class Meta:
        """
        Meta information for the contact form
        """
        model = donation
        fields = ('donation_recipient', 'donation_amount',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['donation_amount'] = forms.DecimalField(min_value=2,
                                                            decimal_places=2,)
        placeholders = {
            'donation_recipient': '',
            'donation_amount': 'Minimum donation €2',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
