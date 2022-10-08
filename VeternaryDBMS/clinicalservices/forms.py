from faulthandler import disable
from django import forms
from django.forms import ModelForm,formset_factory
from .models import ClinicalService, AIService
# regular expression
import re


class ClinicalServiceForm(ModelForm):
    class Meta:
        model = ClinicalService
        exclude = ["paid"]

        widgets = {
            'case_number': forms.Select(attrs={'class':'form-control'}),
            'service_type': forms.Select(attrs={'class':'form-control'}),
            'case_holder': forms.Select(attrs={'class':'form-control','type':'hidden'}),
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
        

        
ClinicalServiceFormset = formset_factory(ClinicalServiceForm,extra=1)

# AIService Form

class AIServiceForm(ModelForm):
        # form validation
    def clean_qnty(self):
        qnty = self.cleaned_data.get("qnty")
        print(f"Qnty:{qnty}")
        if qnty < 1:
            raise forms.ValidationError(
                "Quantity must be greater than 0!!")
        return qnty

    def clean_total(self):
        qnty = self.cleaned_data.get("qnty")
        bull_num = self.cleaned_data.get("bull_number")
        price = self.cleaned_data.get("service_type").price

        print(f"Bull Num: {bull_num}")
        print(f"AI price = {price}, {qnty}")

        total = qnty * price
        return total
    

    class Meta:
        textAreaSize = "height: 100px;"
        model = AIService
        exclude = ["paid"]

        widgets = {
            'service_type': forms.Select(attrs={'class':'form-control'}),
            'case_number': forms.Select(attrs={'class': 'form-control'}),
            'species': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.Select(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'number_of_animals':forms.NumberInput(attrs={'class':'form-control'}),
            'history':forms.Textarea(attrs={'class':'form-control', 'style':textAreaSize}),
            'last_calving_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'ai_frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'bull_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'pd_result': forms.TextInput(attrs={'class': 'form-control'}),
            'qnty': forms.NumberInput(attrs={'class': 'form-control'}),
            'total':forms.NumberInput(attrs={'class':'form-control','type':'hidden'}),
            'case_holder': forms.Select(attrs={'class': 'form-control','type':'hidden'}),
        }

