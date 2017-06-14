# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def search(request):

    return render(request, "search/search.html", {})


def results(request):


    return render(request, "search/results.html", {})


def details(request, strain_id):

    return render(request, "search/details.html", {})