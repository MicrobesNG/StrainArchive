from django import forms

from django.contrib import messages
from cart.models import Quote

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