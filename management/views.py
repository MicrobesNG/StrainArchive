# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers
from archive.models import Strain
from django.contrib.auth.models import User
from cart.models import Quote, Order, ConfirmedBasket, Purchase


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