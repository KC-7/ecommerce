from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Product
from .forms import ProductForm


class ProductsModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category",
            friendly_name="Test Friendly")
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            category=self.category)

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_product_string_representation(self):
        self.assertEqual(str(self.product), "Test Product")

    def test_get_friendly_name(self):
        self.assertEqual(self.category.get_friendly_name(), "Test Friendly")


class ProductsViewsTests(TestCase):

    def setUp(self):
        self.client = Client()

        # Create a superuser and normal user for testing
        self.superuser = User.objects.create_superuser(
            'testuser', 'test@email.com', 'testpassword')
        self.user = User.objects.create_user(
            'normaluser', 'normal@email.com', 'normalpassword')

        # Create a category and product for testing views
        self.category = Category.objects.create(
            name="Test Category",
            friendly_name="Test Friendly")
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
            category=self.category)

        self.all_products_url = reverse('products')
        self.product_detail_url = reverse(
            'product_detail', args=[self.product.id])
        self.add_product_url = reverse('add_product')

    def test_all_products_view(self):
        response = self.client.get(self.all_products_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

    def test_product_detail_view(self):
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Description')

    def test_add_product_view_access_as_superuser(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.add_product_url)
        self.assertEqual(response.status_code, 200)

    def test_add_product_view_no_access_as_user(self):
        self.client.login(username='normaluser', password='normalpassword')
        response = self.client.get(self.add_product_url)
        self.assertEqual(response.status_code, 302)
        # Expect a redirect since a normal user can't add products

    # Additional tests could be added for other views, GET and POST methods


class ProductFormTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Test Category", friendly_name="Test Friendly")

    def test_product_form_valid_data(self):
        form = ProductForm(data={
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 10.00,
            'category': self.category.id,
        })
        self.assertTrue(form.is_valid())

    def test_product_form_no_data(self):
        form = ProductForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
        # Expecting errors for name, description, and price
