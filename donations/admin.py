from django.contrib import admin

from .models import donation


class DonationAdmin(admin.ModelAdmin):
    '''
    Class to organise Donations in Admin panel
    '''
    readonly_fields = ('donation_number', 'created_date', 'donation_amount',
                       'donation_recipient',)

    fields = ('donation_number', 'created_date', 'donater_name',
              'email', 'donation_amount', 'donation_recipient',)

    list_display = ('donation_number', 'created_date', 'donater_name',
                    'donation_amount', 'donation_recipient',)

    ordering = ('-created_date',)


admin.site.register(donation, DonationAdmin)
