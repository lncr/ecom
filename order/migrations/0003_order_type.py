# Generated by Django 3.1.6 on 2021-10-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20211030_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='type',
            field=models.CharField(choices=[('pending', 'Pending'), ('delivered', 'Delivered'), ('canceled', 'Canceled')], default='pending', max_length=128),
        ),
    ]
