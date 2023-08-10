from django.test import TestCase, Client
from django.contrib.auth.models import User
from profiles.models import UserProfile


class ProfilesViewsTestCase(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client = Client()

        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

    def test_profile_view_logged_in(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profile_view_anonymous_user(self):
        self.client.logout()
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        # Should redirect to login page

    def test_update_profile(self):
        response = self.client.post('/profile/', {
            'default_phone_number': '123456789',
            'default_street_address1': 'Street Address',
            'default_town_or_city': 'City',
            'default_postcode': '12345',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile updated successfully')
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.default_phone_number, '123456789')
