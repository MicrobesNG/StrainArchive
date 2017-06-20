# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from archive.models import Strain
from . import utils

import json


def add_to_basket(request, strain_pk):
    
    try:

        selected_strain = Strain.objects.get(pk = strain_pk)

    except Strain.DoesNotExist:

        pass

    else:

        utils.add_to_basket(request, selected_strain)

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

        utils.remove_from_basket(request, selected_strain)

    return HttpResponse(
        json.dumps(request.session["basket"]),
        content_type = "application/json"
    )