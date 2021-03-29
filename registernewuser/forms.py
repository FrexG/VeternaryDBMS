from django.forms import ModelForm
from django import forms

from .models import Customer

# Create ModelForm from Customer


class NewCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_kebele': forms.TextInput(attrs={'class': 'form-control'}),
            'kebele': forms.Select(attrs={'class': 'form-control'}),
            'case_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'species': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.Select(attrs={'class': 'form-control'}),
            'number_of_animals': forms.NumberInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'treatment_history': forms.Textarea(attrs={'class': 'form-control'}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
