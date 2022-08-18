from django.db import models


class Contact(models.Model):
    """
    Model to create contact items
    """

    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_date = models.DateField(null=True)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return self.email
