from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('subject', 'message',)

        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Enter your reason for contacting us'}),
            'message': forms.Textarea(
                attrs={'placeholder': 'Enter your message here'}),
        }
        labels = {
            "subject": "",
            "message": "",
        }