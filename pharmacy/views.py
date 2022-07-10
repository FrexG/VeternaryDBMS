from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# import models
from regulartreatedanimals.models import Prescription
from parasitetreatment.models import ParasitePrescription
# Create your views here.

class Index(LoginRequiredMixin,View):
    login_url =  "/"
    templateURL = 'pharmacy/pharmacist.html'

    def get(self,request):
        prescription = Prescription.objects.filter(paid = True,delivered=False)
        parasite_prescription = ParasitePrescription.objects.filter(paid = True,delivered=False)

        context={
                "parasite_prescriptions":parasite_prescription,
                "prescriptions":prescription
                }

        return render(request,template_name=self.templateURL,context=context)

class DeliverPrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("pharmacy/")

    def post(self,request,pk):
        Prescription.objects.filter(id = pk).update(delivered=True)

        return redirect("/pharmacy")

class CancelPrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("pharmacy/")

    def post(self,request,pk):
        Prescription.objects.filter(id = pk).update(paid=False)
        return redirect("/pharmacy")


class DeliverParasitePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("pharmacy/")

    def post(self,request,pk):
        ParasitePrescription.objects.filter(id = pk).update(delivered=True)

        return redirect("/pharmacy")
        
class CancelParasitePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("pharmacy/")

    def post(self,request,pk):
        ParasitePrescription.objects.filter(id = pk).update(paid=False)
        return redirect("/pharmacy")
