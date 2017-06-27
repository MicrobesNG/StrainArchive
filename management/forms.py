from django import forms

from django.contrib import messages
from cart.models import Quote, Promotion
import json


class GenerateNewCodes(forms.Form):

    number_of_codes = forms.IntegerField(required = True)
    max_number_of_uses = forms.IntegerField(required = True)
    initially_active = forms.BooleanField(required = True)
    promo_pk = forms.IntegerField(required = True)

    def process(self, request);

        cleaned_number_of_codes = self.cleaned_data["number_of_codes"]
        cleaned_max_number_of_uses = self.cleaned_data["max_number_of_uses"]
        cleaned_initially_active = self.cleaned_data["initially_active"]
        cleaned_promo_pk = self.cleaned_data["promo_pk"]

        try:

            promotion = Promotion.objects.get(pk = cleaned_promo_pk)
        
        except Promotion.DoesNotExist:

            messages.error(request, "Promotion with id %d could not be found." % cleaned_promo_pk)
        
        else:

            generate_codes_for_promotion(
                cleaned_promo_pk,
                cleaned_number_of_codes,
                cleaned_max_number_of_uses,
                cleaned_initially_active
            )

            messages.success(request, "The codes were generated successfully.")
    
    def process_errors(self, request):
        
        error_dict = json.loads(self.errors.as_json())
        for key in error_dict:
            for error in error_dict[key]:
                messages.error(request, "Error: %s - %s" % (key, error["message"]))



class CreateNewPromotionForm(forms.Form):

    name = forms.CharField(max_length = 50, required = True)
    description = forms.CharField(max_length = 200, required = True)
    start_date = forms.DateField(required = True)
    expiry_date = forms.DateField(required = True)

    def process(self, request):

        cleaned_name = self.cleaned_data["name"]
        cleaned_description = self.cleaned_data["description"]
        cleaned_start_date = self.cleaned_data["start_date"]
        cleaned_expiry_date = self.cleaned_data["expiry_date"]

        print cleaned_start_date, type(cleaned_start_date)

        if cleaned_start_date:

            Promotion.objects.create(
                name = cleaned_name,
                description = cleaned_description,
                start_date = cleaned_start_date,
                expiry_date = cleaned_expiry_date
            )

            messages.success(
                request,
                "New promotion '%s' has been created successfully and will be active as of %s." % (cleaned_name, cleaned_start_date)
            )
        
        else:

            Promotion.objects.create(
                name = cleaned_name,
                description = cleaned_description,
                expiry_date = cleaned_expiry_date
            )

            messages.success(
                request,
                "New promotion '%s' has been created successfully and will be active as of today." % cleaned_name
            )
    

    def process_errors(self, request):

        error_dict = json.loads(self.errors.as_json())
        for key in error_dict:
            for error in error_dict[key]:
                messages.error(request, "Error: %s - %s" % (key, error["message"]))

        


class QuoteForm(forms.Form):

    selected_quote_id = forms.IntegerField(required = True)
    cost = forms.FloatField(required = False)


    def process(self, request):

        cleaned_selected_quote_id = self.cleaned_data["selected_quote_id"]
        cleaned_cost = self.cleaned_data["cost"]

        try:

            selected_quote = Quote.objects.get(pk = cleaned_selected_quote_id)
        
        except Quote.DoesNotExist:

            messages.error(request, "Quote with id %d could not be found in the database." % cleaned_selected_quote_id)
        
        else:

            selected_quote.cost = cleaned_cost
            selected_quote.save()

            messages.success(request, "Changes to quote %d were made successfully." % cleaned_selected_quote_id)



    def process_errors(self, request):

        error_dict = json.loads(self.errors.as_json())
        for key in error_dict:
            for error in error_dict[key]:
                messages.error(request, "Error: %s - %s" % (key, error["message"]))