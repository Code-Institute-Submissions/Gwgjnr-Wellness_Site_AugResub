from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model for profile users
    """

    GENDER_MALE = 'MA'
    GENDER_FEMALE = 'FE'
    GENDER_UNKNOWN = 'UN'

    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_UNKNOWN, "Prefer not to say"),
    ]

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    city = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

