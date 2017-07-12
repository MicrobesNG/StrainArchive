# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

import json

# # taxonomical models
# class Family(models.Model):
#     name = models.CharField(max_length = 100)    
#     # other family data fields?


#     def to_dict(self):
#         output_dict = {
#             "name": self.name,
#             "pk": self.pk,
#             "genera": []
#         }

#         for genus in self.genus_set.all():

#             output_dict["genera"].append(genus.to_dict())

#         return output_dict


#     def to_json_string(self):

#         return json.dumps(self.to_dict())

# class Genus(models.Model):
#     name = models.CharField(max_length = 100)
#     family = models.ForeignKey(Family, null = True)
#     # other genus data fields?


#     def to_dict(self):
#         output_dict = {
#             "name": self.name,
#             "pk": self.pk,
#             "species": []
#         }

#         for species in self.species_set.all():
#             output_dict["species"].append(
#                 {
#                     "name": species.name,
#                     "pk": species.pk,
#                 }
#             )

#         return output_dict
    

#     def to_json_string(self):

#         return json.dumps(self.to_dict())

# class Species(models.Model):
#     name = models.CharField(max_length = 100)
#     genus = models.ForeignKey(Genus, null = True)
#     # other species data fields? 




class Location(models.Model):
    full_name = models.CharField(max_length = 1000, blank = True)
    country = models.CharField(max_length = 100, blank = True)
    iso_alpha_2 = models.CharField(max_length = 2, blank = True)
    iso_num = models.CharField(max_length = 3, blank = True)
    lat = models.FloatField(blank = True)
    lon = models.FloatField(blank = True)





class Strain(models.Model):

    STRAIN_TYPES = (
        ("D", "Default"),
        ("S", "SomeotherType")
    )

    name = models.CharField(max_length = 100)
    strain_type = models.CharField(max_length = 1, choices = STRAIN_TYPES, default = "D")
    
    data_url = models.URLField(null = True)
    number_of_sales = models.IntegerField(default = 0)
    cost = models.FloatField(default = 0.0)
    host_taxon_id = models.IntegerField(blank = True)
    host_taxon_name = models.CharField(max_length = 100, blank = True)
    taxon_id = models.IntegerField(blank = True)
    taxon_name = models.CharField(max_length = 100, blank = True)
    environmental_sample_type = models.CharField(max_length = 100, blank = True)
    collection_location = 

    # family = models.ForeignKey(Family, null = True)
    # genus = models.ForeignKey(Genus, null = True)
    # species = models.ForeignKey(Species, null = True)