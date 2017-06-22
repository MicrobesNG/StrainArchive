from django import forms
from django.conf import messages
from archive.models import Strain
from . models import Quote
import json

class QuoteForm(forms.Form):

    FUNDING_TYPES = (
        ("NC", "Non-Commercial"),
        ("B", "BBSRC"),
        ("I", "Industry"),
        ("UB", "Internal UoB")
    )

    customer_name = forms.CharField(max_length = 100, required = True)
    email = forms.EmailField(required = True)
    billing_address = forms.CharField(required = True, max_length = 200)
    delivery_address = forms.CharField(required = True, max_length = 200)
    funding_type = forms.CharField(required = True, max_length = 2)
    bbsrc_code = forms.CharField(required = False, max_length = 10)
    note = forms.CharField(required = False, max_length = 250)

    
    def process(self, request):

        cleaned_name = self.cleaned_data["name"]
        cleaned_email = self.cleaned_data["email"]
        cleaned_billing_address = self.cleaned_data["billing_address"]
        cleaned_delivery_address = self.cleaned_data["delivery_address"]
        cleaned_funding_type = self.cleaned_data["funding_type"]
        cleaned_bbsrc_code = self.cleaned_data["bbsrc_code"]
        cleaned_note = self.cleaned_data["note"]

        if cleaned_funding_type == "B":
            
            if not cleaned_bbsrc_code:
                
                messages.error(request, "BBSRC Code is needed for BBSRC funded purchases.")

            else:

                newQuote = Quote.objects.create(
                    customer_name = cleaned_name,
                    customer_email = cleaned_email,
                    funding_type = cleaned_funding_type,
                    bbsrc_code = cleaned_bbsrc_code,
                    billing_address = cleaned_billing_address,
                    delivery_address = cleaned_delivery_address
                )
        
        else:

            newQuote = Quote.objects.create(
                customer_name = cleaned_name,
                customer_email = cleaned_email,
                funding_type = cleaned_funding_type,
                billing_address = cleaned_billing_address,
                delivery_address = cleaned_delivery_address
            )

        if cleaned_note:
            newQuote.customer_note = cleaned_note
        

        newQuote.save()
        





        

    
    def process_errors(self, request):
        
        error_dict = json.loads(self.errors.as_json())
        for key in error_dict:
            for error in error_dict[key]:
                messages.error(request, "Error: %s - %s" % (key, error["message"]))