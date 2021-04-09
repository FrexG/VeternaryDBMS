from django import forms
from django.forms import ModelForm, formset_factory

from .models import ClinicalService, AIService, ServiceProvided


class ClinicalServiceForm(ModelForm):
    class Meta:
        model = ClinicalService
        fields = "__all__"

        widgets = {
            'case_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ServiceProvidedForm(ModelForm):
    class Meta:
        model = ServiceProvided
        fields = "__all__"

        widgets = {
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'clinical_service': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'})
        }


ServiceProvidedFormSet = formset_factory(ServiceProvidedForm, extra=1)
