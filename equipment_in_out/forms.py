# create a django model form 
from django import forms
from .models import ClinicalEquipmentIn,ClinicalEquipmentOut,ClinicalEquipmentCashDeposit
from stock.models import ClinicalEquipmentStock
# create a EquipmentIN form
class ClinicalEquipmentInForm(forms.ModelForm):
    # calcualte total from unit price and quantity
    def clean_total(self):
        print('clean_total')
        unit_price = self.cleaned_data.get("unit_price")
        quantity = self.cleaned_data.get("quantity")
        if quantity is None:
            quantity = 0
        if unit_price is None:
            unit_price = 0
        
        total = unit_price * quantity
        return total
    # update the drug stock
    def clean_unit_price(self):
        print('clean_unit_price')
        unit_price = self.cleaned_data.get("unit_price")
        if unit_price <= 0:
            raise forms.ValidationError("Unit price cannot be negative or zero")
        return unit_price
    # update the equipment stock
    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative")
        elif quantity == 0:
            raise forms.ValidationError("Quantity cannot be zero")
        else:
            # update the equipment stock
            equipment_stock = ClinicalEquipmentStock.objects.get(equipment=self.cleaned_data.get("equipment"))
            equipment_stock.quantity = equipment_stock.quantity + quantity
            equipment_stock.save()
        return quantity

    class Meta:
        model = ClinicalEquipmentIn
        exclude = ["date_received"]

        widgets = {
            'equipment' : forms.Select(attrs={'class': 'form-control'}),
            'source' : forms.Select(attrs={'class': 'form-control'}),
            'receiver' : forms.Select(attrs={'class': 'form-control'}),
            'dropped_by' : forms.TextInput(attrs={'class': 'form-control'}),
            'quantity' : forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'total' : forms.NumberInput(attrs={'class': 'form-control','type':'hidden'}),
            'batch_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'expiration_data' : forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'remark' : forms.Textarea(attrs={'class': 'form-control'}),
        }
# create a equipment out form
class ClinicalEquipmentOutForm(forms.ModelForm):
    # calcualte total from unit price and quantity
    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        quantity_in_stock = ClinicalEquipmentStock.objects.get(equipment=self.cleaned_data.get("equipment")).quantity
        print("Quantity in stock:",quantity_in_stock,"Quantity to be out:",quantity)
        if quantity > quantity_in_stock:
            raise forms.ValidationError("The quantity you entered is greater than the quantity in stock")
        elif quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative")
        elif quantity == 0:
            raise forms.ValidationError("Quantity cannot be zero")
        else:
            # update the equipment stock
            equipment_stock = ClinicalEquipmentStock.objects.get(equipment=self.cleaned_data.get("equipment"))
            equipment_stock.quantity = equipment_stock.quantity - quantity
            equipment_stock.save()
        return quantity

    def clean_total(self):
        unit_price = self.cleaned_data.get("unit_price")
        quantity = self.cleaned_data.get("quantity")
        if quantity is None:
            quantity = 0
        print(unit_price,quantity)
        total = unit_price * quantity
        return total

    class Meta:
        model = ClinicalEquipmentOut
        exclude = ["date_received"]

        widgets = {
            'equipment' : forms.Select(attrs={'class': 'form-control'}),
            'destination' : forms.Select(attrs={'class': 'form-control'}),
            'receiver' : forms.Select(attrs={'class': 'form-control'}),
            'approved_by' : forms.Select(attrs={'class': 'form-control'}),
            'store_man' : forms.TextInput(attrs={'class':'form-control'}),
            'quantity' : forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'total' : forms.NumberInput(attrs={'class': 'form-control','type':'hidden'}),
            'batch_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'remark' : forms.Textarea(attrs={'class': 'form-control'}),
        }
# create a drugOutCashDeposit form
class ClinicalEquipmentCashDepositForm(forms.ModelForm):
    def clean_remaining_amount(self):
        amount = self.cleaned_data.get("amount")
        total_amount = self.cleaned_data.get("payment_for")
        remaining_amount = total_amount - amount
        return remaining_amount

    class Meta:
        model = ClinicalEquipmentCashDeposit
        exclude = ["date_paid"]

        widgets = {
            'payment_for':forms.Select(attrs={'class': 'form-control'}),
            'amount':forms.NumberInput(attrs={'class': 'form-control'}),
            'bank_slip_number':forms.TextInput(attrs={'class': 'form-control'}),
            'remaining_amount':forms.NumberInput(attrs={'class': 'form-control','type':'hidden'}),
            'confirmed_by':forms.Select(attrs={'class': 'form-control'}),
            'remark':forms.Textarea(attrs={'class': 'form-control'}),
        }