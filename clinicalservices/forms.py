from django import forms
from django.forms import ModelForm,modelformset_factory
from .models import ClinicalService, AIService
# regular expression
import re


class ClinicalServiceForm(ModelForm):
    class Meta:
        model = ClinicalService
        exclude = ["paid"]

        widgets = {
            'case_number': forms.Select(attrs={'class': 'form-control'}),
            'service_type': forms.Select()
        }

    def clean(self):
        super(ClinicalServiceForm, self).clean()
    
        print("cleaning case number")
        service_type = self.cleaned_data.get("service_type")
        

        # check if case number is  not empty
        if service_type == None:
            raise forms.ValidationError(
                "Please select a service type!!")
        return self.cleaned_data
        

        

ClinicalServiceFormset = modelformset_factory(ClinicalService,form=ClinicalServiceForm,extra=1)
# AIService Form


class AIServiceForm(ModelForm):
    def clean_case_number(self):
        case_number = self.cleaned_data.get("case_number")

        if str(case_number) == "":
            raise forms.ValidationError("This field can't be empty!")
        return case_number

    def clean_color(self):
        print("I am called!!")

        color = self.cleaned_data.get("color")
        # Color name should not contain any numbers
        pattern = '[0-9#$@%]'
        pattern = re.compile(pattern)

        match = pattern.findall(str(color))

        if len(match) > 0:
            print(f'Length :{len(match)}')
            raise forms.ValidationError("This can't be a valid color")

        return color

    class Meta:
        model = AIService
        exclude = ["service_type"]

        widgets = {
            'case_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'last_calving_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'ai_frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'bull_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'pd_result': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'})

        }

        # form validation
