# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_auto_20170622_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='bbsrc_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='billing_address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='quote',
            name='customer_note',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='quote',
            name='delivery_address',
            field=models.TextField(default=''),
        ),
    ]