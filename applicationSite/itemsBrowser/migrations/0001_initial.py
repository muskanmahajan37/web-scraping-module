# Generated by Django 3.1.4 on 2020-12-04 21:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('name', models.CharField(choices=[('PLN', 'PLN'), ('PLN', 'EUR'), ('USD', 'USD'), ('JPY', 'JPY'), ('GBP', 'GBP'), ('SupEuro', 'SupremeEuro')], max_length=10, primary_key=True, serialize=False, unique=True)),
                ('exchange_rate_to_pln', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 12, 4, 21, 38, 0, 266551, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Boots',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='itemsBrowser.abstractitem')),
                ('size', models.CharField(choices=[('37', '37'), ('37.5', '37.5'), ('38', '38'), ('38.5', '38.5'), ('39', '39'), ('39.5', '39.5'), ('40', '40'), ('40.5', '40.5'), ('41', '41'), ('41.5', '41.5'), ('42', '42'), ('42.5', '42.5'), ('43', '43'), ('44', '44'), ('44.5', '44.5'), ('45', '45'), ('45.5', '45.5')], max_length=5)),
                ('image', models.ImageField(upload_to='')),
                ('brand', models.CharField(max_length=50)),
            ],
            bases=('itemsBrowser.abstractitem',),
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('abstractitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='itemsBrowser.abstractitem')),
                ('brand', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=4)),
                ('image', models.ImageField(upload_to='')),
            ],
            bases=('itemsBrowser.abstractitem',),
        ),
        migrations.CreateModel(
            name='AbstractItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='Unrecognised Item', max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('url', models.CharField(max_length=300)),
                ('site_name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('currency', models.ForeignKey(default='PLN', on_delete=models.SET('PLN'), to='itemsBrowser.currency')),
            ],
        ),
    ]
