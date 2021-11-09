from django.db import models


# Create your models here.
class Product(models.Model):
    name: models.CharField(max_length=200)
    price: models.DecimalField(max_digits=7, decimal_places=2)
    delivery: models.DecimalField(max_digits=7, decimal_places=2)
    image: models.CharField(max_length=2000)
    stock: models.IntegerField()
