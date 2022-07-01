from django.forms import ModelForm
from django import forms
from django.forms import modelformset_factory, formset_factory
from .models import TreatedAnimal, Prescription

import re


class TreatedAnimalsForm(ModelForm):

    class Meta:
        textAreaSize = "height: 100px;"
        model = TreatedAnimal
        fields = "__all__"

        widgets = {
            'case_number': forms.Select(attrs={'class': 'form-control'}),
            't0': forms.NumberInput(attrs={'class': 'form-control'}),
            'pr': forms.NumberInput(attrs={'class': 'form-control'}),
            'rr': forms.NumberInput(attrs={'class': 'form-control'}),
            'clinical_finding': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
            'dx': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'differential_diag': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
            'rumen_motility': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
        }

    # Add form validation
class PrescriptionForm(ModelForm):       
    class Meta:
        model = Prescription
        exclude = ["paid"]

        widgets = {
            'rx': forms.Select(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'treatment': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control','type': 'hidden'}),
        }
    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity < 1:
            raise forms.ValidationError(
                "Quantity must be greater than 0!!")
        return quantity

    def clean_total(self):
        quantity = self.cleaned_data.get("quantity")
        print(f"Quantity: {quantity}")
        rx_price = self.cleaned_data.get("rx").price
        print(f"RX Price: {rx_price}")
        total = quantity * rx_price
        print(f"Total: {total}")
        return total
        
PrescriptionFormSet = formset_factory(PrescriptionForm,extra=0)
#PrescriptionFormSet = modelformset_factory(Prescription,form=PrescriptionForm,extra=1)
