from django.forms import ModelForm
from django import forms

from .models import TreatedAnimal
from registernewuser.models import Drug


class TreatedAnimalsForm(ModelForm):
    class Meta:
        model = TreatedAnimal
        fields = "__all__"

        widgets = {
            'case_number': forms.TextInput(),
        }
