from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    '''
    This class is used for generating my model for the session categories.
    '''
    TYPES = (
        ('P', 'Physical'),
        ('M', 'Mental'),
        ('N', 'Nutritional'),
    )
    
    type = models.CharField(max_length=1, choices=TYPES)

    def __str__(self):

        return self.type


class Session(models.Model):
    '''
    This class is used for generating my model for the virtual sessions.
    '''

    DAYS = (
        ('S', 'Sunday'),
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('H', 'Thursday'),
        ('F', 'Friday'),
        ('A', 'Saturday'),
    )

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, unique=True)
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hosted_sessions"
    )
    summary = models.TextField(max_length=200)
    details = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_date = models.DateTimeField(auto_now_add=True)
    event_day = models.CharField(max_length=1, choices=DAYS)
    event_time = models.TimeField()
    signed_up = models.ManyToManyField(
        User, related_name='attending_sessions', blank=True)

    def __str__(self):
        return self.title

    def number_signed_up(self):
        return self.signed_up.count()
