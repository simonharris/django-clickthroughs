from django.contrib import admin

from .models import (
    Campaign,
    CampaignHostname,
    Clickthrough,
    Parameter,
    Platform,
)


## inlines --------------------------------------------------------------------


class CampaignHostnameInline(admin.TabularInline):
    model = CampaignHostname
    extra = 1


## filters --------------------------------------------------------------------


class HostnameFilter(admin.SimpleListFilter):
    title = 'hostname'
    parameter_name = 'hostname'

    def lookups(self, request, model_admin):
        hostnames = {c.hostname for c in Clickthrough.objects.all()}
        return [(h, h) for h in hostnames if not h.startswith('dev.')]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(hostname=self.value())
        return queryset


## admins ---------------------------------------------------------------------


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):

    list_display = ['name']


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'start_date', 'end_date']
    prepopulated_fields = {'slug': ['name']}
    inlines = [CampaignHostnameInline]


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):

    list_display = ['platform', 'key', 'value']
    list_filter = ['platform']


@admin.register(Clickthrough)
class ClickthroughAdmin(admin.ModelAdmin):

    list_display = ['clicked_at', 'hostname', 'url_to']
    list_filter = (HostnameFilter,)
    search_fields = ['url_to']
    show_facets = admin.ShowFacets.ALWAYS
