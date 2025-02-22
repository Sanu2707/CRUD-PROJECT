from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    size = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='product_images/', null=True)

    def __str__(self):
        return self.name  