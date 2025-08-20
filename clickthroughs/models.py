from django.db import models


class Clickthrough(models.Model):

    clicked_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(protocol='IPv4')
    session_id = models.CharField(blank=True, null=True, max_length=64, verbose_name='Session ID')
    user_agent = models.TextField(blank=True, null=True)
    url_to = models.URLField(blank=True, null=True, verbose_name='To')
    hostname = models.CharField(blank=True, null=True, max_length=256)
    path_from = models.TextField(blank=True, null=True, verbose_name='From')

