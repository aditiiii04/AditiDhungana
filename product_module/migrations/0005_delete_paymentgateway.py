# Generated by Django 4.0.4 on 2022-06-05 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_paymentgateway'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentGateway',
        ),
    ]
