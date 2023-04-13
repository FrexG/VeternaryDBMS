from django import forms

class CaseNumForm(forms.Form):
    case_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))