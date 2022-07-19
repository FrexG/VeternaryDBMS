from contextlib import redirect_stdout
from django.shortcuts import render,redirect
# import view
from django.views import View
from matplotlib.style import context
from .models import *
from .forms import *

# Create your views here.
class VaccineInView(View):
    def get(self, request):
        vaccine_in_form = VaccineInForm()
        context = {
            'vaccine_in_form': vaccine_in_form,
        }
        return render(request,context=context,template_name='vaccine_in_out/vaccine_in.html')
    def post(self, request):
        vaccine_in_form = VaccineInForm(request.POST)
        if vaccine_in_form.is_valid():
            vaccine_in_form.save()
            return redirect('vaccine_in_out:vaccinein')
        else:
            context = {
            'vaccine_in_form': vaccine_in_form,
            }
            return render(request,context = context,template_name='vaccine_in_out/vaccine_in.html')

class VaccineOutView(View):
    vaccine_out_form = VaccineOutForm()
    vaccine_cash_deposit_form = VaccineOutCashDepositForm()
    def get(self, request):
        context = {
            'vaccine_out_form': self.vaccine_out_form,
            'vaccine_cash_deposit_form': self.vaccine_cash_deposit_form
        }
        return render(request,context=context,template_name='vaccine_in_out/vaccine_out.html')
    def post(self, request):
        vaccine_out_form = VaccineOutForm(request.POST)
        if vaccine_out_form.is_valid():
            vaccine_out_form.save()
            return redirect('vaccine_in_out:vaccineout')
        
        else:
            context = {
            'vaccine_out_form': vaccine_out_form,
            'vaccine_cash_deposit_form': self.vaccine_cash_deposit_form
            }
            return render(request,context=context,template_name='vaccine_in_out/vaccine_out.html')

class VaccineOutCashDeposit(View):
    def post(self, request):
        vaccine_cash_deposit_form = VaccineOutCashDepositForm(request.POST)
        if vaccine_cash_deposit_form.is_valid():
            vaccine_cash_deposit_form.save()
            return redirect('vaccine_in_out:vaccineout')
        else:
            return render(request,template_name='vaccine_in_out/vaccine_out.html')