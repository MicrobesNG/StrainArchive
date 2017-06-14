from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from . views import *
import json



class LoginForm(forms.Form):

    username = forms.CharField(required = True)
    password = forms.CharField(required = True)

    def process_form(self, request):

        cleaned_username = self.cleaned_data["username"]
        cleaned_password = self.cleaned_data["password"]

        user = authenticate(cleaned_username, cleaned_password)

        if user:
            
            if user.is_active:
                
                return redirect("userprofile:dashboard")
            
            else:

                messages.info(request, "Account not activated.")
        
        else:

            messages.error(request, "Username or password was incorrect.")




    def process_errors(self, request):

        error_dict = json.loads(self.errors.as_json())
        for key in error_dict:
            for error in error_dict[key]:
                messages.error(request, "Error: %s - %s" % (key, error["message"]))