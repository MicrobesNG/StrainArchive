# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from archive.models import Strain
from django.contrib.auth.models import User
from cart.models import Quote, Order, ConfirmedBasket, Purchase, Promotion, PromotionCode
from forms import CreateNewPromotionForm, GenerateNewCodesForm
from django.http import HttpResponse
import json

# view to get and return promotional codes for promotion with pk == promotion_pk
def get_promo_codes(request, promo_pk):

    # try to find promotino
    try:

        promo = Promotion.objects.get(pk = promo_pk)
    
    except Promotion.DoesNotExist:

        pass
    
    else:

        # generate list of dicts with data for each code
        codes = [
            {
                "pk": code.pk,
                "code": code.code,
                "number_of_uses": code.number_of_uses,
                "max_usages": code.max_usages,
                "active": code.active
            } for code in promo.promotioncode_set.all()
        ]
    
    # send data back to page
    return HttpResponse(
        json.dumps(codes),
        content_type = "application/json"
    )




# view to get order details
def get_order_details(request, order_pk):

    # check order exists
    try:
    
        order = Order.objects.get(pk = order_pk)
    
    except Order.DoesNotExist:
        
        # process case if order not existing
        messages.error(request, "Details for quote could not be located")
        order = None
    
    else:

        order_data = {

        }
        

    return HttpResponse(
        json.dumps(order_data),
        content_type = "application/json"
    )

# view to get quote details
def get_quote_details(request, quote_pk):

    # check quote exists
    try:
    
        quote = Quote.objects.get(pk = quote_pk)
    
    except Quote.DoesNotExist:
        
        # process case if quote not existing
        messages.error(request, "Details for quote could not be located")
        quote = None
    
    else:

        # create dict representing quote
        quote_data = {
            "customer_name": quote.customer_name,
            "customer_email": quote.customer_email,
            "funding_type": quote.get_verbose_funding_type_name(),
            "billing_address": quote.billing_address,
            "delivery_address": quote.delivery_address,
            "customer_notes": quote.customer_note
        }

        # if bbsrc code present, add to dict
        if quote.bbsrc_code:
            quote_data["bbsrc_code"] = quote.bbsrc_code
        else:
            quote_data["bbsrc_code"] = ""
        
        # check existence of basket and add to dict
        if quote.basket:
            quote_data["basket"] = quote.basket.as_dict()
        else:
            quote_data["basket"] = ""

    return HttpResponse(
        json.dumps(quote_data),
        content_type = "application/json"
    )




# management dashboard view
def management_dashboard(request):


    return render(
        request,
        "management/dashboard.html",
        {

        }
    )

# strain management view
def management_strains(request):

    return render(
        request,
        "management/strains.html",
        {
            "strains": Strain.objects.all()
        }
    )




# sales management view
def management_sales(request):

    createNewPromotionForm = CreateNewPromotionForm()
    generateCodesForm = GenerateNewCodesForm()

    if request.method == "POST":

        print request.POST
        
        if "generateCodesForm" in request.POST:

            generateCodesForm = GenerateNewCodesForm(request.POST)

            if generateCodesForm.is_valid():

                generateCodesForm.process(request)
            
            else:

                generateCodesForm.process_errors(request)

        if "createNewPromotionForm" in request.POST:

            createNewPromotionForm = CreateNewPromotionForm(request.POST)

            if createNewPromotionForm.is_valid():

                createNewPromotionForm.process(request)
            
            else:

                createNewPromotionForm.process_errors(request)
    

    return render(
        request,
        "management/sales.html",
        {
            "generateCodesForm": GenerateNewCodesForm,
            "createNewPromotionForm": createNewPromotionForm,
            "quotes": Quote.objects.all(),
            "promotions": Promotion.objects.all()
        }
    )



# user management view
def management_users(request):

    return render(
        request,
        "management/users.html",
        {
            "users": User.objects.all()
        }
    )