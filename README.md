# django-clickthroughs

[![PyPI version](https://img.shields.io/pypi/v/django_clickthroughs.svg)](https://pypi.org/project/django_clickthroughs/)
![Tests](https://github.com/simonharris/django-clickthroughs/actions/workflows/tests.yml/badge.svg)

Logging and reporting for outbound links, with ability to configure in extra
parameters such as affiliate tags.


## Installation notes

 - `pip install django-clickthroughs`
 - add `clickthroughs` to `INSTALLED_APPS`
 - add `urls.py` entry (pick your own URL space)
 - run migrations: `python manage.py migrate clickthroughs`


## Usage notes

```
{% load click_tags %}

<a href="{% clickthrough 'https://example.com' %}">Visit Example</a>

```

