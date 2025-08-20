from django.contrib import admin

from .models import *

@admin.register(Clickthrough)
class ClickthroughAdmin(admin.ModelAdmin):

    list_display = ['clicked_at', 'hostname', 'url_to']
