from django.contrib import admin
from .models import Session, Comment

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    '''
    Class to organise Sessions in Admin panel
    '''
    list_display = (
        'title',
        'host',
        'created_date',
    )

    ordering = ('created_date',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Class to organise Comments in Admin panel
    '''
    list_display = (
        'name',
        'body',
        'created_on',
        'updated',
        'approved',
    )

    ordering = ('created_on',)
