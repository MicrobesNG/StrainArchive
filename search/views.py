# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from archive.models import Strain


def search(request):

    return render(request, "search/search.html", {})


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