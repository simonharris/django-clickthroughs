from django.test import TestCase

from clickthroughs.models import (
    Clickthrough,
    Campaign,
    CampaignHostname,
    Parameter,
    Platform
)

class ClickthroughModelTests(TestCase):
    def test_create_clickthrough(self):
        c = Clickthrough.objects.create(
            ip_address='127.0.0.1',
            url_to='https://example.com',
        )
        self.assertIsNotNone(c.clicked_at)
        self.assertEqual(c.ip_address, '127.0.0.1')
        self.assertEqual(c.url_to, 'https://example.com')


class ModelStrTests(TestCase):
    def test_str_methods(self):
        platform = Platform.objects.create(name="Test Platform")
        campaign = Campaign.objects.create(name="Test Campaign", platform=platform)
        ch = CampaignHostname.objects.create(campaign=campaign, hostname="example.com")
        param = Parameter.objects.create(platform=platform, key="key1", value="value1")

        self.assertEqual(str(platform), "Test Platform")
        self.assertEqual(str(campaign), "Test Campaign")
        self.assertEqual(str(ch), "example.com")
        self.assertEqual(str(param), "key1=value1 (Test Platform)")
