from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from regulartreatedanimals.models import Prescription
from parasitetreatment.models import ParasitePrescription
from .forms import CaseNumForm

# Create your views here.

class Index(LoginRequiredMixin,View):
    login_url = "/"
    templateURL = 'opd/index.html'

    # get all the prescription from regular treatment with
    # duraiton of greater than 1

    def get(self,request):
        case_number_form = CaseNumForm()
        context = {'case_num_form':case_number_form}
        return render(request,self.templateURL,context)

    def post(self,request):
        case_number_form = CaseNumForm()
        case_number_form = CaseNumForm(request.POST)
        case_number = case_number_form["case_number"].value()

        prescription = Prescription.objects.filter(duration__gte=1,treatment__treatment_id__case_number = case_number)
        parasite_prescription = ParasitePrescription.objects.filter(duration__gte=2,treatment__case_number = case_number)

        context = {"case_num_form":case_number_form,
                    "regular_opd":prescription,
                    "parasite_opd":parasite_prescription
                    }
        
        return render(request,self.templateURL,context)

class OpdRegularView(LoginRequiredMixin,View):

    def get(self,request):
        return redirect("/opd")

    def post(self,request,pk):
        prescription = Prescription.objects.filter(id = pk)
        current_duration = prescription[0].duration - 1
        prescription.update(duration=current_duration)

        return redirect("/opd")

class OpdParasiteView(LoginRequiredMixin,View):

    def get(self,request):
        return redirect("/opd")

    def post(self,request,pk):
        prescription = ParasitePrescription.objects.filter(id = pk)
        current_duration = prescription[0].duration - 1
        prescription.update(duration=current_duration)

        return redirect("/opd")