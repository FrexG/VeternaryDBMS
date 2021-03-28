from django.forms import ModelForm

from .models import Customer

# Create ModelForm from Customer


class NewCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
