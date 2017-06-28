# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from archive.models import Strain
from . forms import QuoteForm
from . import basket_utils

import json


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