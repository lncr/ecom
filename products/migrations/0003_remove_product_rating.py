# Generated by Django 3.1.6 on 2021-11-01 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
