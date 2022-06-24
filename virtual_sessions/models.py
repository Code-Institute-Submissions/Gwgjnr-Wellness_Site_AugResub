from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Session(models.Model):
    '''
    This class is used for generating my model for the virtual sessions.
    '''

    PHYSICAL = 'PH'
    MENTAL = 'ME'
    NUTRTIONAL = 'NU'

    TYPES = [
        (PHYSICAL, 'Physical'),
        (MENTAL, 'Mental'),
        (NUTRTIONAL, 'Nutritional'),
    ]

    SUNDAY = 'SU'
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    SATURDAY = 'SA'

    DAYS = [
        (SUNDAY, 'Sunday'),
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
    ]

    category = models.CharField(max_length=50, choices=TYPES)
    title = models.CharField(max_length=200, unique=True)
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hosted_sessions"
    )
    summary = models.TextField(max_length=200)
    details = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_date = models.DateTimeField(auto_now_add=True)
    event_day = models.CharField(max_length=50, choices=DAYS)
    event_time = models.TimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    number_of_sessions = models.IntegerField(null=True)
    signed_up = models.ManyToManyField(
        User, related_name='attending_sessions', blank=True)

    def __str__(self):
        return f"{self.title}"

    def number_signed_up(self):
        return self.signed_up.count()
