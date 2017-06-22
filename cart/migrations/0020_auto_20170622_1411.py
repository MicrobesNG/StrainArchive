# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 14:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0019_purchase_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='received_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='quote',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Processing'), ('D', 'Dispatched'), ('R', 'Received'), ('V', 'Void')], default='A', max_length=1),
        ),
    ]
