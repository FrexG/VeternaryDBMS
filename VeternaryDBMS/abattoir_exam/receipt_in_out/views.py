from django.shortcuts import redirect, render,HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from utils.printout import receipt_printout
# import your forms
from .forms import ReceiptInForm,ReceiptOutForm
# Create your views here.

class ReceiptInView(LoginRequiredMixin,View):
    login_url = "/"
    templateURL = "receipt_in_out/receipt_in.html"

    def get(self,request):
        form = ReceiptInForm()
        context = {
            'form':form
        }
    
        return render(request,self.templateURL,context)

    def post(self,request):
        form = ReceiptInForm(request.POST)

        if form.is_valid():
            obj = form.save()
            params = {
                'invoice_type':'RECEIPT IN',
                'item':obj.receipt_type.receipt_type,
                'deliverer_receiver':obj.deliverer_name,
                'quantity':str(obj.quantity),
                'kebele':obj.kebele.name,
                'unit':obj.unit,
                'date':obj.date,
                'serial_init':obj.serial_num_init,
                'serial_last':obj.serial_num_last,
                }
            return receipt_printout(request,params)
        else:
            context = {
                'form':form
            }
            return render(request,self.templateURL,context)
        return redirect('receipt_in_out:receipt_in')

class ReceiptOutView(LoginRequiredMixin,View):
    login_url = "/"
    templateURL = "receipt_in_out/receipt_out.html"

    def get(self,request):
        form = ReceiptOutForm()
        context = {
            'form':form
        }
    
        return render(request,self.templateURL,context)

    def post(self,request):
        form = ReceiptOutForm(request.POST)

        if form.is_valid():
            obj = form.save()
            params = {
                'invoice_type':'RECEIPT OUT',
                'item':obj.receipt_type.receipt_type,
                'deliverer_receiver':obj.receiver_name,
                'quantity':str(obj.quantity),
                'kebele':obj.kebele.name,
                'unit':obj.unit,
                'date':obj.date,
                'serial_init':obj.serial_num_init,
                'serial_last':obj.serial_num_last,
                }
            return receipt_printout(request,params)
        else:
            context = {
                'form':form
            }
            return render(request,self.templateURL,context)
        return redirect('receipt_in_out:receipt_out')