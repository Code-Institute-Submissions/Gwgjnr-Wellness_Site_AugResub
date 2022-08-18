from django.contrib import admin
from .models import NewsletterSignup


class NewsletterAdmin(admin.ModelAdmin):
    '''
    Class to organise newsletter sign ups in Admin panel
    '''
    list_display = (
        'name',
        'email',
    )


admin.site.register(NewsletterSignup, NewsletterAdmin)
