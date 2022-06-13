from django.contrib import admin
from .models import Contact


class SessionAdmin(admin.ModelAdmin):
    '''
    Class to organise Sessions in Admin panel
    '''
    ordering = ('created_date',)


admin.site.register(Contact)

