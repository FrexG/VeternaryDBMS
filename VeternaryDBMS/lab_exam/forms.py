from .models import LabExamRequest,LabResult
from django import forms

class LabExamRequestForm(forms.ModelForm):
    class Meta:
        model = LabExamRequest
        exclude = ['paid','lab_result_arrived']

        widgets = {
            'treated_animal':forms.Select(attrs={'class':'form-control'}),
            'lab_sample':forms.Select(attrs={'class':'form-control'}),
            'lab_technique':forms.Select(attrs={'class':'form-control'}),
        }

class LabResult(forms.ModelForm):
    class Meta:
        model = LabResult
        exclude = ["date"]

        widgets = {
            'lab_exam_request':forms.Select(attrs={'class':'form-control'}),
            'lab_result':forms.TextInput(attrs={'class':'form-control'}),
            'case_holder':forms.Select(attrs={'class':'form-control'}), 
        }
    def clean_lab_result(self):
        lab_result = self.cleaned_data.get("lab_result")
        if lab_result == "":
            raise forms.ValidationError("this field can't be empty")

        return lab_result