from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from matplotlib.style import context
from datetime import datetime
# custom utility fucncs
from utils.utils import getPrice,getExpiringItems,getItembyDestination
# Import all models from all apps
from clinicalservices.models import ClinicalService,AIService,Service
from parasitetreatment.models import ParasiteTreatment,ParasitePrescription
from regulartreatedanimals.models import TreatedAnimal,Disease,Prescription
from registernewuser.models import Kebele,Species,Customer
from vaccination.models import Vaccination,Vaccine
# Import from stock models
from drug_in_out.models import DrugIn,DrugOut, DrugOutCashDeposit
from vaccine_in_out.models import VaccineIn,VaccineOut,VaccineOutCashDeposit
from equipment_in_out.models import ClinicalEquipmentIn,ClinicalEquipmentOut,ClinicalEquipmentCashDeposit
# forms
from .forms import *
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
class VaccinationSummary(LoginRequiredMixin,View):
    login_url =  "/"
    templateUrl = "dashboard/vaccination_summary.html"
    dateForm = DateRangeFrom()

    def get(self,request):
        vaccinationObj = Vaccination.objects.all()
        distByKebele = self.getDistByKebele(Kebele.objects.all(),vaccinationObj)
    
        context = {"vaccinationObj":vaccinationObj,
                    "dateForm":self.dateForm,
                    "totalVaccinations":vaccinationObj.count(),
                    "totalPrice":self.getPrice(vaccinationObj),
                    "distByKebele":distByKebele}

        return render(request,self.templateUrl,context)

    def post(self,request):
        dateForm = DateRangeFrom(request.POST)
        start_date = dateForm['start_date'].value()
        end_date = dateForm['end_date'].value()

        vaccinationObj = Vaccination.objects.filter(service_date__gte=start_date,service_date__lte=end_date)

        distByKebele = self.getDistByKebele(Kebele.objects.all(),vaccinationObj)

        context = {"vaccinationObj":vaccinationObj,
                    "dateForm":dateForm,
                    "totalVaccination":vaccinationObj.count(),
                    "totalPrice":self.getPrice(vaccinationObj),
                    "distByKebele":distByKebele}

        return render(request,self.templateUrl,context)
    
    def getDistByKebele(self,kebeles=None,vaccinationObj=None):
        distByKebele = {}
        for kebele in kebeles:
            for t in  vaccinationObj:
                if t.getKebele() == kebele:
                    if kebele.name in distByKebele:
                        distByKebele[kebele.name] += 1
                    else:
                        distByKebele[kebele.name] = 1
        return distByKebele

    def getPrice(self,vaccinationObj):
        totalPrice = 0
        for v in vaccinationObj:
            for vaccine in v.vaccine_id.all():
                totalPrice += vaccine.getPrice()
        return totalPrice
class VaccinationTypes(LoginRequiredMixin,View):
    vaccines = Vaccine.objects.all()
    vaccinations = Vaccination.objects.all()
    def get(self,request):
        vaccine_names,count = self.getVaccinationPrevalence()
        data = {
            "vaccination_types":vaccine_names,
            "vaccination_count":count,
        }

        return JsonResponse(data)

    def getVaccinationPrevalence(self):
        vaccine_count = {}
        for vaccine in self.vaccines:
            for vaccination in self.vaccinations:
                for v in vaccination.vaccine_id.all():
                    
                    if v == vaccine:
                        if v.vaccine_type in vaccine_count:
                            vaccine_count[v.vaccine_type] += 1
                        else:
                            vaccine_count[v.vaccine_type] = 1

        return list(vaccine_count.keys()),list(vaccine_count.values())
class ArtificialInseminationSummary(LoginRequiredMixin,View):
    login_url =  "/"
    templateUrl = "dashboard/ai_summary.html"
   
    def get(self,request):
        dateForm = DateRangeFrom()
        ai_services = AIService.objects.all()
        distByKebele = self.getDistByKebele(Kebele.objects.all(),ai_services)

        context = {"ai_services":ai_services,
                    "dateForm":dateForm,
                    "totalAIServices":ai_services.count(),
                    "totalPrice":self.getPrice(ai_services),
                    "distByKebele":distByKebele}
        return render(request,self.templateUrl,context)

    def post(self,request):
        dateForm = DateRangeFrom(request.POST)
        start_date = dateForm['start_date'].value()
        end_date = dateForm['end_date'].value()
        ai_services = AIService.objects.filter(service_date__gte=start_date,service_date__lte=end_date)
        distByKebele = self.getDistByKebele(Kebele.objects.all(),ai_services)

        context = {"ai_services":ai_services,
                    "dateForm":dateForm,
                    "totalAIServices":ai_services.count(),
                    "totalPrice":self.getPrice(ai_services),
                    "distByKebele":distByKebele}
        return render(request,self.templateUrl,context)

    def getDistByKebele(self,kebeles=None,ai_services=None):
        distByKebele = {}
        for kebele in kebeles:
            for t in  ai_services:
                if t.getKebele() == kebele:
                    if kebele.name in distByKebele:
                        distByKebele[kebele.name] += 1
                    else:
                        distByKebele[kebele.name] = 1
        return distByKebele

    def getPrice(self,ai_services):
        totalPrice = 0
        for v in ai_services:
            totalPrice += v.getPrice()
        return totalPrice
