from django.forms import ModelForm
from django import forms
import re

from .models import Customer

# Create ModelForm from Customer
class NewCustomerForm(ModelForm):

    def clean_customer_name(self):
        customer_name = self.cleaned_data.get("customer_name")

        match_object = re.findall('[0-9]+', str(customer_name))

        if len(match_object) > 0:
            raise forms.ValidationError(
                "Only Letters are allowed in a user name!!")

        return customer_name

    class Meta:
        textAreaSize = "height: 100px;"
        model = Customer
        fields = "__all__"

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sub_kebele': forms.TextInput(attrs={'class': 'form-control'}),
            'kebele': forms.Select(attrs={'class': 'form-control'}),
            'case_number': forms.Select(attrs={'class': 'form-control'}),
            'species': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.Select(attrs={'class': 'form-control'}),
            'number_of_animals': forms.NumberInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'history': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
            'mobile_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
# Search customer form
class SearchForm(forms.Form):
    customer_name = forms.CharField(max_length = 100,label="Customer Name:",widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
