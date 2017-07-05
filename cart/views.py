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


def clear_basket(request):

    request.session["basket"] = basket_utils.generate_empty_basket()
    request.session.modified = True

    return HttpResponse(
        json.dumps(request.session["basket"]),
        content_type = "application/json"
    )


def apply_promotion(request, promotion_code):


    try:

        promotion_code = PromotionCode.objects.get(code = promotion_code)

    except PromotionCode.DoesNotExist:

        data = {"status": "NOT_FOUND"}

    else:

        if promotion_code.promotion.expired:

            data = {"status": "EXPIRED"}
        
        elif promotion_code.check_usage_limit_hit():

            data = {"status": "USEAGE_LIMIT"}
        
        elif not promotion_code.active:

            data = {"status": "INACTIVE"}

        else:

            promo_utils.apply_code_to_session_basket(request, promotion_code)

            data = {"status": "SUCCESS", "basket": request.session["basket"]}

            return HttpResponse(
                json.dumps(data),
                content_type = "application/json"
            )




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


def add_to_basket(request, strain_pk):
    
    try:

        selected_strain = Strain.objects.get(pk = strain_pk)

    except Strain.DoesNotExist:

        pass

    else:

        basket_utils.add_to_basket(request, selected_strain)
        cart.basket_utils.set_basket_cost(request)


    return HttpResponse(
        json.dumps(request.session["basket"]),
        content_type = "application/json"
    )





def remove_from_basket(request, strain_pk):

    try:

        selected_strain = Strain.objects.get(pk = strain_pk)
    
    except Strain.DoesNotExist:

        pass

    else:

        cart.basket_utils.remove_from_basket(request, selected_strain)
        cart.basket_utils.set_basket_cost(request)


    return HttpResponse(
        json.dumps(request.session["basket"]),
        content_type = "application/json"
    )