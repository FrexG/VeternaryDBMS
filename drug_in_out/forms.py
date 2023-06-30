# create a django model form
from django import forms
from .models import DrugIn, DrugOut, DrugOutCashDeposit
from stock.models import DrugStock


class DrugInForm(forms.ModelForm):
    # calcualte total from unit price and quantity
    def clean_total(self):
        print("clean_total")
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
        print("clean_unit_price")
        unit_price = self.cleaned_data.get("unit_price")
        if unit_price <= 0:
            raise forms.ValidationError("Unit price cannot be negative or zero")
        return unit_price

    def clean_quantity(self):
        print("clean_quantity")
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
            "drug": forms.Select(attrs={"class": "form-control"}),
            "source": forms.Select(attrs={"class": "form-control"}),
            "receiver": forms.Select(attrs={"class": "form-control"}),
            "dropped_by": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "total": forms.NumberInput(
                attrs={"class": "form-control", "type": "hidden"}
            ),
            "unit_price": forms.NumberInput(attrs={"class": "form-control"}),
            "batch_number": forms.TextInput(attrs={"class": "form-control"}),
            "expiration_data": forms.SelectDateWidget(attrs={"class": "form-control"}),
            "remark": forms.Textarea(attrs={"class": "form-control"}),
        }


# create a drugOut form
class DrugOutForm(forms.ModelForm):
    # calcualte total from unit price and quantity
    def clean_total(self):
        unit_price = self.cleaned_data.get("drug").stock_price
        quantity = self.cleaned_data.get("quantity")
        if quantity is None:
            quantity = 0
        print(unit_price, quantity)
        total = unit_price * quantity
        return total

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        quantity_in_stock = DrugStock.objects.get(
            drug=self.cleaned_data.get("drug")
        ).quantity
        print(f"Quantity in stock: {quantity_in_stock}")

        if quantity > quantity_in_stock:
            raise forms.ValidationError(
                "The quantity you entered is greater than the quantity in stock"
            )
        elif quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative")
        elif quantity == 0:
            raise forms.ValidationError("Quantity cannot be zero")
        else:
            # update the drug stock
            drug_stock = DrugStock.objects.get(drug=self.cleaned_data.get("drug"))
            drug_stock.quantity = drug_stock.quantity - quantity
            drug_stock.save()
        print("final quantity: ", quantity)
        return quantity

    class Meta:
        model = DrugOut
        exclude = ["date_received"]

        widgets = {
            "drug": forms.Select(attrs={"class": "form-control"}),
            "destination": forms.Select(attrs={"class": "form-control"}),
            "kebele": forms.Select(attrs={"class": "form-control"}),
            "received_by": forms.TextInput(attrs={"class": "form-control"}),
            "approved_by": forms.Select(attrs={"class": "form-control"}),
            "store_man": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "total": forms.NumberInput(
                attrs={"class": "form-control", "type": "hidden"}
            ),
            #'unit_price' : forms.NumberInput(attrs={'class': 'form-control'}),
            "batch_number": forms.TextInput(attrs={"class": "form-control"}),
            "remark": forms.Textarea(attrs={"class": "form-control"}),
        }


# create a drugOutCashDeposit form
class DrugOutCashDepositForm(forms.ModelForm):
    def clean_amount(self):
        # all previous payments for this equipment
        previous_payments = DrugOutCashDeposit.objects.all()
        # total amount of previous payments
        previous_deposited_amount = 0
        for payment in previous_payments:
            previous_deposited_amount = previous_deposited_amount + payment.amount
        # current payment amount
        current_payment_amount = self.cleaned_data.get("amount")
        # Initial total amount of the equipment
        total_amount = 0
        for obj in DrugOut.objects.all():
            total_amount += obj.total
        # check if the current payment amount is greater than the total amount of previous payments
        if current_payment_amount + previous_deposited_amount > total_amount:
            print(
                f"The amount you entered is greater than {total_amount - previous_deposited_amount} birr"
            )
            raise forms.ValidationError(
                f"The amount you entered is greater than {total_amount - previous_deposited_amount} birr"
            )

        if current_payment_amount <= 0:
            raise forms.ValidationError("Amount cannot be negative or zero")
        return current_payment_amount

    def clean_remaining_amount(self):
        # all previous payments for this equipment
        previous_payments = DrugOutCashDeposit.objects.all()
        # total amount of previous payments
        previous_deposited_amount = 0
        for payment in previous_payments:
            previous_deposited_amount = previous_deposited_amount + payment.amount
        # current payment amount
        deposited_amount = self.cleaned_data.get("amount")
        # Initial total amount of the equipment
        total_amount = 0
        for obj in DrugOut.objects.all():
            total_amount += obj.total

        if deposited_amount == None:
            deposited_amount = 0
        remaining_amount = (total_amount - previous_deposited_amount) - deposited_amount
        return remaining_amount

    class Meta:
        model = DrugOutCashDeposit
        exclude = ["date_paid"]

        widgets = {
            "amount": forms.NumberInput(attrs={"class": "form-control"}),
            "bank_slip_number": forms.TextInput(attrs={"class": "form-control"}),
            "remaining_amount": forms.NumberInput(
                attrs={"class": "form-control", "type": "hidden"}
            ),
            "confirmed_by": forms.Select(attrs={"class": "form-control"}),
            "remark": forms.Textarea(attrs={"class": "form-control"}),
        }
