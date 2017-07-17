# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from archive.models import Strain
from . forms import SearchParameterForm, BlastSearchForm
import cart.basket_utils
import json
import os.path

from django.contrib.staticfiles.templatetags.staticfiles import static


def results(request, page_number):
    
    basket = cart.basket_utils.get_basket(request)
    
    paginator = Paginator(request.session["search_results"], 25)

    page = request.GET.get("page")

    try:

        strains = paginator.page(page)
    
    except PageNotAnInteger:

        strains = paginator.page(page_number)

    except EmptyPage:

        strains = paginator.page(paginator.num_pages)


    return render(
        request,
        "search/results.html",
        {
            "strains": strains,
            "num_pages": range(paginator.num_pages),
            "basket": basket
        }
    )



def search(request):

    if request.method == "POST":

        blastSearchForm = BlastSearchForm(request.POST)

        if blastSearchForm.is_valid():

            blastSearchForm.process(request)

            return redirect("search:results", 1)

        else:

            blastSearchForm.process_errors(request)
    
    else:

        blastSearchForm = BlastSearchForm()


    data = {"data": "EMPTY"}
    
    
    with open("search/world_50m.json") as j_file:
        world_json = json.load(j_file)

    return render(
        request,
        "search/search.html",
        {
            "blastSearchForm": blastSearchForm,
            "data": json.dumps(data),
            "world_data": json.dumps(world_json)
        }
    )





def details(request, strain_pk):

    try:

        selected_strain = Strain.objects.get(pk = strain_pk)
    
    except Strain.DoesNotExist:

        raise Http404("Can't find the strain with id %d." % strain_pk)
    
    else:
        
        return render(
            request,
            "search/details.html",
            {
                "selected_strain": selected_strain
            }
        )