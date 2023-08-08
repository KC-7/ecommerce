from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import BlogPage


class BlogPageTests(TestCase):
    """  """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
            is_superuser=True
        )
        self.blog = BlogPage.objects.create(
            title='Test Blog',
            content='Test Content'
        )
        self.list_url = reverse('blog')
        self.detail_url = reverse('blog_page_detail', args=[self.blog.id])
        self.create_url = reverse('create_blog_page')
        self.edit_url = reverse('edit_blog_page', args=[self.blog.id])
        self.delete_url = reverse('delete_blog_page', args=[self.blog.id])

    def test_blog_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Blog')
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_blog_page_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Blog')
        self.assertTemplateUsed(response, 'blog/blog_page_detail.html')

    def test_create_blog_page(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.create_url, {
            'title': 'New Blog',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPage.objects.last().title, 'New Blog')

    def test_edit_blog_page(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.edit_url, {
            'title': 'Updated Blog',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, 302)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.title, 'Updated Blog')

    def test_delete_blog_page(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(self.delete_url, {
            'username': 'testuser'
        })
        self.assertEqual(response.status_code, 302)
        self.assertFalse(BlogPage.objects.filter(pk=self.blog.id).exists())
