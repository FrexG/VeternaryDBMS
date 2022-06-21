from django.forms import ModelForm
from django import forms
from django.forms import modelformset_factory, formset_factory

from regulartreatedanimals.models import Prescription
from .models import ParasiteTreatment
from registernewuser.models import Customer
import re

class ParasiteTreatmentForm(ModelForm):
     class Meta:
        textAreaSize = "height: 100px;"
        model = ParasiteTreatment
        exclude = ['service_date','unit']

        widgets = {
            'case_number': forms.Select(attrs={'class': 'form-control'}),
            'treatment_type': forms.Select(attrs={'class': 'form-control'}),
            'dx': forms.Textarea(attrs={'class': 'form-control', 'style': textAreaSize}),
            'case_holder': forms.Select(attrs={'class': 'form-control'}),
        }


