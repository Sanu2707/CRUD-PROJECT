from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True)
    price = models.IntegerField(null=True)

    def _str_(self):
        return self.name
