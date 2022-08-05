# create a form for the dashboard
from dataclasses import field
from django import forms
from clinicalservices.models import ClinicalService
from parasitetreatment.models import ParasiteTreatment
from drug_in_out.models import DrugIn,DrugOut
from equipment_in_out.models import ClinicalEquipmentIn,ClinicalEquipmentOut
from vaccine_in_out.models import VaccineIn,VaccineOut
from receipt_in_out.models import ReceiptIn,ReceiptOut
from registernewuser.models import Kebele
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
class DrugReceiverForm(forms.ModelForm):
    class Meta:
        model = DrugOut
        fields = ['receiver']
        widgets = {
            'receiver': forms.Select(),
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
class EquipmentReceiverForm(forms.ModelForm):
    class Meta:
        model = ClinicalEquipmentOut
        fields = ['receiver']
        widgets = {
            'receiver': forms.Select(),
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
class VaccineReceiverForm(forms.ModelForm):
    class Meta:
        model = VaccineOut
        fields = ['receiver']
        widgets = {
            'receiver': forms.Select(),
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
class ReceiptTypeForm(forms.ModelForm):
    class Meta:
        model = ReceiptIn
        fields = ["receipt_type"]

        widgets = {
            'receipt_type' : forms.Select(attrs={'id':'receipt_type'})
         }
class KebeleTypeForm(forms.ModelForm):
    class Meta:
        model = ReceiptOut
        fields = ["kebele"]

        widgets = {
            'kebele' : forms.Select(attrs={'id':'kebele'})
         } 
class StockSelectForm(forms.Form):
    stock_type = forms.ChoiceField(choices=[('Drug','Drug'),('Equipment','Equipment'),('Vaccine','Vaccine')],
                                    widget=forms.Select(attrs={'id':'stock_type'}))
