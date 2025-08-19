from django.contrib import admin

from .models import *

@admin.register(Clickthrough)
class ClickthroughAdmin(admin.ModelAdmin):

    list_display = ['ip_address', 'url_to']
