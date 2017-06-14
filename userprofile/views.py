# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . forms import LoginForm

def user_dashboard(request):

    return render(request, "userprofile/dashboard.html", {})



def login_page(request):

    if request.method == "POST":

        login_form = LoginForm(request.POST)

        if login_form.is_valid():

            login_form.process_form(request)

        else:

            login_form.process_errors(request)
    
    else:

        login_form = LoginForm()

    return render(
        request,
        "userprofile/login.html",
        {
            "login_form": login_form
        }
    )