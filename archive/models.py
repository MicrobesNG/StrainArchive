# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from userprofile.models import Organisation


# taxonomical models
class Family(models.Model):
    name = models.CharField(max_length = 100)    
    # other family data fields?

class Genus(models.Model):
    name = models.CharField(max_length = 100)
    family = models.ForeignKey(Family, null = True)
    # other genus data fields?

class Species(models.Model):
    name = models.CharField(max_length = 100)
    genus = models.ForeignKey(Genus, null = True)
    # other species data fields? 

class Strain(models.Model):

    STRAIN_TYPES = (
        ("D", "Default"),
        ("S", "SomeotherType")
    )

    name = models.CharField(max_length = 100)
    strain_type = models.CharField(max_length = 1, choices = STRAIN_TYPES, default = "D")
    date_added = models.DateTimeField(default = datetime.now)
    organisation = models.ForeignKey(Organisation, null = True)
    data_url = models.URLField(null = True)
    number_of_sales = models.IntegerField(default = 0)

    family = models.ForeignKey(Family, null = True)
    genus = models.ForeignKey(Genus, null = True)
    species = models.ForeignKey(Species, null = True)