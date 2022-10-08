from .models import Vaccine,Vaccination
from django import forms
from django.forms import ModelForm

class VaccinationForm(ModelForm):
    class Meta:
        textAreaSize = "height: 100px;"
        model = Vaccination
        exclude = ['service_date']
        widgets = {
            'case_number': forms.Select(attrs={'class': 'form-control'}),
            'species': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.Select(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'number_of_animals':forms.NumberInput(attrs={'class':'form-control'}),
            'history':forms.Textarea(attrs={'class':'form-control', 'style':textAreaSize}),
            'vaccine_id': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'vaccine_batch_num': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'case_holder': forms.Select(attrs={'class': 'form-control'}),
            'dx': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
class SearchVaccinationHistoryForm(ModelForm):
    class Meta:
        model = Vaccination
        fields = ["case_number"]
        widgets = {
            'case_number': forms.Select(attrs={'class': 'form-control'}),
        }