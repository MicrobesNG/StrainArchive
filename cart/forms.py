from django import forms
from django.contrib import messages
from archive.models import Strain
from . models import Quote
import json
import cart.basket_utils

class QuoteForm(forms.Form):

    # verbose name mappings for funding types
    FUNDING_TYPES = (
        ("NC", "Non-Commercial"),
        ("B", "BBSRC"),
        ("I", "Industry"),
        ("UB", "Internal UoB")
    )

    # form fields
    customer_name = forms.CharField(max_length = 100, required = True)
    email = forms.EmailField(required = True)
    billing_address = forms.CharField(required = True, max_length = 200)
    delivery_address = forms.CharField(required = True, max_length = 200)
    funding_type = forms.CharField(required = True, max_length = 2)
    bbsrc_code = forms.CharField(required = False, max_length = 10)
    note = forms.CharField(required = False, max_length = 250)

    # clean the data and process the form
    def process(self, request):

        # get cleaned data
        cleaned_name = self.cleaned_data["customer_name"]
        cleaned_email = self.cleaned_data["email"]
        cleaned_billing_address = self.cleaned_data["billing_address"]
        cleaned_delivery_address = self.cleaned_data["delivery_address"]
        cleaned_funding_type = self.cleaned_data["funding_type"]
        cleaned_bbsrc_code = self.cleaned_data["bbsrc_code"]
        cleaned_note = self.cleaned_data["note"]

        # if needed, make sure that a BBSRC code has been given
        if cleaned_funding_type == "B":
            
            if not cleaned_bbsrc_code:
                
                messages.error(request, "BBSRC Code is needed for BBSRC funded purchases.")

            else:

                # create BBSRC funded quote
                newQuote = Quote.objects.create(
                    customer_name = cleaned_name,
                    customer_email = cleaned_email,
                    funding_type = cleaned_funding_type,
                    bbsrc_code = cleaned_bbsrc_code,
                    billing_address = cleaned_billing_address,
                    delivery_address = cleaned_delivery_address
                )
        
        else:

            # create non-BBSRC funded quote
            newQuote = Quote.objects.create(
                customer_name = cleaned_name,
                customer_email = cleaned_email,
                funding_type = cleaned_funding_type,
                billing_address = cleaned_billing_address,
                delivery_address = cleaned_delivery_address
            )

        # add the note if one was submitted
        if cleaned_note:
            newQuote.customer_note = cleaned_note

        # save the session basket to the database
        confirmed_basket = cart.basket_utils.save_session_basket_to_db(request)

        # add the basket to the quote and save
        newQuote.basket = confirmed_basket
        newQuote.save()

        # clear the session basket
        request.session["basket"] = cart.basket_utils.generate_empty_basket()
        request.session.modified = True
        

    def process_errors(self, request):
        
        error_dict = json.loads(self.errors.as_json())
        for key in error_dict:
            for error in error_dict[key]:
                messages.error(request, "Error: %s - %s" % (key, error["message"]))