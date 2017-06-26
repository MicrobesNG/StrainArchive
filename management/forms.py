from django import forms

from django.contrib import messages
from cart.models import Quote, Promotion
from datetime import datetime



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
        
        if cleaned_start_date:

            Promotion.objects.create(
                name = cleaned_name,
                description = cleaned_description,
                start_date = datetime.strptime(cleaned_start_date, "%d/%m/%Y"),
                expiry_date = datetime.strptime(cleaned_expiry_date, "%d/%m/%Y")
            )

            messages.success(
                request,
                "New promotion '%s' has been created successfully and will be active as of %s." % (cleaned_name, cleaned_start_date)
            )
        
        else:

            Promotion.objects.create(
                name = cleaned_name,
                description = cleaned_description,
                expiry_date = datetime.strptime(cleaned_expiry_date, "%d/%m/%Y")
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