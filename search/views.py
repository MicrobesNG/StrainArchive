# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from archive.models import Strain, Family, Genus, Species
from . forms import SearchParameterForm
import json

def search(request):

    if request.method == "POST":

        searchParameterForm = SearchParameterForm(request.POST)

        if searchParameterForm.is_valid():

            searchParameterForm.process(request)
        
        else:

            searchParameterForm.process_errors(request)
    
    else:

        searchParameterForm = SearchParameterForm()



    if Family.objects.all().count() > 0:
        
        data = {"data": []}

        for family in Family.objects.all():

            data["data"].append(family.to_dict())
    
    else: 

        data = {"data": "EMPTY"}

    return render(
        request,
        "search/search.html",
        {
            "data": json.dumps(data)
        }
    )


def results(request):


    return render(request, "search/results.html", {})


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