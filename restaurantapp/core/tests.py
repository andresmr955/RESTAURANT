from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class HomeViewTests(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')