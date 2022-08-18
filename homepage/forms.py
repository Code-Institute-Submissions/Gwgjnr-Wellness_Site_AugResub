from django import forms
from .models import NewsletterSignup


class NewsletterForm(forms.ModelForm):
    """
    Form class to create the newsletter form
    """
    class Meta:
        """
        Meta information for the contact form
        """
        model = NewsletterSignup
        fields = ('name', 'email',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.TextInput(
                attrs={'placeholder': 'Enter your email address'}),
        }
        labels = {
            "name": "",
            "email": "",
        }
