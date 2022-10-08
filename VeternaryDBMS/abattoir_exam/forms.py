from django import forms
from .models import AbattoirExam

class AbattoirExamForm(forms.ModelForm):
    class Meta:
        model = AbattoirExam
        exclude = ["date"]

        widgets = {
            'hotel' : forms.Select(attrs={'class':'form-control'}),
            'species' : forms.Select(attrs={'class':'form-control'}),
            'sex': forms.Select(attrs={'class':'form-control'}),
            'color': forms.Select(attrs={'class':'form-control'}),
            'origin':forms.Select(attrs={'class':'form-control'}),
            'body_weight':forms.NumberInput(attrs={'class':'form-control'}),
            't0':forms.NumberInput(attrs={'class':'form-control'}),
            'pr':forms.NumberInput(attrs={'class':'form-control'}),
            'rr':forms.NumberInput(attrs={'class':'form-control'}),
            'result' :forms.Select(attrs={'class':'form-control'})
        }