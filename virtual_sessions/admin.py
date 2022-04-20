from django.contrib import admin
from .models import Session


class SessionAdmin(admin.ModelAdmin):
    '''
    Class to organise Sessions in Admin panel
    '''
    list_display = (
        'category',
        'title',
        'host',
        'created_date',
        'event_day',
        'event_time',
    )

    ordering = ('created_date',)


admin.site.register(Session, SessionAdmin)

