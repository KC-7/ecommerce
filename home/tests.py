from django.test import TestCase, Client
from django.urls import reverse


class HomeViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')

    def test_view_home_page(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
