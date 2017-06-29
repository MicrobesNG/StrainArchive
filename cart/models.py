# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from archive.models import Strain
from datetime import datetime
import json



class Promotion(models.Model):

    PROMOTION_TYPES = (
        ("FPR", "Fixed Price Reduction"),
        ("PPR", "Percentage Reduction"),
        ("NS", "Not Set")
    )

    name = models.CharField(max_length = 50)
    description = models.TextField(null = True)

    start_date = models.DateField(default = datetime.now)
    expiry_date = models.DateField(null = True)

    expired = models.BooleanField(default = False)
    promotion_parameters = models.TextField(null = True)
    promotion_type = models.CharField(max_length = 4, choices = PROMOTION_TYPES, default = "NS")

    def get_verbose_promotion_type_name(self):

        return self.get_promotion_type_display()

    def check_expiry_date(self):

        if datetime.now().date() >= self.expiry_date.date():

            return True
        
        else:

            return False
    
    def update_expiry_date(self):

        if self.check_expiry_date():

            self.expired = True
        
        else:

            self.expired = False
        
        self.save()


class PromotionCode(models.Model):

    code = models.CharField(max_length = 10, unique = True)
    max_usages = models.IntegerField(default = 1)
    number_of_uses = models.IntegerField(default = 0)
    active = models.BooleanField(default = True)

    promotion = models.ForeignKey(Promotion, null = True)






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


class PaymentOrder(models.Model):
    
    # numbers stored as char fields so large ints dont need to be stored
    reference_number = models.CharField(max_length = 30, null = True)
    pdf = models.FileField(null = True)


class ShopOrder(models.Model):

    # numbers stored as char fields so large ints dont need to be stored
    order_number = models.CharField(max_length = 30, null = True)
    transaction_number = models.CharField(max_length = 30, null = True)


# represents dispatched product/order status
class Order(models.Model):

    # status of order
    STATUS_CHOICES = (
        ("PP", "Pending Payment"),
        ("P", "Processing"),
        ("AD", "Awaiting Dispatch"),
        ("D", "Dispatched"),
        ("R", "Received"),
        ("V", "Void")
    )

    PAYMENT_METHODS = (
        ("PO", "Payment Order"),
        ("OS", "Online Shop"),
        ("NS", "Not Set")
    )

    status = models.CharField(
        default = "PP",
        choices = STATUS_CHOICES,
        max_length = 2
    )

    payment_method = models.CharField(
        default = "NS",
        choices = PAYMENT_METHODS,
        max_length = 2
    )

    # quote for which order is for
    quote = models.OneToOneField(Quote, null = True)

    # dates for each stage of order
    start_date = models.DateTimeField(default = datetime.now)
    post_date = models.DateTimeField(null = True)
    received_date = models.DateTimeField(null = True)

    cirms_number = models.CharField(max_length = 30, null = True)
    
    finance_reference_number = models.CharField(max_length = 30, null = True)
    payment_order = models.OneToOneField(PaymentOrder, null = True)
    shop_order = models.OneToOneField(ShopOrder, null = True)


    # get the display name for the payment type
    def get_verbose_payment_method_name(self):

        return self.get_payment_method_display()

    # get display name for order status
    def get_verbose_status_name(self):

        return self.get_status_display()