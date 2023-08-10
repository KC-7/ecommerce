from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product


class BagViewsTestCase(TestCase):
    """ Tests for Bag """
    def setUp(self):
        self.client = Client()
        self.view_bag_url = reverse('view_bag')
        self.product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            price=10.00,
        )

    def test_view_bag(self):
        response = self.client.get(self.view_bag_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]), {
                'quantity': 2, 'redirect_url': self.view_bag_url})
        bag = self.client.session['bag']
        self.assertIn(str(self.product.id), bag)
        self.assertEqual(bag[str(self.product.id)], 2)

    def test_adjust_bag(self):
        self.client.session['bag'] = {str(self.product.id): 2}
        response = self.client.post(
            reverse('adjust_bag', args=[self.product.id]), {'quantity': 3, })
        bag = self.client.session['bag']
        self.assertIn(str(self.product.id), bag)
        self.assertEqual(bag[str(self.product.id)], 3)

    def test_remove_from_bag(self):
        self.client.session['bag'] = {str(self.product.id): 2}
        response = self.client.post(
            reverse('remove_from_bag', args=[self.product.id]))
        bag = self.client.session.get('bag', {})
        self.assertNotIn(str(self.product.id), bag)
