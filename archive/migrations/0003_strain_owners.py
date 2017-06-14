# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 14:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('archive', '0002_strain_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='strain',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
