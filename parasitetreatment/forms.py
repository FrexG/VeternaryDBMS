from django.forms import ModelForm
from django import forms
from django.forms import modelformset_factory,formset_factory

from .models import ParasitePrescription
from .models import ParasiteTreatment
from registernewuser.models import Customer
import re

class ParasiteTreatmentForm(ModelForm):
     class Meta:
        textAreaSize = "height: 100px;"
        model = ParasiteTreatment
        exclude = ['service_date','unit']

        widgets = {
            'case_number': forms.Select(attrs={'class': 'form-control'}),
            'treatment_type': forms.Select(attrs={'class': 'form-control'}),
            'dx': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'case_holder': forms.Select(attrs={'class': 'form-control'}),
        }

    # Add form validation
class PrescriptionForm(ModelForm):       
    class Meta:
        model = ParasitePrescription
        exclude = ["paid","delivered"]

        widgets = {
            'rx': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control','required':'True'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control','required':'True'}),
            'treatment': forms.Select(attrs={'class': 'form-control', 'type': 'hidden'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'type': 'hidden'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity < 1:
            raise forms.ValidationError(
                "Quantity must be greater than 0!!")
        return quantity

    def clean_total(self):
        quantity = self.cleaned_data.get("quantity")
        rx_price = self.cleaned_data.get("rx").dis_price

        print(f"RX price = {rx_price}")

        total = quantity * rx_price
        print(f"Total = {total}")
        return total
    
PrescriptionFormSet = formset_factory(form=PrescriptionForm,extra=0)
#PrescriptionFormSet = modelformset_factory(ParasitePrescription,form=PrescriptionForm,extra=1)