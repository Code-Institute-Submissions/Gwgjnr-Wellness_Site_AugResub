from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Session(models.Model):
    '''
    This class is used for generating my model for the virtual sessions.
    '''

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

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hosted_sessions"
    )
    summary = models.TextField(max_length=200)
    details = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_date = models.DateTimeField(auto_now_add=True)
    event_day = models.CharField(max_length=50, choices=DAYS)
    event_time = models.TimeField()
    signed_up = models.ManyToManyField(
        User, related_name='attending_sessions', blank=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return f"{self.title}"

    def number_signed_up(self):
        return self.signed_up.count()

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    '''
    This class is used for generating my model for the comments and replies.
    '''
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')


    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"