from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Category, Product


class CatalogViewsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Books", slug="books")
        self.product = Product.objects.create(
            category=self.category,
            name="Clean Code",
            slug="clean-code",
            price=Decimal("39.99"),
        )

    def test_product_list(self):
        response = self.client.get(reverse("catalog:product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Clean Code")

    def test_product_detail(self):
        response = self.client.get(self.product.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "39.99")

    def test_inactive_product_is_hidden(self):
        self.product.is_active = False
        self.product.save()
        response = self.client.get(reverse("catalog:product_list"))
        self.assertNotContains(response, "Clean Code")
