# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from archive.models import Strain
from django.contrib.auth.models import User
from cart.models import Quote, Order, ConfirmedBasket, Purchase


def get_order_details(request, order_pk):

    try:
    
        order = Order.objects.get(pk = order_pk)
    
    except Order.DoesNotExist:
    
        messages.error(request, "Details for quote could not be located")
        order = None
    
    else:

        order_data = {

        }
        

    return HttpResponse(
        json.dumps(order_data),
        content_type = "application/json"
    )

def get_quote_details(request, quote_pk):

    try:
    
        quote = Quote.objects.get(pk = quote_pk)
    
    except Quote.DoesNotExist:
    
        messages.error(request, "Details for quote could not be located")
        quote = None
    
    else:

        quote_data = {
            "customer_name": quote.customer_name,
            "customer_email": quote.customer_email,
            "funding_Type": quote.funding_type,
            "bbsrc_code": quote.bbsrc_code,
            "billing_address": quote.billing_address,
            "selivery_address": quote.delivery_address,
            "customer_notes": quote.customer_note
        }
        

    return HttpResponse(
        json.dumps(quote_data),
        content_type = "application/json"
    )





def management_dashboard(request):

    

    return render(
        request,
        "management/dashboard.html",
        {

        }
    )


def management_strains(request):



    return render(
        request,
        "management/strains.html",
        {
            "strains": Strain.objects.all()
        }
    )


def management_sales(request):

    return render(
        request,
        "management/sales.html",
        {
            "quotes": Quote.objects.all()
        }
    )


def management_users(request):

    return render(
        request,
        "management/users.html",
        {
            "users": User.objects.all()
        }
    )