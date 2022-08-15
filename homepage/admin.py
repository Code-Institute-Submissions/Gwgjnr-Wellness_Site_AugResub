from django.contrib import admin
from .models import NewsletterSignup


class NewsletterAdmin(admin.ModelAdmin):
    '''
    Class to organise Sessions in Admin panel
    '''
    list_display = (
        'name',
        'email',
    )


admin.site.register(NewsletterSignup, NewsletterAdmin)
