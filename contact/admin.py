from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    '''
    Class to organise Sessions in Admin panel
    '''
    list_display = (
        'name',
        'subject',
        'email',
        'created_date',
        'responded',
    )


admin.site.register(Contact, ContactAdmin)
