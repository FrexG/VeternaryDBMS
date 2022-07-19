from contextlib import redirect_stdout
from django.shortcuts import render,redirect
# import view
from django.views import View
from matplotlib.style import context
from .models import *
from .forms import *

# Create your views here.
class DrugInView(View):
    def get(self, request):
        drug_in_form = DrugInForm()
        context = {
            'drug_in_form': drug_in_form,
        }
        return render(request,context=context,template_name='drug_in_out/drug_in.html')
    def post(self, request):
        drug_in_form = DrugInForm(request.POST)
        if drug_in_form.is_valid():
            drug_in_form.save()
            return redirect('drug_in_out:drugin')
        else:
            context = {
            'drug_in_form': drug_in_form,
            }
            return render(request,context = context,template_name='drug_in_out/index.html')

class DrugOutView(View):
    drug_out_form = DrugOutForm()
    drug_cash_deposit_form = DrugOutCashDepositForm()
    def get(self, request):
        context = {
            'drug_out_form': self.drug_out_form,
            'drug_cash_deposit_form': self.drug_cash_deposit_form
        }
        return render(request,context=context,template_name='drug_in_out/drug_out.html')
    def post(self, request):
        drug_out_form = DrugOutForm(request.POST)
        if drug_out_form.is_valid():
            drug_out_form.save()
            return redirect('drug_in_out:drugout')
        
        else:
            context = {
            'drug_out_form': drug_out_form,
            'drug_cash_deposit_form': self.drug_cash_deposit_form
            }
            return render(request,context=context,template_name='drug_in_out/drug_out.html')

class DrugOutCashDeposit(View):
    def post(self, request):
        drug_cash_deposit_form = DrugOutCashDepositForm(request.POST)
        if drug_cash_deposit_form.is_valid():
            drug_cash_deposit_form.save()
            return redirect('drug_in_out:drugout')
        else:
            return render(request,template_name='drug_in_out/drug_out.html')