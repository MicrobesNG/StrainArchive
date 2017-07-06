# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from archive.models import Strain
from . forms import QuoteForm
from . import basket_utils
from . import promo_utils
from . models import Promotion, PromotionCode
import json
from datetime import datetime


def checkout_complete(request):

    return render(request, "cart/checkoutSuccess.html", {})


# generates an empty basket (dict) and sets session basket to new empty basket
def clear_basket(request):

    # generate empty basket and set session basket
    request.session["basket"] = basket_utils.generate_empty_basket()
    request.session.modified = True

    # return empty basket to page
    return HttpResponse(
        json.dumps(request.session["basket"]),
        content_type = "application/json"
    )


def cancel_promotion(request, promotion_code):

    try:

        promotion_code = PromotionCode.objects.get(code = promotion_code)

    except PromotionCode.DoesNotExist:

        # code does not exist
        data = {"status": "NOT_FOUND"}

    else:

        promotion_code.number_of_uses -= 1
        promotion_code.save()
        request.session["basket"]["promotion"] = {
            "promotion_code": "",
            "promotion_pk": "",
            "promotion_total_cost": 0.0
        }

        request.session.modified = True

        data = {"status": "SUCCESS", "basket": request.session["basket"]}


    return HttpResponse(
        json.dumps(data),
        content_type = "application/json"
    )


    # return basket and status to the page
    return HttpResponse(
        json.dumps(data),
        content_type = "application/json"
    )


# applies promotion code to basket
# returns promotion status and basket
def check_promotion(request, promotion_code):

    # attempt to find promotion code in database
    try:

        promotion_code = PromotionCode.objects.get(code = promotion_code)

    except PromotionCode.DoesNotExist:

        # code does not exist
        data = {"status": "NOT_FOUND"}

    else:

        if promotion_code.promotion.expired:

            # promotion has expired
            data = {"status": "EXPIRED"}

        elif promotion_code.promotion.start_date > datetime.now().date():

            # promotion is not yet running
            data = {"status": "NOT_YET_RUNNING"}
        
        elif promotion_code.check_usage_limit_hit():

            # code has reached usage limit
            data = {"status": "USEAGE_LIMIT"}
        
        elif not promotion_code.active:

            # code is not active
            data = {"status": "INACTIVE"}

        else:

            # if code is valid and active, apply to basket
            promo_utils.apply_code_to_session_basket(request, promotion_code)
            
            promotion_code.save()

            remaining_usages = promotion_code.max_usages - promotion_code.number_of_uses

            # code has been applied successfully
            data = {
                "status": "SUCCESS",
                "basket": request.session["basket"],
                "promo_name": promotion_code.promotion.name,
                "promo_description": promotion_code.promotion.description,
                "remaining_usages": remaining_usages
            }

        # return basket and status to the page
        return HttpResponse(
            json.dumps(data),
            content_type = "application/json"
        )


# adds strain to session basket
def add_to_basket(request, strain_pk):
    
    # try and find strain in database
    try:

        selected_strain = Strain.objects.get(pk = strain_pk)

    except Strain.DoesNotExist:

        pass

    else:

        # add strain to session basket
        basket_utils.add_to_basket(request, selected_strain)

        # recalculate cost and update session basket
        basket_utils.set_basket_cost(request)


    # return basket to the page
    return HttpResponse(
        json.dumps(request.session["basket"]),
        content_type = "application/json"
    )


# remove strain from session basket
def remove_from_basket(request, strain_pk):

    # try to find strain in database
    try:

        selected_strain = Strain.objects.get(pk = strain_pk)
    
    except Strain.DoesNotExist:

        pass

    else:

        # remove strain from session basket
        basket_utils.remove_from_basket(request, selected_strain)

        # recalculate cost and update session basket
        basket_utils.set_basket_cost(request)

    # return basket to page
    return HttpResponse(
        json.dumps(request.session["basket"]),
        content_type = "application/json"
    )


# render the checkout page and handle quote requests
def checkout(request):

    if request.method == "POST":

        quote_form = QuoteForm(request.POST)

        if quote_form.is_valid():

            quote_form.process(request)
        
        else:

            quote_form.process_errors(request)
    
    else:

        quote_form = QuoteForm()

    return render(
        request,
        "cart/checkout.html",
        {
            "quote_form": quote_form,
            "basket": request.session["basket"]
        }
    )