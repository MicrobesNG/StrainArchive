# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ManagementUserProfile(models.Model):

    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    user = models.OneToOneField(User)

    def get_full_name(self):
        
        return "%s %s" % (self.first_name, self.last_name)