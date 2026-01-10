from django.template import Template, Context
from django.test import TestCase

class ClickthroughTemplateTagTests(TestCase):

    def test_url_tag(self):
        tpl = Template("{% load click_tags %}foo {% clickthrough 'https://example.com/some/page' %} bar")
        rendered = tpl.render(Context())
        self.assertIn('/?to=https%3A%2F%2Fexample.com%2Fsome%2Fpage', rendered)

    # def test_affiliate_url_tag(self):
    #     tpl = Template('{% load click_tags %}{{ "https://example.com"|affiliate_url:"skiddle" }}')
    #     rendered = tpl.render(Context())
    #     #self.assertIn('affiliate_id', rendered)  # if your tag appends one
