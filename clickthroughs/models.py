from django.db import models


class Clickthrough(models.Model):

    clicked_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(protocol='IPv4')
    url_to = models.URLField(blank=True, null=True, verbose_name='To')
    path_from = models.CharField(blank=True, null=True, max_length=256, verbose_name='From')

