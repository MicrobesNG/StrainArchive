# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Organisation(models.Model):

    name = models.CharField(max_length = 200)

    def get_upload_count(self):

        total = 0
        for userdata in self.userdata_set.all():
            total += userdata.uploader_set.all().count()
        
        return total
    
    def get_member_count(self):

        return self.userdata_set.all().count()

class UserData(models.Model):

    title = models.CharField(max_length = 5)
    forename = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    email = models.EmailField(null = True)
    organisation = models.OneToOneField(Organisation, null = True)
    user = models.OneToOneField(User, null = True)

    def get_full_name(self):

        return self.title + " " + self.forename + self.surname