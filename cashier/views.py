from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

# import models
from clinicalservices.models import ClinicalService
# Create your views here.

class Index(LoginRequiredMixin,View):
    login_url =  "/"
    templateURL = 'cashier/cashier.html'

    def get(self,request):
        clinical_services = ClinicalService.objects.filter(paid=False)
        return render(request,template_name=self.templateURL,context={"services":clinical_services})

class UpdateService(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        ClinicalService.objects.filter(id = pk).update(paid=True)

        return redirect("/cashier")

