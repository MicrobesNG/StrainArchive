# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from archive.models import Strain
from datetime import datetime
import json


class PromotionCode(models.Model):

    code = models.CharField(max_length = 10, unique = True)
    max_usages = models.IntegerField(default = 1)



class Promotion(models.Model):

    code = models.ManyToManyField(PromotionCode)
    description = models.TextField(null = True)
    start_date = models.DateField(default = datetime.now)
    expiry_date = models.DateField(null = True)
    





# how many of which strain to be purchased
class Purchase(models.Model):

    # which strain, how many, and total cost for purchase
    strain = models.ForeignKey(Strain)
    quantity = models.IntegerField(default = 0)
    cost = models.FloatField(default = 0.0)

# collection of purchases and user which requested them
class ConfirmedBasket(models.Model):

    # purchases in order and summed cost for all of them
    purchases = models.ManyToManyField(Purchase)
    total_cost = models.FloatField(default = 0.0)

    # put data for basket into dict
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

    # serialize basket into json string
    def as_json_string(self):

        return json.dumps(self.as_dict())


# quote for cost of basket
class Quote(models.Model):

    # status of quote
    STATUS_CHOICES = (
        ("P", "Pending"),
        ("S", "Sent"),
        ("A", "Accepted"),
        ("R", "Rejected"),
        ("C", "Cancelled")
    )

    # available types of funding
    FUNDING_TYPES = (
        ("NC", "Non-Commercial"),
        ("B", "BBSRC"),
        ("I", "Industry"),
        ("UB", "Internal UoB"),
        ("NS", "Not Set")
    )
    
    status = models.CharField(default = "P", choices = STATUS_CHOICES, max_length = 1)
    funding_type = models.CharField(max_length = 2, choices = FUNDING_TYPES, default = "NS")

    # bbsrc funding code (required if bbsrc funding put on quote)
    bbsrc_code = models.CharField(max_length = 10, null = True)
    
    # customer details
    # (note can be attached to quote by customer)
    customer_name = models.CharField(max_length = 100, null = True)
    customer_email = models.EmailField(null = True)
    customer_note = models.TextField(default = "")

    # basket for which quote relates to
    basket = models.OneToOneField(ConfirmedBasket, null = True)
    
    # addresses
    billing_address = models.TextField(default = "")
    delivery_address = models.TextField(default = "")
    
    # date at which quote was created
    creation_date = models.DateTimeField(default = datetime.now)

    # get display names for funding type and status
    def get_verbose_funding_type_name(self):

        return self.get_funding_type_display()

    def get_verbose_status_name(self):

        return self.get_status_display()


# represents dispatched product/order status
class Order(models.Model):

    # status of order
    STATUS_CHOICES = (
        ("P", "Processing"),
        ("D", "Dispatched"),
        ("R", "Received"),
        ("V", "Void")
    )

    status = models.CharField(
        default = "A",
        choices = STATUS_CHOICES,
        max_length = 1
    )

    # quote for which order is for
    quote = models.OneToOneField(Quote, null = True)

    # dates for each stage of order
    start_date = models.DateTimeField(default = datetime.now)
    post_date = models.DateTimeField(null = True)
    received_date = models.DateTimeField(null = True)

    # get display name for order status
    def get_verbose_status_name(self):

        return self.get_status_display()
