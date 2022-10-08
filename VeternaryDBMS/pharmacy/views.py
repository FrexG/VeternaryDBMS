from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# import models
from regulartreatedanimals.models import Prescription,Treatment
from parasitetreatment.models import ParasitePrescription,ParasiteTreatment
from datetime import datetime
# Create your views here.

class Index(LoginRequiredMixin,View):
    login_url =  "/"
    templateURL = 'pharmacy/pharmacist.html'

    def get(self,request):
        prescription = Prescription.objects.filter(treatment__treatment_id__service_date = datetime.now().date())
        regular_treatment = Treatment.objects.filter(treatment_id__service_date = datetime.now().date(),paid = True,delivered=False)

        parasite_prescription = ParasitePrescription.objects.filter(treatment__service_date = datetime.now().date())
        parasite_treatment = ParasiteTreatment.objects.filter(service_date = datetime.now().date(),paid = True,delivered=False)

        context={
                "parasite_prescriptions":parasite_prescription,
                "parasite_treatment":parasite_treatment,
                "prescriptions":prescription,
                "regular_treatment":regular_treatment
                }

        return render(request,template_name=self.templateURL,context=context)

class DeliverPrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("pharmacy/")

    def post(self,request,pk):
        Treatment.objects.filter(id = pk).update(delivered=True)

        return redirect("/pharmacy")

class CancelPrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("pharmacy/")

    def post(self,request,pk):
        Treatment.objects.filter(id = pk).update(paid=False)
        return redirect("/pharmacy")


class DeliverParasitePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("pharmacy/")

    def post(self,request,pk):
        ParasiteTreatment.objects.filter(id = pk).update(delivered=True)

        return redirect("/pharmacy")
        
class CancelParasitePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("pharmacy/")

    def post(self,request,pk):
        ParasiteTreatment.objects.filter(id = pk).update(paid=False)
        return redirect("/pharmacy")
