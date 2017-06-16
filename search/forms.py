from django import forms
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import json



class SearchParameterForm(forms.Form):

    selected_family_ids = forms.CharField(max_length = None)
    selected_genus_ids = forms.CharField(max_length = None)
    selected_species_ids = forms.CharField(max_length = None)

    def process(self, request):

        cleaned_family_ids = self.cleaned_data["selected_family_ids"]
        cleaned_genus_ids = self.cleaned_data["selected_genus_ids"]
        cleaned_species_ids = self.cleaned_data["selected_species_ids"]


        payload = {
            "families": cleaned_family_ids,
            "genera": cleaned_genus_ids,
            "species": cleaned_species_ids
        }

        return HttpResponseRedirect("/search/results/" + json.dumps(payload))
        # return redirect("search.views.results", parameterString = json.dumps(payload))

        
    
    def process_errors(self, request):

        error_dict = json.loads(self.errors.as_json())
        for key in error_dict:
            for error in error_dict[key]:
                messages.error(request, "Error: %s - %s" % (key, error["message"]))