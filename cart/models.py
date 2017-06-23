# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from archive.models import Strain
from datetime import datetime
import json

# how many of which strain to be purchased
class Purchase(models.Model):

    strain = models.ForeignKey(Strain)
    quantity = models.IntegerField(default = 0)
    cost = models.FloatField(default = 0.0)

# collection of purchases and user which requested them
class ConfirmedBasket(models.Model):

    
    purchases = models.ManyToManyField(Purchase)
    total_cost = models.FloatField(default = 0.0)

    def as_dict(self):

        output = {"purchases": [], "total_cost": self.total_cost}

        for purchase in self.purchases.all():
            output["purchases"].append(
                {
                    "strain_id": purchase.strain.pk,
                    "strain_name": purchase.strain.name,
                    "quantity": purchase.quantity,
                    "cost": purchase.cost
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

    FUNDING_TYPES = (
        ("NC", "Non-Commercial"),
        ("B", "BBSRC"),
        ("I", "Industry"),
        ("UB", "Internal UoB"),
        ("NS", "Not Set")
    )
    
    status = models.CharField(
        default = "P",
        choices = STATUS_CHOICES,
        max_length = 1
    )

    customer_name = models.CharField(max_length = 100, null = True)
    customer_email = models.EmailField(null = True)
    basket = models.OneToOneField(ConfirmedBasket, null = True)
    funding_type = models.CharField(max_length = 2, choices = FUNDING_TYPES, default = "NS")
    bbsrc_code = models.CharField(max_length = 10, null = True)

    billing_address = models.TextField(default = "")
    delivery_address = models.TextField(default = "")
    customer_note = models.TextField(default = "")

    creation_date = models.DateTimeField(default = datetime.now)


    def get_verbose_funding_type_name(self):

        return self.get_funding_type_display()

    def get_verbose_status_name(self):

        return self.get_status_display()


# represents dispatched product/order status
class Order(models.Model):

    STATUS_CHOICES = (
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


    start_date = models.DateTimeField(default = datetime.now)
    post_date = models.DateTimeField(null = True)
    received_date = models.DateTimeField(null = True)


    def get_verbose_status_name(self):

        return self.get_status_display()
