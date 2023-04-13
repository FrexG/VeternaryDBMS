from .models import Vaccine,Vaccination
from django import forms
from django.forms import ModelForm

class VaccinationForm(ModelForm):
    class Meta:
        textAreaSize = "height: 100px;"
        model = Vaccination
        exclude = ['service_date',"paid"]
        widgets = {
            'case_number': forms.Select(attrs={'class': 'form-control'}),
            'species': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'breed': forms.Select(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'number_of_animals':forms.NumberInput(attrs={'class':'form-control'}),
            'history':forms.Textarea(attrs={'class':'form-control', 'style':textAreaSize}),
            'vaccine_id': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'vaccine_batch_num': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'case_holder': forms.Select(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            #'dx': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity < 1:
            raise forms.ValidationError(
                "Quantity must be greater than 0!!")
        return quantity

    def clean_total(self):
        quantity = self.cleaned_data.get("quantity")
        vaccine_price = self.cleaned_data.get("vaccine_id")[0].dis_price
        
        total = quantity * vaccine_price
        print(f"Total = {total}")
        return total


class SearchVaccinationHistoryForm(ModelForm):
    class Meta:
        model = Vaccination
        fields = ["case_number"]
        widgets = {
            'case_number': forms.Select(attrs={'class': 'form-control'}),
        }