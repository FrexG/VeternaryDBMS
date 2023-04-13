from dataclasses import field
from django import forms
from drug_in_out.models import DrugOut

class DateForm(forms.Form):
    date = forms.DateField(label='Date',widget=forms.DateInput(attrs={'type':'date','id':'date','class': 'form-control'}))

printout_type = (
    ("drug_in", "Drug In"),
    ("drug_out", "Drug Out"),
    ("vaccine_in", "Vaccine In"),
    ("vaccine_out", "Vaccine Out"),
    ("equipment_in", "Equipment In"),
    ("equipment_out", "Equipment Out"),
    ("receipt_in", "Receipt In"),
    ("receipt_out", "Receipt Out"),
  
)

class SelectPrintOutForm(forms.Form):
    choice_field= forms.ChoiceField(label='Type', label_suffix = " : ",
                                  required = True,  disabled = False,
                                  choices = printout_type, widget=forms.Select(attrs={'class': 'form-control'}),
                                  error_messages = {'required':"This field is required."})

class SelectKebeleForm(forms.ModelForm):
    class Meta:
        model = DrugOut
        fields = ["kebele"]

        widgets = {
            'kebele' : forms.Select(attrs={'id':'kebele','class': 'form-control'})
         } 