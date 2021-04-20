from django import forms
from django.forms import ModelForm, formset_factory

from .models import ClinicalService, AIService, ServiceProvided
# regular expression
import re


class ClinicalServiceForm(ModelForm):
    class Meta:
        model = ClinicalService
        fields = "__all__"

        widgets = {
            'case_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ServiceProvidedForm(ModelForm):
    def clean_service_type(self, *args, **kwargs):

        service_type = self.cleaned_data.get("service_type")
        # Check if service_type is filled and is valid

        if service_type == "":

            raise forms.ValidationError("Please, select a customer")

        return service_type

    class Meta:
        model = ServiceProvided
        fields = "__all__"

        widgets = {
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'clinical_service': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'})
        }
    # Form Validation


ServiceProvidedFormSet = formset_factory(ServiceProvidedForm, extra=0)


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
        fields = "__all__"

        widgets = {
            'case_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'last_calving_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'ai_frequency': forms.TextInput(attrs={'class': 'form-control'}),
            'bull_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'pd_result': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'})

        }

        # form validation
