from django.db import models

# Create your models here.
class AbstractItem(models.model):
    product_name = models.CharField(max_length=200, default='Unrecognised Item', unique=False)
    price = models.PositiveIntegerField(unique=False)
    currency = models.ForeignKey()

