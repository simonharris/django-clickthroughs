from django.test import TestCase
from clickthroughs.models import Clickthrough

class ClickthroughModelTests(TestCase):
    def test_create_clickthrough(self):
        c = Clickthrough.objects.create(
            ip_address='127.0.0.1',
            url_to='https://example.com',
        )
        self.assertIsNotNone(c.clicked_at)
        self.assertEqual(c.ip_address, '127.0.0.1')
        self.assertEqual(c.url_to, 'https://example.com')
