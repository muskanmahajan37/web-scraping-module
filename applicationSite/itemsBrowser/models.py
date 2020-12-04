from django.db import models
from django.utils import timezone
import json


# Create your models here.
class RawData(models.Model):
    data = models.TextField()
    date = models.DateTimeField(default=timezone.now())


class Currency(models.Model):
    CURRENCY_CHOICES = [
        ('PLN', 'PLN'),
        ('PLN', 'EUR'),
        ('USD', 'USD'),
        ('JPY', 'JPY'),
        ('GBP', 'GBP'),
        ('SupEuro', 'SupremeEuro'),
    ]
    name = models.CharField(choices=CURRENCY_CHOICES)
    exchange_rate_to_pln = models.FloatField()


class AbstractItem(models.Model):
    product_name = models.CharField(max_length=200, default='Unrecognised Item', unique=False)
    price = models.PositiveIntegerField(unique=False)
    currency = models.ForeignKey(Currency, on_delete=models.SET_DEFAULT(), default='PLN')
    url = models.CharField()
    site_name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)


class Clothes(AbstractItem):
    SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]
    brand = models.CharField()
    size = models.CharField(choices=SIZE_CHOICES)
    image = models.ImageField()


class Boots(Clothes):
    SIZE_CHOICES = [
        ('37', '37'), ('37.5', '37.5'), ('38', '38'), ('38.5', '38.5'), ('39', '39'), ('39.5', '39.5'),
        ('40', '40'), ('40.5', '40.5'), ('41', '41'), ('41.5', '41.5'), ('42', '42'), ('42.5', '42.5'),
        ('43', '43'), ('44', '44'), ('44.5', '44.5'), ('45', '45'), ('45.5', '45.5')
    ]
    size = models.CharField(choices=SIZE_CHOICES)
