# create a django model form 
from attr import attr
from django import forms
from .models import DrugIn,DrugOut

# create a drugIn form
class DrugInForm(forms.ModelForm):
    # calcualte total from unit price and quantity
    def clean_total(self):
        unit_price = self.cleaned_data.get("unit_price")
        quantity = self.cleaned_data.get("quantity")
        total = unit_price * quantity
        return total

    class Meta:
        model = DrugIn
        exclude = ["date_received","total"]

        widgets = {
            'drug' : forms.Select(attrs={'class': 'form-control'}),
            'source' : forms.TextInput(attrs={'class': 'form-control'}),
            'receiver' : forms.Select(attrs={'class': 'form-control'}),
            'dropped_by' : forms.TextInput(attrs={'class': 'form-control'}),
            'quantity' : forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'batch_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'expiration_data' : forms.DateInput(attrs={'class': 'form-control'}),
            'remark' : forms.Textarea(attrs={'class': 'form-control'}),
        }
# create a drugOut form
class DrugOutForm(forms.ModelForm):
    # calcualte total from unit price and quantity
    def clean_total(self):
        unit_price = self.cleaned_data.get("unit_price")
        quantity = self.cleaned_data.get("quantity")
        total = unit_price * quantity
        return total
    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative")
        if quantity == 0:
            raise forms.ValidationError("Quantity cannot be zero")
        return quantity

    class Meta:
        model = DrugOut
        exclude = ["date_received","total"]

        widgets = {
            'drug' : forms.Select(attrs={'class': 'form-control'}),
            'destination' : forms.TextInput(attrs={'class': 'form-control'}),
            'receiver' : forms.Select(attrs={'class': 'form-control'}),
            'approved_by' : forms.TextInput(attrs={'class': 'form-control'}),
            'store_man' : forms.TextInput(attrs={'class':'form-control'}),
            'quantity' : forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'batch_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'remark' : forms.Textarea(attrs={'class': 'form-control'}),
        }