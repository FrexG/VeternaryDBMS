from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
# Import all models from all apps
from clinicalservices.models import ClinicalService,AIService,Service
from parasitetreatment.models import ParasiteTreatment,ParasitePrescription
from regulartreatedanimals.models import TreatedAnimal,Disease,Prescription
from registernewuser.models import Kebele,Species,Customer
from .forms import DateRangeFrom,CaseHolderForm,ServieTypeForm,TreatmentTypeForm
# Create your views here.

class Index(LoginRequiredMixin,View):
    login_url =  "/"
    templateURL = 'dashboard/dashboard.html'
    kebeles = list(Kebele.objects.all())

    def get(self,request):
        print("Called")
        return render(request,self.templateURL)

        return data
class DashboardData(LoginRequiredMixin,View):
    diseases = Disease.objects.all()
    kebeles =Kebele.objects.all()
    species = Species.objects.all()
    customers = Customer.objects.all()
    clinical_service = ClinicalService.objects.all()
    ai_service = AIService.objects.all()
    parasite_treatment = ParasiteTreatment.objects.all()
    regular_treatment = TreatedAnimal.objects.all()

    def get(self,request):
        disease_name,count = self.getDiseasePrevalence()
        data = {
                "kebele_names":[kebele.name for kebele in self.kebeles],
                "kebele_count":self.kebeleCount(),
                
                "species_names":[species.getSpeciesName() for species in self.species],
                "species_count":self.speciesCount(),

                "service_names":["Clinical Service","AI Service","Parasite Treatment","Regular Treatment"],
                "service_count":[ClinicalService.objects.count(),AIService.objects.count(),ParasiteTreatment.objects.count(),TreatedAnimal.objects.count()],

                "disease_names":disease_name,
                "disease_count":count,
                }
        return JsonResponse(data)

    def kebeleCount(self):
        count = []
        for kebele in self.kebeles:
            i = 0
            for s in [ClinicalService,AIService,ParasiteTreatment,TreatedAnimal]:
                for obj in s.objects.all():
                    if obj.getKebele() == kebele:
                        i += 1
            count.append(i)
        return count
    def speciesCount(self):
        count = []
        for species in self.species:
            i = 0
            for customer in self.customers:
                if customer.species == species:
                    i += 1
            count.append(i)
        return count

    def getDiseasePrevalence(self):
        disease_count = {}
        for disease in self.diseases:
            for x in [self.regular_treatment,self.parasite_treatment]:
                for obj in x:
                    for dx in obj.dx.all():
                        if dx == disease:
                            if disease.disease_name in disease_count:
                                disease_count[disease.disease_name] += 1
                            else:
                                disease_count[disease.disease_name] = 1
        print(disease_count)
        return list(disease_count.keys()),list(disease_count.values())
class RegularTreatmentSummary(LoginRequiredMixin,View):
    login_url =  "/"
    templateUrl = "dashboard/regular_treatment_summary.html"
    dateForm = DateRangeFrom()

    def get(self,request):
        treatedAnimalsObj = TreatedAnimal.objects.all()
        totalTreatedAnimals = TreatedAnimal.objects.all().count()
        distByKebele = self.getDistByKebele(Kebele.objects.all(),treatedAnimalsObj)

        context = {"treatedAnimalsObj":treatedAnimalsObj,
                    "dateForm":self.dateForm,
                    "totalTreatedAnimals":totalTreatedAnimals,
                    "distByKebele":distByKebele}

        return render(request,self.templateUrl,context)

    def post(self,request):
        dateForm = DateRangeFrom(request.POST)
       
        start_date = dateForm['start_date'].value()
        end_date = dateForm['end_date'].value()

        treatedAnimalsObj = TreatedAnimal.objects.filter(service_date__gte=start_date,service_date__lte=end_date)
        totalTreatedAnimals = treatedAnimalsObj.count()
        distByKebele = self.getDistByKebele(Kebele.objects.all(),treatedAnimalsObj)

        context = {"treatedAnimalsObj":treatedAnimalsObj,
                    "dateForm":dateForm,
                    "totalTreatedAnimals":totalTreatedAnimals,
                    "distByKebele":distByKebele}

        return render(request,self.templateUrl,context)
    
    def getDistByKebele(self,kebeles=None,TreatedAnimalsObj=None):
        distByKebele = {}
        for kebele in kebeles:
            for t in  TreatedAnimalsObj:
                if t.getKebele() == kebele:
                    if kebele.name in distByKebele:
                        distByKebele[kebele.name] += 1
                    else:
                        distByKebele[kebele.name] = 1
        return distByKebele
