from django.db import models

class Product(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mobile_number = models.CharField(max_length=15)
    size = models.CharField(max_length=10, null=True, blank=True)
    category = models.CharField(max_length=255)
    images = models.TextField()
    scraped_at = models.DateTimeField(auto_now_add=True)