class DrugInSummary(LoginRequiredMixin,View):
    login_url =  "/"
    templateUrl = "dashboard/drugin_summary.html"
    def get(self,request):
        dateForm = DateRangeFrom()
        drug_typeForm = DrugTypeForm()
        drug_sourceForm = DrugSourceForm()
        in_drugs = DrugIn.objects.all()
        # get total price for all in drugs
        total = getPrice(in_drugs)
        # context
        context = {
            'in_drugs':in_drugs,
            'total_price':total,
            'dateForm':dateForm,
            'drug_typeForm':drug_typeForm,
            'drug_sourceForm':drug_sourceForm,
            'expiringDrugs':getExpiringItems(in_drugs)
        }
        return render(request,self.templateUrl,context)
    def post(self,request):
        dateForm = DateRangeFrom(request.POST)
        drug_typeForm = DrugTypeForm(request.POST)
        drug_sourceForm = DrugSourceForm(request.POST)
        # values
        start_date = dateForm['start_date'].value()
        end_date = dateForm['end_date'].value()
        drug_type = drug_typeForm["drug"].value()
        drug_source = drug_sourceForm["source"].value()
        in_drugs = DrugIn.objects.filter(date_received__gte=start_date,date_received__lte=end_date,drug=drug_type,source=drug_source)
        # get total price for all in drugs
        total = getPrice(in_drugs)
        # context
        context = {
            'in_drugs':in_drugs,
            'total_price':total,
            'dateForm':dateForm,
            'drug_typeForm':drug_typeForm,
            'drug_sourceForm':drug_sourceForm,
            'expiringDrugs':getExpiringItems(in_drugs)
        }
        return render(request,self.templateUrl,context)

class DrugOutSummary(LoginRequiredMixin,View):
    login_url =  "/"
    templateUrl = "dashboard/drugout_summary.html"
    def get(self,request):
        dateForm = DateRangeFrom()
        drug_typeForm = DrugTypeForm()
        drug_destinationForm = DrugDestinationForm()
        out_drugs = DrugOut.objects.all()
        deposited_cash = DrugOutCashDeposit.objects.all()
        # get total price for all in drugs
        total = getPrice(out_drugs)
        # get total deposited cash
        total_deposit = deposited_cash.aggregate(amount_sum = Sum('amount')).get('amount_sum')
        if total_deposit == None:
            total_deposit = 0
        remaining_cash = total- total_deposit
        # context
        context = {
            'out_drugs':out_drugs,
            'total_price':total,
            'total_deposit':total_deposit,
            'remaining_cash':remaining_cash,
            'dateForm':dateForm,
            'drug_typeForm':drug_typeForm,
            'drug_destinationForm':drug_destinationForm,
            'drug_destinations':getItembyDestination(out_drugs)
        }
        return render(request,self.templateUrl,context)
    def post(self,request):
        dateForm = DateRangeFrom(request.POST)
        drug_typeForm = DrugTypeForm(request.POST)
        drug_destinationForm = DrugDestinationForm(request.POST)
        # values
        start_date = dateForm['start_date'].value()
        end_date = dateForm['end_date'].value()
        drug_type = drug_typeForm["drug"].value()
        drug_destination = drug_destinationForm["destination"].value()
        out_drugs = DrugOut.objects.filter(date_received__gte=start_date,date_received__lte=end_date,drug=drug_type,destination=drug_destination)
        deposited_cash = DrugOutCashDeposit.objects.filter(date_paid__gte=start_date,date_paid__lte=end_date)
        # get total price for all in drugs
        total = getPrice(out_drugs)
        # get total deposited cash
        total_deposit = deposited_cash.aggregate(amount_sum = Sum('amount')).get('amount_sum')
        if total_deposit == None:
            total_deposit = 0
        remaining_cash = total - total_deposit
        # context
        context = {
           'out_drugs':out_drugs,
            'total_price':total,
            'total_deposit':total_deposit,
            'remaining_cash':remaining_cash,
            'dateForm':dateForm,
            'drug_typeForm':drug_typeForm,
            'drug_destinationForm':drug_destinationForm,
            'drug_destinations':getItembyDestination(out_drugs)
        }
        return render(request,self.templateUrl,context)
       
