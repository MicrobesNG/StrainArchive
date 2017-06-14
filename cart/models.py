# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from archive.models import Strain
import json

# how many of which strain to be purchased
class Purchase(models.Model):

    strain = models.ForeignKey(Strain)
    quantity = models.IntegerField(default = 0)

# collection of purchases and user which requested them
class ConfirmedBasket(models.Model):

    user = models.ForeignKey(User)
    purchases = models.ManyToManyField(Purchase)

    def as_dict(self):

        output = {"purchases": []}

        for purchase in self.purchases.all():
            output["purchases"].append(
                {
                    "strain_id": purchase.strain.pk,
                    "strain_name": purchase.strain.name,
                    "quantity": purchase.quantity
                }
            )
        
        return output

    def as_json_string(self):

        return json.dumps(self.as_dict())


# quote for cost of basket
class Quote(models.Model):

    STATUS_CHOICES = (
        ("P", "Pending"),
        ("S", "Sent"),
        ("A", "Accepted"),
        ("R", "Rejected"),
        ("C", "Cancelled")
    )

    user = models.ForeignKey(User)
    basket = models.OneToOneField(ConfirmedBasket, null = True)
    cost = models.FloatField(default = 0)

    status = models.CharField(
        default = "P",
        choices = STATUS_CHOICES,
        max_length = 1
    )

    def get_verbose_status_name(self):

        return self.get_status_display()


# represents dispatched product/order status
class Order(models.Model):

    STATUS_CHOICES = (
        ("A", "Awaiting Payment"),
        ("P", "Processing"),
        ("D", "Dispatched"),
        ("R", "Received"),
        ("V", "Void")
    )

    quote = models.OneToOneField(Quote, null = True)
    
    status = models.CharField(
        default = "A",
        choices = STATUS_CHOICES,
        max_length = 1
    )


    def get_verbose_status_name(self):

        return self.get_status_display()
