# create a django model form 
from django import forms
from .models import DrugIn,DrugOut,DrugOutCashDeposit
from stock.models import DrugStock
class DrugInForm(forms.ModelForm):
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

    def clean_quantity(self):
        print('clean_quantity')
        quantity = self.cleaned_data.get("quantity")

        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative")
        elif quantity == 0:
            raise forms.ValidationError("Quantity cannot be zero")
        else:
            # update the drug stock
            drug_stock = DrugStock.objects.get(drug=self.cleaned_data.get("drug"))
            drug_stock.quantity = drug_stock.quantity + quantity
            drug_stock.save()
        return quantity

    class Meta:
        model = DrugIn
        exclude = ["date_received"]

        widgets = {
            'drug' : forms.Select(attrs={'class': 'form-control'}),
            'source' : forms.Select(attrs={'class': 'form-control'}),
            'receiver' : forms.Select(attrs={'class': 'form-control'}),
            'dropped_by' : forms.TextInput(attrs={'class': 'form-control'}),
            'quantity' : forms.NumberInput(attrs={'class': 'form-control'}),
            'total' : forms.NumberInput(attrs={'class': 'form-control','type':'hidden'}),
            'unit_price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'batch_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'expiration_data' : forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'remark' : forms.Textarea(attrs={'class': 'form-control'}),
        }
# create a drugOut form
class DrugOutForm(forms.ModelForm):
    # calcualte total from unit price and quantity
    def clean_total(self):
        unit_price = self.cleaned_data.get("unit_price")
        quantity = self.cleaned_data.get("quantity")
        if quantity is None:
            quantity = 0
        print(unit_price,quantity)
        total = unit_price * quantity
        return total

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        quantity_in_stock = DrugStock.objects.get(drug=self.cleaned_data.get("drug")).quantity
        print(f"Quantity in stock: {quantity_in_stock}")
        
        if quantity > quantity_in_stock:
            raise forms.ValidationError("The quantity you entered is greater than the quantity in stock")  
        elif quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative")
        elif quantity == 0:
            raise forms.ValidationError("Quantity cannot be zero")
        else:
            # update the drug stock
            drug_stock = DrugStock.objects.get(drug=self.cleaned_data.get("drug"))
            drug_stock.quantity = drug_stock.quantity - quantity
            drug_stock.save()
        print("final quantity: ",quantity)
        return quantity

    class Meta:
        model = DrugOut
        exclude = ["date_received"]

        widgets = {
            'drug' : forms.Select(attrs={'class': 'form-control'}),
            'destination' : forms.Select(attrs={'class': 'form-control'}),
            'receiver' : forms.Select(attrs={'class': 'form-control'}),
            'approved_by' : forms.Select(attrs={'class': 'form-control'}),
            'store_man' : forms.TextInput(attrs={'class':'form-control'}),
            'quantity' : forms.NumberInput(attrs={'class': 'form-control'}),
             'total' : forms.NumberInput(attrs={'class': 'form-control','type':'hidden'}),
            'unit_price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'batch_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'remark' : forms.Textarea(attrs={'class': 'form-control'}),
        }
# create a drugOutCashDeposit form
class DrugOutCashDepositForm(forms.ModelForm):
    def clean_remaining_amount(self):
        amount = self.cleaned_data.get("amount")
        total_amount = self.cleaned_data.get("payment_for").total
        print(amount,total_amount)
        remaining_amount = total_amount - amount
        return remaining_amount

    class Meta:
        model = DrugOutCashDeposit
        exclude = ["date_paid"]

        widgets = {
            'payment_for':forms.Select(attrs={'class': 'form-control'}),
            'amount':forms.NumberInput(attrs={'class': 'form-control'}),
            'bank_slip_number':forms.TextInput(attrs={'class': 'form-control'}),
            'remaining_amount':forms.NumberInput(attrs={'class': 'form-control','type':'hidden'}),
            'confirmed_by':forms.Select(attrs={'class': 'form-control'}),
            'remark':forms.Textarea(attrs={'class': 'form-control'}),
        }