class EquipmentInSummary(LoginRequiredMixin,View):
    login_url =  "/"
    templateUrl = "dashboard/equipmentin_summary.html"
    def get(self,request):
        dateForm = DateRangeFrom()
        equipment_typeForm = EquipmentTypeForm()
        equipment_sourceForm = EquipmentSourceForm()
        in_equipments = ClinicalEquipmentIn.objects.all()
        # get total price for all in drugs
        total = getPrice(in_equipments)
        # context
        context = {
            'in_equipments':in_equipments,
            'total_price':total,
            'dateForm':dateForm,
            'equipment_typeForm':equipment_typeForm,
            'equipment_sourceForm':equipment_sourceForm,
            'expiring_equipment':getExpiringItems(in_equipments)
        }
        return render(request,self.templateUrl,context)
    def post(self,request):
        dateForm = DateRangeFrom(request.POST)
        equipment_typeForm = EquipmentTypeForm()
        equipment_sourceForm = EquipmentSourceForm()
        # values
        start_date = dateForm['start_date'].value()
        end_date = dateForm['end_date'].value()
        equipment_type = equipment_typeForm["equipment"].value()
        equipment_source = equipment_sourceForm["source"].value()
   
        in_equipments = ClinicalEquipmentIn.objects.filter(date_received__gte=start_date,date_received__lte=end_date,equipment=equipment_type,source=equipment_source)
        # get total price for all in drugs
        total = getPrice(in_equipments)
        # context
        context = {
            'in_equipments':in_equipments,
            'total_price':total,
            'dateForm':dateForm,
            'equipment_typeForm':equipment_typeForm,
            'equipment_sourceForm':equipment_sourceForm,
            'expiring_equipment':getExpiringItems(in_equipments)
        }
        return render(request,self.templateUrl,context)

class EquipmentOutSummary(LoginRequiredMixin,View):
    login_url =  "/"
    templateUrl = "dashboard/equipmentout_summary.html"
    def get(self,request):
        dateForm = DateRangeFrom()
        equipment_typeForm = EquipmentTypeForm()
        equipment_destinationForm = EquipmentDestinationForm()
        out_equipments = ClinicalEquipmentOut.objects.all()
        deposited_cash = ClinicalEquipmentCashDeposit.objects.all()
        # get total price for all in drugs
        total = getPrice(out_equipments)
        # get total deposited cash
        total_deposit = deposited_cash.aggregate(amount_sum = Sum('amount')).get('amount_sum')
        if total_deposit == None:
            total_deposit = 0
        remaining_cash = total- total_deposit
        # context
        context = {
            'out_equipments':out_equipments,
            'total_price':total,
            'total_deposit':total_deposit,
            'remaining_cash':remaining_cash,
            'dateForm':dateForm,
            'equipment_typeForm':equipment_typeForm,
            'equipment_destinationForm':equipment_destinationForm,
            'equipment_destinations':getItembyDestination(out_equipments)
        }
        return render(request,self.templateUrl,context)
    def post(self,request):
        dateForm = DateRangeFrom(request.POST)
        equipment_typeForm = EquipmentTypeForm()
        equipment_destinationForm = EquipmentDestinationForm()
        # values
        start_date = dateForm['start_date'].value()
        end_date = dateForm['end_date'].value()
        equipment_type = equipment_typeForm["drug"].value()
        equipment_destination = equipment_destinationForm["destination"].value()
        out_equipments = ClinicalEquipmentOut.objects.filter(date_received__gte=start_date,date_received__lte=end_date,drug=equipment_type,destination=equipment_destination)
        # get total price for all in drugs
        total = getPrice(out_equipments)

        deposited_cash = ClinicalEquipmentCashDeposit.objects.filter(date_paid__gte=start_date,date_paid__lte=end_date)
        
        # get total deposited cash
        total_deposit = deposited_cash.aggregate(amount_sum = Sum('amount')).get('amount_sum')
        if total_deposit == None:
            total_deposit = 0
        remaining_cash = total- total_deposit
        # context
        context = {
            'out_equipments':out_equipments,
            'total_price':total,
            'total_deposit':total_deposit,
            'remaining_cash':remaining_cash,
            'dateForm':dateForm,
            'equipment_typeForm':equipment_typeForm,
            'equipment_destinationForm':equipment_destinationForm,
            'equipment_destinations':getItembyDestination(out_equipments)
        }
        return render(request,self.templateUrl,context)

