from django.forms import ModelForm
from django import forms
from django.forms import modelformset_factory, formset_factory

from .models import TreatedAnimal, Prescription
from registernewuser.models import Customer

import re


class TreatedAnimalsForm(ModelForm):
    class Meta:
        textAreaSize = "height: 100px;"
        model = TreatedAnimal
        fields = "__all__"

        widgets = {
            'case_number': forms.TextInput(attrs={'class': 'form-control'}),
            't0': forms.NumberInput(attrs={'class': 'form-control'}),
            'pr': forms.NumberInput(attrs={'class': 'form-control'}),
            'rr': forms.NumberInput(attrs={'class': 'form-control'}),
            'clinical_finding': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
            'dx': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
            'differential_diag': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
            'rumen_motility': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),

        }

    # Add form validation
    def cleaned_case_number(self):
        CASE_NUMBER_EXISTS = False

        case_number = self.cleaned_data["case_number"]

        # Check if case_number is not empty
        if case_number == "":
            raise forms.ValidationError("This field can't be empty!")

        # Check if the case number exists in the customers table
        for customer in Customer.objects.all():
            if customer.case_number == case_number:
                CASE_NUMBER_EXISTS = True

        if not CASE_NUMBER_EXISTS:
            raise forms.ValidationError("This Customer doesn't exist")

        return case_number


class PrescriptionForm(ModelForm):

    class Meta:
        model = Prescription
        fields = "__all__"

        widgets = {
            'rx': forms.Select(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'treatment': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
        }


widgets = {
    'rx': forms.Select(attrs={'class': 'form-control'}),
    'unit': forms.Select(attrs={'class': 'form-control'}),
    'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
    'duration': forms.NumberInput(attrs={'class': 'form-control'}),
    'treatment': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
}

PrescriptionFormSet = formset_factory(PrescriptionForm, extra=0)
