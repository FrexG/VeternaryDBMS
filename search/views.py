from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from regulartreatedanimals.models import TreatedAnimal,Prescription,Treatment
from clinicalservices.models import ClinicalService,AIService
from vaccination.models import Vaccination
from parasitetreatment.models import ParasiteTreatment,ParasitePrescription

# Create your views here.
class SearchHistory(LoginRequiredMixin,View):
    login_url = "/"
    templateURL = "search/search.html"

    def post(self,request):
        case_number = request.POST.get('search_case_number')
        # search for case number in treated animal table, clinical service table, parasite treatment table
        regular_treatment = Treatment.objects.filter(treatment_id__case_number=case_number)
        vaccination = Vaccination.objects.filter(case_number=case_number)
        parasite_treatment = ParasiteTreatment.objects.filter(case_number=case_number)
        ai_service = AIService.objects.filter(case_number=case_number)

        # search for case number in prescription table
        parasite_prescription = ParasitePrescription.objects.all()
        regular_prescription = Prescription.objects.all()

        context = {
            'regular_treatment':regular_treatment,
            'regular_prescription':regular_prescription,
            'vaccination':vaccination,
            'parasite_treatment':parasite_treatment,
            'parasite_prescription':parasite_prescription,
            'ai_service':ai_service,
        }
        return render(request,self.templateURL,context)