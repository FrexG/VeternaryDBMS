from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from datetime import datetime

# import models
from clinicalservices.models import ClinicalService,AIService
from regulartreatedanimals.models import Treatment,Prescription
from parasitetreatment.models import ParasitePrescription,ParasiteTreatment
from lab_exam.models import LabExamRequest
# Create your views here.

class Index(LoginRequiredMixin,View):
    login_url =  "/"
    templateURL = 'cashier/cashier.html'

    def get(self,request):
        clinical_services = ClinicalService.objects.filter(paid=False)
        ai_services = AIService.objects.filter(paid=False)

        prescription = Prescription.objects.filter(treatment__treatment_id__service_date = datetime.now().date())
        regular_treatment = Treatment.objects.filter(treatment_id__service_date = datetime.now().date(),paid = False)

        parasite_prescription = ParasitePrescription.objects.filter(treatment__service_date = datetime.now().date())
        parasite_treatment = ParasiteTreatment.objects.filter(service_date = datetime.now().date(),paid = False)

        lab_exam = LabExamRequest.objects.filter(paid=False)

        context={"services":clinical_services,
                "ai_services":ai_services,
                "parasite_prescriptions":parasite_prescription,
                "regular_treatment":regular_treatment,
                "prescriptions":prescription,
                "parasite_treatment":parasite_treatment,
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

class UpdateAIService(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        AIService.objects.filter(id = pk).update(paid=True)

        return redirect("/cashier")

class DeleteAIService(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        AIService.objects.get(id = pk).delete()
        return redirect("/cashier")

class UpdatePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        # pk is the treatment id
        Treatment.objects.filter(id = pk).update(paid=True)

        return redirect("/cashier")

class DeletePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        Treatment.objects.get(id = pk).delete()
        return redirect("/cashier")


class UpdateParasitePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        ParasiteTreatment.objects.filter(id = pk).update(paid=True)

        return redirect("/cashier")
        
class DeleteParasitePrescription(LoginRequiredMixin,View):
    def get(self,request):
        return redirect("cashier/")

    def post(self,request,pk):
        ParasiteTreatment.objects.get(id = pk).delete()
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