class VaccineInSummary(LoginRequiredMixin,View):
    login_url =  "/"
    templateUrl = "dashboard/vaccinein_summary.html"
    def get(self,request):
        dateForm = DateRangeFrom()
        vaccine_typeForm = VaccineTypeForm()
        vaccine_sourceForm = VaccineSourceForm()
        in_vaccine = VaccineIn.objects.all()
        # get total price for all in drugs
        total = getPrice(in_vaccine)
        # context
        context = {
            'in_drugs':in_vaccine,
            'total_price':total,
            'dateForm':dateForm,
            'vaccine_typeForm':vaccine_typeForm,
            'vaccine_sourceForm':vaccine_sourceForm,
            'expiringVaccines':getExpiringItems(in_vaccine)
        }
        return render(request,self.templateUrl,context)
    def post(self,request):
        dateForm = DateRangeFrom(request.POST)
        vaccine_typeForm = VaccineTypeForm(request.POST)
        vaccine_sourceForm = VaccineSourceForm(request.POST)
        # values
        start_date = dateForm['start_date'].value()
        end_date = dateForm['end_date'].value()
        vaccine_type = vaccine_typeForm["vaccine"].value()
        vaccine_source = vaccine_sourceForm["source"].value()
        in_vaccine = VaccineIn.objects.filter(date_received__gte=start_date,date_received__lte=end_date,vaccine=vaccine_type,source=vaccine_source)
        # get total price for all in drugs
        total = getPrice(in_vaccine)
        # context
        context = {
            'in_drugs':in_vaccine,
            'total_price':total,
            'dateForm':dateForm,
            'vaccine_typeForm':vaccine_typeForm,
            'vaccine_sourceForm':vaccine_sourceForm,
            'expiringVaccines':getExpiringItems(in_vaccine)
        }
        return render(request,self.templateUrl,context)
class VaccineOutSummary(LoginRequiredMixin,View):
    login_url =  "/"
    templateUrl = "dashboard/vaccineout_summary.html"
    def get(self,request):
        dateForm = DateRangeFrom()
        vaccine_typeForm = VaccineTypeForm()
        vaccine_destinationForm = VaccineDestinationForm()
        out_vaccines = VaccineOut.objects.all()
        deposited_cash = VaccineOutCashDeposit.objects.all()
        # get total price for all in drugs
        total = getPrice(out_vaccines)
        # get total deposited cash
        total_deposit = deposited_cash.aggregate(amount_sum = Sum('amount')).get('amount_sum')
        if total_deposit == None:
            total_deposit = 0
        remaining_cash = total- total_deposit
        # context
        context = {
            'out_vaccines':out_vaccines,
            'total_price':total,
            'total_deposit':total_deposit,
            'remaining_cash':remaining_cash,
            'dateForm':dateForm,
            'vaccine_typeForm':vaccine_typeForm,
            'vaccine_destinationForm':vaccine_destinationForm,
            'vaccine_destinations':getItembyDestination(out_vaccines)
        }
        return render(request,self.templateUrl,context)
    def post(self,request):
        dateForm = DateRangeFrom()
        vaccine_typeForm = VaccineTypeForm()
        vaccine_destinationForm = VaccineDestinationForm()
        # values
        start_date = dateForm['start_date'].value()
        end_date = dateForm['end_date'].value()
        vaccine_type = vaccine_typeForm["vaccine"].value()
        vaccine_destination = vaccine_destinationForm["destination"].value()

        out_vaccines = VaccineOut.objects.filter(date_received__gte=start_date,date_received__lte=end_date,drug=vaccine_type,destination=vaccine_destination)
        deposited_cash = DrugOutCashDeposit.objects.filter(date_paid__gte=start_date,date_paid__lte=end_date)
        # get total price for all in drugs
        total = getPrice(out_vaccines)
        # get total deposited cash
        total_deposit = deposited_cash.aggregate(amount_sum = Sum('amount')).get('amount_sum')
        if total_deposit == None:
            total_deposit = 0
        remaining_cash = total - total_deposit
        # context
        context = {
           'out_vaccines':out_vaccines,
            'total_price':total,
            'total_deposit':total_deposit,
            'remaining_cash':remaining_cash,
            'dateForm':dateForm,
            'vaccine_typeForm':vaccine_typeForm,
            'vaccine_destinationForm':vaccine_destinationForm,
            'vaccine_destinations':getItembyDestination(out_vaccines)
        }
        return render(request,self.templateUrl,context)