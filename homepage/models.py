from django.db import models


class NewsletterSignup(models.Model):
    email = models.EmailField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
