from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import AboutPage


class AboutPageTests(TestCase):
    """ Tests for About App """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            is_superuser=True
        )
        self.about_page = AboutPage.objects.create(
            title='Test Title',
            content='Test Content'
        )
        self.create_url = reverse(
            'create_about_page')
        self.detail_url = reverse(
            'about_page_detail', args=[self.about_page.id])
        self.edit_url = reverse(
            'edit_about_page', args=[self.about_page.id])
        self.delete_url = reverse(
            'delete_about_page', args=[self.about_page.id])
        self.list_url = reverse(
            'about')

    def test_about_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Title')
        self.assertTemplateUsed(response, 'about/about.html')

    def test_create_about_page(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.create_url, {
            'title': 'New Test Title',
            'content': 'New Test Content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(AboutPage.objects.last().title, 'New Test Title')

    def test_about_page_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Title')
        self.assertTemplateUsed(response, 'about/about_page_detail.html')

    def test_edit_about_page(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.edit_url, {
            'title': 'Updated Title',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, 302)
        self.about_page.refresh_from_db()
        self.assertEqual(self.about_page.title, 'Updated Title')

    def test_delete_about_page(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.delete_url, {
            'username': 'testuser'
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            AboutPage.objects.filter(pk=self.about_page.id).exists())
