from .models import Vaccine,Vaccination
from django import forms
from django.forms import ModelForm

class VaccinationForm(ModelForm):
    class Meta:
        model = Vaccination
        exclude = ['service_date']
        widgets = {
            'case_number': forms.Select(attrs={'class': 'form-control'}),
            'vaccine_id': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'vaccine_batch_num': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'dx': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }