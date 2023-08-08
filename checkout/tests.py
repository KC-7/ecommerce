from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
from .models import Order, OrderLineItem
from products.models import Product
from django.contrib.auth.models import User


class TestModels(TestCase):

    def test_order_model(self):
        order = Order.objects.create()
        self.assertEqual(str(order), order.order_number)
    
    def test_order_line_item_model(self):
        product = Product.objects.create(
            price=9.99
        )
        order = Order.objects.create()
        line_item = OrderLineItem.objects.create(
            order=order, product=product, quantity=5
        )
        self.assertEqual(str(line_item), f'SKU {product.sku} on order {order.order_number}')