class ClinicalServiceSummary(LoginRequiredMixin,View):
    login_url =  "/"
    templateUrl = "dashboard/clinical_service_summary.html"
    dateForm = DateRangeFrom()
    caseHolderForm = CaseHolderForm()
    serviceTypeForm = ServieTypeForm()

    def get(self,request):
        clinicalServicesObj = ClinicalService.objects.all()
        totalClinicalServices = ClinicalService.objects.all()
        distByKebele = self.getDistByKebele(Kebele.objects.all(),clinicalServicesObj)
        print(ClinicalService.objects.aggregate(Sum('service_type__price')))
        context = {"clinicalServicesObj":clinicalServicesObj,
                    "dateForm":self.dateForm,
                    "caseHolderForm":self.caseHolderForm,
                    "serviceTypeForm":self.serviceTypeForm,
                    "totalClinicalServices":totalClinicalServices.count(),
                    "totalPrice":totalClinicalServices.aggregate(sum_price = Sum('service_type__price')),
                    "distByKebele":distByKebele}

        return render(request,self.templateUrl,context)

    def post(self,request):
        dateForm = DateRangeFrom(request.POST)
        caseHolderForm = CaseHolderForm(request.POST)
        serviceTypeForm = ServieTypeForm(request.POST)

        case_holder = caseHolderForm['case_holder'].value()

        start_date = dateForm['start_date'].value()
        end_date = dateForm['end_date'].value()

        clinicalServicesObj = ClinicalService.objects.filter(service_date__gte=start_date,service_date__lte=end_date ,case_holder=case_holder,service_type=serviceTypeForm['service_type'].value())
        totalClinicalServices = clinicalServicesObj
        distByKebele = self.getDistByKebele(Kebele.objects.all(),clinicalServicesObj)

        context = {"clinicalServicesObj":clinicalServicesObj,
                    "dateForm":dateForm,
                    "caseHolderForm":caseHolderForm,
                    "serviceTypeForm":serviceTypeForm,
                    "totalClinicalServices":totalClinicalServices.count(),
                    "totalPrice":totalClinicalServices.aggregate(sum_price = Sum('service_type__price')),
                    "distByKebele":distByKebele}

        return render(request,self.templateUrl,context)
    
    def getDistByKebele(self,kebeles=None,ClinicalServicesObj=None):
        distByKebele = {}
        for kebele in kebeles:
            for t in  ClinicalServicesObj:
                if t.getKebele() == kebele:
                    if kebele.name in distByKebele:
                        distByKebele[kebele.name] += 1
                    else:
                        distByKebele[kebele.name] = 1
        return distByKebele
class ClinicalServiceTypes(LoginRequiredMixin,View):
    def get(self,request):
        service_types = Service.objects.all()
        clinical_service = ClinicalService.objects.all()

        data = {
            "service_types":[service_names.getServiceName() for service_names in service_types],
            "counts":[ClinicalService.objects.filter(service_type = service).count() for service in service_types]
        }
        return JsonResponse(data)
class ParasiteTreatmentSummary(LoginRequiredMixin,View):
    login_url =  "/"
    templateUrl = "dashboard/parasite_treatment_summary.html"
    dateForm = DateRangeFrom()
    caseHolderForm = CaseHolderForm()
    treatmentTypeForm = TreatmentTypeForm()

    def get(self,request):
        parasiteTreatmentObj = ParasiteTreatment.objects.all()
        distByKebele = self.getDistByKebele(Kebele.objects.all(),parasiteTreatmentObj)
    
        context = {"parasiteTreatmentObj":parasiteTreatmentObj,
                    "dateForm":self.dateForm,
                    "caseHolderForm":self.caseHolderForm,
                    "treatmentTypeForm":self.treatmentTypeForm,
                    "totalTreatments":parasiteTreatmentObj.count(),
                    "totalPrice":self.getPrice(parasiteTreatmentObj),
                    "distByKebele":distByKebele}

        return render(request,self.templateUrl,context)

    def post(self,request):
        dateForm = DateRangeFrom(request.POST)
        caseHolderForm = CaseHolderForm(request.POST)
        treatmentTypeForm = TreatmentTypeForm(request.POST)

        case_holder = caseHolderForm['case_holder'].value()

        start_date = dateForm['start_date'].value()
        end_date = dateForm['end_date'].value()

        parasiteTreatmentObj = ParasiteTreatment.objects.filter(service_date__gte=start_date,service_date__lte=end_date ,case_holder=case_holder,treatment_type=treatmentTypeForm['treatment_type'].value())

        distByKebele = self.getDistByKebele(Kebele.objects.all(),parasiteTreatmentObj)

        context = {"parasiteTreatmentObj":parasiteTreatmentObj,
                    "dateForm":dateForm,
                    "caseHolderForm":caseHolderForm,
                    "treatmentTypeForm":treatmentTypeForm,
                    "totalClinicalServices":parasiteTreatmentObj.count(),
                    "totalPrice":self.getPrice(parasiteTreatmentObj),
                    "distByKebele":distByKebele}

        return render(request,self.templateUrl,context)
    
    def getDistByKebele(self,kebeles=None,ClinicalServicesObj=None):
        distByKebele = {}
        for kebele in kebeles:
            for t in  ClinicalServicesObj:
                if t.getKebele() == kebele:
                    if kebele.name in distByKebele:
                        distByKebele[kebele.name] += 1
                    else:
                        distByKebele[kebele.name] = 1
        return distByKebele

    def getPrice(self,parasiteTreatmentObj):
        totalPrice = 0
        for pp in ParasitePrescription.objects.all():
            for p in parasiteTreatmentObj:
                if pp.treatment == p:
                    totalPrice += pp.getPrice()
        return totalPrice

class ParasiteTreatmentTypes(LoginRequiredMixin,View):
    diseases = Disease.objects.all()
    parasite_treatment = ParasiteTreatment.objects.all()
    def get(self,request):
        treatment_names = ["Internal","External"]
        disease_name,count = self.getDiseasePrevalence()
        data = {
            "treatment_types":treatment_names,
            "treatment_count":[ParasiteTreatment.objects.filter(treatment_type = treatment).count() for treatment in treatment_names],
            "disease_names":disease_name,
            "disease_count":count,
        }

        return JsonResponse(data)

    def getDiseasePrevalence(self):
        disease_count = {}
        for disease in self.diseases:
            for x in self.parasite_treatment:
                for dx in x.dx.all():
                    if dx == disease:
                        if disease.disease_name in disease_count:
                            disease_count[disease.disease_name] += 1
                        else:
                            disease_count[disease.disease_name] = 1
        return list(disease_count.keys()),list(disease_count.values())
