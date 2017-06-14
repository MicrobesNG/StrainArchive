# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from userprofile.models import Organisation


class Strain(models.Model):

    name = models.CharField(max_length = 100)
    date_added = models.DateTimeField(default = datetime.now)
    organisation = models.ForeignKey(Organisation, null = True)
    data_url = models.URLField(null = True)
    number_of_sales = models.IntegerField(default = 0)