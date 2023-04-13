from dataclasses import fields
from django.forms import ModelForm
from django import forms
from django.forms import modelformset_factory, formset_factory
from .models import TreatedAnimal,Treatment,Prescription
from registernewuser.models import Customer
import re

class TreatedAnimalsForm(ModelForm):
    class Meta:
        textAreaSize = "height: 100px;"
        model = TreatedAnimal
        fields = "__all__"

        widgets = {
            'case_number': forms.Select(attrs={'class': 'form-control'}),
            'species': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.Select(attrs={'class': 'form-control'}),
            'number_of_animals': forms.NumberInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'history': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
            'case_holder': forms.Select(attrs={'class': 'form-control'}),
        }

class TreatmentForm(ModelForm):
    class Meta:
        textAreaSize = "height: 100px;"
        model = Treatment
        exclude = ["paid","delivered"]

        widgets = {
            'treatment_id': forms.Select(attrs={'class': 'form-control'}),
            't0': forms.NumberInput(attrs={'class': 'form-control'}),
            'pr': forms.NumberInput(attrs={'class': 'form-control'}),
            'rr': forms.NumberInput(attrs={'class': 'form-control'}),
            'clinical_finding': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
            'dx': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'differential_diag': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
            'rumen_motility': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
        }
class PrescriptionForm(ModelForm):       
    class Meta:
        model = Prescription
        fields = "__all__"

        widgets = {
            'rx': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control','required':'True'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control','required':'True'}),
            'treatment': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control','type': 'hidden'}),
        }
    
    def clean_rx(self):
        rx = self.cleaned_data.get("rx")
        print(f"rx = {rx}")
        if rx is None:
            raise forms.ValidationError("RX must be selected!!")
        return rx

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity < 1:
            raise forms.ValidationError(
                "Quantity must be greater than 0!!")
        return quantity

    def clean_total(self):
        quantity = self.cleaned_data.get("quantity")
        print(f"Quantity: {quantity}")
        rx_price = self.cleaned_data.get("rx").dis_price
        print(f"RX Price: {rx_price}")
        total = quantity * rx_price
        print(f"Total: {total}")
        return total
        
PrescriptionFormSet = formset_factory(PrescriptionForm,extra=0)

class SearchTreatmentHistoryForm(ModelForm):
    class Meta:
        model = TreatedAnimal
        fields = ["case_number"]
        widgets = {
            'case_number': forms.Select(attrs={'class': 'form-control'}),
        }

