# create a form for the dashboard
from django import forms
from matplotlib import widgets
from clinicalservices.models import ClinicalService
from parasitetreatment.models import ParasiteTreatment
from drug_in_out.models import DrugIn,DrugOut
from equipment_in_out.models import ClinicalEquipmentIn,ClinicalEquipmentOut
from vaccine_in_out.models import VaccineIn,VaccineOut

# Drug In Out forms
class DrugTypeForm(forms.ModelForm):
    class Meta:
        model = DrugIn
        fields = ['drug']
        widgets = {
            'drug': forms.Select(),
        }
class DrugSourceForm(forms.ModelForm):
    class Meta:
        model = DrugIn
        fields = ['source']
        widgets = {
            'source': forms.Select(),
        }
class DrugDestinationForm(forms.ModelForm):
    class Meta:
        model = DrugOut
        fields = ['destination']
        widgets = {
            'destination': forms.Select(),
        }
# Equipment In Out forms
class EquipmentTypeForm(forms.ModelForm):
    class Meta:
        model = ClinicalEquipmentIn
        fields = ['equipment']
        widgets = {
            'equipment': forms.Select(),
        }
class EquipmentSourceForm(forms.ModelForm):
    class Meta:
        model = ClinicalEquipmentIn
        fields = ['source']
        widgets = {
            'source': forms.Select(),
        }
class EquipmentDestinationForm(forms.ModelForm):
    class Meta:
        model = ClinicalEquipmentOut
        fields = ['destination']
        widgets = {
            'destination': forms.Select(),
        }
# Vaccine In Out forms
class VaccineTypeForm(forms.ModelForm):
    class Meta:
        model = VaccineIn
        fields = ['vaccine']
        widgets = {
            'vaccine': forms.Select(),
        }
class VaccineSourceForm(forms.ModelForm):
    class Meta:
        model = VaccineIn
        fields = ['source']
        widgets = {
            'source': forms.Select(),
        }
class VaccineDestinationForm(forms.ModelForm):
    class Meta:
        model = VaccineOut
        fields = ['destination']
        widgets = {
            'destination': forms.Select(),
        }
        
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