# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0028_auto_20170626_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='promotion_parameters',
            field=models.TextField(null=True),
        ),
    ]
