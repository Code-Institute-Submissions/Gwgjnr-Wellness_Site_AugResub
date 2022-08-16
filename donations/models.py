import uuid

from django.db import models
from django.contrib.auth.models import User

from virtual_sessions.models import Session


class donation(models.Model):
    donation_number = models.CharField(max_length=32, null=False, editable=False)
    donater_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donater")
    email = models.EmailField(max_length=254, null=False, blank=False)
    donation_recipient = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True, blank=True, related_name='recipient')
    created_date = models.DateTimeField(auto_now_add=True)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=2)

    def _generate_donation_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the donation number
        """
        if not self.donation_number:
            self.donation_number = self._generate_donation_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.donation_number
