from django import template
from django.urls import reverse
from django.utils.http import urlencode


register = template.Library()

@register.simple_tag
def clickthrough(url: str) -> str:

    cturl = reverse('clickthroughs:go')

    return cturl + '?' + urlencode({'to': url})

