# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

import json





class Location(models.Model):

    # specific location name
    full_name = models.CharField(max_length = 1000, blank = True)

    # country to which location belongs
    country = models.CharField(max_length = 100, blank = True)

    # 2-char country code
    iso_alpha_2 = models.CharField(max_length = 2, blank = True)

    # 3-char numerical country code
    # (charfield to handle codes such as 010 or 001)
    iso_num = models.CharField(max_length = 3, blank = True)

    # latitude and longitude coords for location
    lat = models.FloatField(blank = True)
    lon = models.FloatField(blank = True)





class Strain(models.Model):

    # name of sample
    name = models.CharField(max_length = 100)

    # location of associated data files
    data_url = models.URLField(null = True)

    # number of times strain has been purchased
    number_of_sales = models.IntegerField(default = 0)

    # cost of a single purchase
    cost = models.FloatField(default = 0.0)

    # true if the strain is available for purchase
    available = models.BooleanField(default = False)

    # taxonomic info of sample host
    host_taxon_id = models.IntegerField(blank = True)
    host_taxon_name = models.CharField(max_length = 100, blank = True)

    # taxonomic info of strain
    taxon_id = models.IntegerField(blank = True)
    taxon_name = models.CharField(max_length = 100, blank = True)

    # environment type of sample was extracted from
    environmental_sample_type = models.CharField(max_length = 100, blank = True)

    # sample collection info
    collection_location = models.OneToOneField(Location, null = True)
    collection_date = models.DateField(blank = True)