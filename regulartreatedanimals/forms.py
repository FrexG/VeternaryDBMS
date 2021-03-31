from django.forms import ModelForm
from django import forms

from .models import TreatedAnimal, Prescription


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


class PrescriptionForm(ModelForm):

    class Meta:
        model = Prescription
        exclude = ["treatment"]

        widgets = {
            'rx': forms.Select(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }
