from contextlib import redirect_stdout
from django.shortcuts import render,redirect
# import view
from django.views import View
from .models import *
from .forms import *

# Create your views here.
class EquipmentInView(View):
    def get(self, request):
        equipment_in_form = ClinicalEquipmentInForm()
        context = {
            'equipment_in_form': equipment_in_form,
        }
        return render(request,context=context,template_name='equipment_in_out/equipment_in.html')
    def post(self, request):
        equipment_in_form = ClinicalEquipmentInForm(request.POST)
        if equipment_in_form.is_valid():
            equipment_in_form.save()
            return redirect('equipment_in_out:equipmentin')
        else:
            context = {
            'equipment_in_form': equipment_in_form,
            }
            return render(request,context = context,template_name='equipment_in_out/equipment_in.html')

class EquipmentOutView(View):
    equipment_out_form = ClinicalEquipmentOutForm()
    equipment_cash_deposit_form = ClinicalEquipmentCashDepositForm()
    def get(self, request):
        context = {
            'equipment_out_form': self.equipment_out_form,
            'equipment_cash_deposit_form': self.equipment_cash_deposit_form
        }
        return render(request,context=context,template_name='equipment_in_out/equipment_out.html')

    def post(self, request):
        equipment_out_form = ClinicalEquipmentOutForm(request.POST)
        if equipment_out_form.is_valid():
            equipment_out_form.save()
            return redirect('equipment_in_out:equipmentout')
        else:
            context = {
            'equipment_out_form': equipment_out_form,
            'equipment_cash_deposit_form': self.equipment_cash_deposit_form
            }
            return render(request,context=context,template_name='equipment_in_out/equipment_out.html')

class EquipmentOutCashDeposit(View):
    def post(self, request):
        equipment_cash_deposit_form = ClinicalEquipmentCashDepositForm(request.POST)
        if equipment_cash_deposit_form.is_valid():
            equipment_cash_deposit_form.save()
            return redirect('equipment_in_out:equipmentout')
        else:
            return render(request,template_name='equipment_in_out/equipment_out.html')