from django import forms
from archive.models import Strain


class RemoveFromBasket(forms.Form):

    strain_pk = forms.IntegerField(required = True)

    def process(self, request):
        
        cleaned_strain_pk = self.cleaned_data["strain_pk"]

        try:

            strain = Strain.objects.get(pk = cleaned_strain_pk)

        except Strain.DoesNotExist:

            pass

        else:

            for strain in request.session["basket"]["items"]:

                pass




class AddToBasket(forms.Form):

    strain_pk = forms.IntegerField(required = True)

    def process(self, request):

        cleaned_strain_pk = self.cleaned_data["strain_pk"]

        try:

            strain = Strain.objects.get(pk = cleaned_strain_pk)

        except Strain.DoesNotExist:

            pass

        else:
        
            pass

