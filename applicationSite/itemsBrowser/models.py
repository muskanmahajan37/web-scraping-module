from django.db import models
from django.utils import timezone
import json


# Create your models here.
class RawData(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    data = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    @property
    def to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return self.unique_id


class Currencies(models.Model):
    CURRENCY_CHOICES = [
        ('PLN_PLN', 'PLN'),
        ('EUR_PLN', 'EUR'),
        ('USD_PLN', 'USD'),
        ('JPY_PLN', 'JPY'),
        ('GBP_PLN', 'GBP'),
        ('SupEuro', 'SupremeEuro'),
    ]
    currency_name = models.CharField(choices=CURRENCY_CHOICES, unique=True, primary_key=True, max_length=10)
    exchange_rate_to_pln = models.FloatField()


class AbstractItem(models.Model):
    product_name = models.CharField(max_length=200, default='Unrecognised Item', unique=False)
    price = models.PositiveIntegerField(unique=False)
    currency = models.ForeignKey(Currencies, on_delete=models.SET('PLN'), default='PLN')

    class Meta:
        abstract = True


class Clothes(AbstractItem):
    brand = models.CharField(max_length=50)
    image = models.ImageField()
    date_added = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=30)
