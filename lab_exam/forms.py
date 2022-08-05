from .models import LabExam
from django import forms

class LabExamForm(forms.ModelForm):
    class Meta:
        model = LabExam
        exclude = ['date']

        widgets = {
            'customer':forms.Select(attrs={'class':'form-control'}),
            'lab_sample':forms.Select(attrs={'class':'form-control'}),
            'lab_technique':forms.Select(attrs={'class':'form-control'}),
            'lab_result':forms.TextInput(attrs={'class':'form-control'})
        }
    
    def clean_lab_result(self):
        lab_result = self.cleaned_data.get("lab_result")
        if lab_result == "":
            raise forms.ValidationError("this field can't be empty")

        return lab_result