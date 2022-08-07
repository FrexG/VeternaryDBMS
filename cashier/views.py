from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

# import models
from clinicalservices.models import ClinicalService
from regulartreatedanimals.models import Prescription
from parasitetreatment.models import ParasitePrescription
from lab_exam.models import LabExamRequest
# Create your views here.

class Index(LoginRequiredMixin,View):
    login_url =  "/"
    templateURL = 'cashier/cashier.html'

    def get(self,request):
        clinical_services = ClinicalService.objects.filter(paid=False)
        prescription = Prescription.objects.filter(paid = False)
        parasite_prescription = ParasitePrescription.objects.filter(paid = False)
        lab_exam = LabExamRequest.objects.filter(paid=False)

        print(f"Count: {prescription.count()}")
        #print(parasite_prescription[0].treatment)

        context={"services":clinical_services,
                "parasite_prescriptions":parasite_prescription,
                "prescriptions":prescription,
                "lab_exam":lab_exam
                }

        return render(request,template_name=self.templateURL,context=context)

class UpdateService(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        ClinicalService.objects.filter(id = pk).update(paid=True)

        return redirect("/cashier")

class DeleteService(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        ClinicalService.objects.get(id = pk).delete()
        return redirect("/cashier")

class UpdatePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        Prescription.objects.filter(id = pk).update(paid=True)

        return redirect("/cashier")

class DeletePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        Prescription.objects.get(id = pk).delete()
        return redirect("/cashier")


class UpdateParasitePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        ParasitePrescription.objects.filter(id = pk).update(paid=True)

        return redirect("/cashier")
        
class DeleteParasitePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        ParasitePrescription.objects.get(id = pk).delete()
        return redirect("/cashier")

class UpdateLabExam(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        LabExamRequest.objects.filter(id = pk).update(paid=True)

        return redirect("/cashier")

class DeleteLabExam(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        LabExamRequest.objects.get(id = pk).delete()
        return redirect("/cashier")