from django.test import TestCase, Client
from django.urls import reverse
from .models import Product

class ScrapeDataTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = 'https://www.flipkart.com/srpm-wayfarer-sunglasses/p/itmaf19ae5820c06'
        self.data = {'url': self.url}

    def test_scrape_data(self):
        response = self.client.post(reverse('scrape_data'), data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Scraped Successfully')

        product = Product.objects.get(url=self.url)
        self.assertEqual(product.url, self.url)
        self.assertIsNotNone(product.title)
        self.assertIsNotNone(product.description)
        self.assertIsNotNone(product.price)

    def test_scraped_data_expiration(self):
        product = Product(url=self.url)
        product.scraped_date = datetime.now() - timedelta(days=8)
        product.save()

        response = self.client.post(reverse('scrape_data'), data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Scraped Successfully')

        updated_product = Product.objects.get(url=self.url)
        self.assertGreater(updated_product.scraped_date, product.scraped_date)
