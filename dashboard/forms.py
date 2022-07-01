# create a form for the dashboard
from django import forms
from matplotlib import widgets
from clinicalservices.models import ClinicalService
from parasitetreatment.models import ParasiteTreatment

class DateRangeFrom(forms.Form):
    start_date = forms.DateField(label='Start Date',widget=forms.DateInput(attrs={'type':'date',
                                    'id':'start_date'}))
    end_date = forms.DateField(label='End Date',widget=forms.DateInput(attrs={'type':'date',
                                    'id':'end_date'}))
class CaseHolderForm(forms.ModelForm):
    class Meta:
        model = ClinicalService
        fields = ['case_holder']
        widgets = {
            'case_holder': forms.Select(attrs={'id':'case_holder'})
        }
class ServieTypeForm(forms.ModelForm):
    class Meta:
        model = ClinicalService
        fields = ['service_type']
        widgets = {
            'service_type': forms.Select(attrs={'id':'service_type'})
        }
class TreatmentTypeForm(forms.ModelForm):
    class Meta:
        model = ParasiteTreatment
        fields = ["treatment_type"]
        widgets = {
            'treatment_type': forms.Select(attrs={'id':'treatment_type'})
        }