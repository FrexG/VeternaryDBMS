from django import forms
from .models import ReceiptOut,Receipt,ReceiptIn

class ReceiptInForm(forms.ModelForm):
    class Meta:
        model = ReceiptIn
        exclude = ["date"]

        widgets = {
        'receipt_type' : forms.Select(attrs={'class':'form-control'}),
        'deliverer_name' : forms.TextInput(attrs={'class':'form-control'}),
        'kebele' : forms.Select(attrs={'class':'form-control'}),
        'unit' : forms.Select(attrs={'class':'form-control'}),
        'quantity' : forms.NumberInput(attrs={'class':'form-control'}),
        'serial_num_init' : forms.TextInput(attrs={'class':'form-control'}),
        'serial_num_last' :forms.TextInput(attrs={'class':'form-control'}),
        }

class ReceiptOutForm(forms.ModelForm):
    class Meta:
        model = ReceiptOut
        exclude = ["date"]

        widgets = {
        'receipt_type' : forms.Select(attrs={'class':'form-control'}),
        'receiver_name' : forms.TextInput(attrs={'class':'form-control'}),
        'kebele' : forms.Select(attrs={'class':'form-control'}),
        'unit' : forms.Select(attrs={'class':'form-control'}),
        'quantity' : forms.NumberInput(attrs={'class':'form-control'}),
        'serial_num_init' : forms.TextInput(attrs={'class':'form-control'}),
        'serial_num_last' :forms.TextInput(attrs={'class':'form-control'}),
        }
