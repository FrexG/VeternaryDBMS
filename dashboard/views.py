from django.db.models import Sum
from django.dispatch import receiver
from django.shortcuts import render
from django.views import View
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

# custom utility funcs
from utils.utils import getPrice, getExpiringItems, getItembyDestination

# Import all models from all apps
from clinicalservices.models import ClinicalService, AIService, Service
from parasitetreatment.models import ParasiteTreatment, ParasitePrescription
from regulartreatedanimals.models import TreatedAnimal, Disease, Treatment, Prescription
from registernewuser.models import Kebele, Species, Customer
from vaccination.models import Vaccination, Vaccine
from stock.models import ClinicalEquipmentStock, DrugStock, VaccineStock
from receipt_in_out.models import ReceiptIn, ReceiptOut

# Import from stock models
from drug_in_out.models import DrugIn, DrugOut, DrugOutCashDeposit
from vaccine_in_out.models import VaccineIn, VaccineOut, VaccineOutCashDeposit
from equipment_in_out.models import ClinicalEquipmentIn, ClinicalEquipmentOut

# Import Lab exam models
from lab_exam.models import LabExamRequest, LabTechnique, LabResult
from abattoir_exam.models import AbattoirExam

# forms
from .forms import *

# Create your views here.


class Index(LoginRequiredMixin, View):
    login_url = "/"
    templateURL = "dashboard/dashboard.html"
    kebeles = list(Kebele.objects.all())

    def get(self, request):
        print("Called")
        return render(request, self.templateURL)


class DashboardData(LoginRequiredMixin, View):
    diseases = Disease.objects.all()
    kebeles = Kebele.objects.all()
    species = Species.objects.all()
    customers = Customer.objects.all()
    clinical_service = ClinicalService.objects.all()
    ai_service = AIService.objects.all()
    parasite_treatment = ParasiteTreatment.objects.all()
    treated_animals = TreatedAnimal.objects.all()
    regular_treatment = Treatment.objects.all()
    vaccination = Vaccination.objects.all()

    def get(self, request):
        disease_name, count = self.getDiseasePrevalence()
        data = {
            "kebele_names": [kebele.name for kebele in self.kebeles],
            "kebele_count": self.kebeleCount(),
            "species_names": [species.getSpeciesName() for species in self.species],
            "species_count": self.speciesCount(),
            "service_names": [
                "Clinical Service",
                "AI Service",
                "Parasite Treatment",
                "Regular Treatment",
                "Lab Exam",
                "Abattoir Exam",
            ],
            "service_count": [
                ClinicalService.objects.count(),
                AIService.objects.count(),
                ParasiteTreatment.objects.count(),
                TreatedAnimal.objects.count(),
                LabExamRequest.objects.count(),
                AbattoirExam.objects.count(),
            ],
            "disease_names": disease_name,
            "disease_count": count,
        }
        return JsonResponse(data)

    def kebeleCount(self):
        count = []
        for kebele in self.kebeles:
            i = 0
            for s in [ClinicalService, AIService, ParasiteTreatment, TreatedAnimal]:
                for obj in s.objects.all():
                    if obj.getKebele() == kebele:
                        i += 1
            count.append(i)
        return count

    def speciesCount(self):
        count = []
        for species in self.species:
            i = 0
            for x in [
                self.vaccination,
                self.ai_service,
                self.parasite_treatment,
                self.treated_animals,
            ]:
                for obj in x:
                    if obj.species == species:
                        i += 1
            count.append(i)
        return count

    def getDiseasePrevalence(self):
        disease_count = {}
        for disease in self.diseases:
            for x in [self.regular_treatment, self.parasite_treatment]:
                for obj in x:
                    for dx in obj.dx.all():
                        if dx == disease:
                            if disease.disease_name in disease_count:
                                disease_count[disease.disease_name] += 1
                            else:
                                disease_count[disease.disease_name] = 1
        return list(disease_count.keys()), list(disease_count.values())


class RegularTreatmentSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/regular_treatment_summary.html"
    dateForm = DateRangeFrom()
    case_holder_form = CaseHolderForm()

    def get(self, request):
        treatmentObj = Treatment.objects.all()
        treatedAnimals = TreatedAnimal.objects.all()

        prescriptions = Prescription.objects.all()

        distByKebele = self.getDistByKebele(Kebele.objects.all(), treatedAnimals)

        context = {
            "treatmentObj": treatmentObj,
            "prescriptions": prescriptions,
            "dateForm": self.dateForm,
            "case_holder_form": self.case_holder_form,
            "totalTreatedAnimals": treatedAnimals.count(),
            "totalPrice": self.getPrice(treatmentObj),
            "distByKebele": distByKebele,
        }

        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        case_holder_form = CaseHolderForm(request.POST)

        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        case_holder = case_holder_form["case_holder"].value()

        treatmentObj = Treatment.objects.filter(
            treatment_id__service_date__gte=start_date,
            treatment_id__service_date__lte=end_date,
            treatment_id__case_holder=case_holder,
        )
        prescriptions = Prescription.objects.all()
        treatedAnimals = TreatedAnimal.objects.all()
        distByKebele = self.getDistByKebele(Kebele.objects.all(), treatedAnimals)

        context = {
            "treatmentObj": treatmentObj,
            "dateForm": self.dateForm,
            "prescriptions": prescriptions,
            "case_holder_form": self.case_holder_form,
            "totalTreatedAnimals": treatedAnimals.count(),
            "totalPrice": self.getPrice(treatmentObj),
            "distByKebele": distByKebele,
        }

        return render(request, self.templateUrl, context)

    def getDistByKebele(self, kebeles=None, TreatedAnimalsObj=None):
        distByKebele = {}

        for t in TreatedAnimalsObj:
            if t.getKebele().name in distByKebele:
                distByKebele[t.getKebele().name] += 1
            else:
                distByKebele[t.getKebele().name] = 1

        return distByKebele

    def getPrice(self, treatmentObj):
        totalPrice = 0

        for treatment in treatmentObj:
            for prescription in Prescription.objects.filter(treatment=treatment):
                totalPrice += prescription.getPrice()

        return totalPrice


class RegularTreatmentTypes(LoginRequiredMixin, View):
    diseases = Disease.objects.all()
    treatment = Treatment.objects.all()

    def get(self, request):
        disease_name, count = self.getDiseasePrevalence()
        data = {
            "disease_names": disease_name,
            "disease_count": count,
        }

        return JsonResponse(data)

    def getDiseasePrevalence(self):
        disease_count = {}
        for treatment in self.treatment:
            for dx in treatment.dx.all():
                if dx.disease_name in disease_count:
                    disease_count[dx.disease_name] += 1
                else:
                    disease_count[dx.disease_name] = 1

        return list(disease_count.keys()), list(disease_count.values())


class ClinicalServiceSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/clinical_service_summary.html"
    dateForm = DateRangeFrom()
    caseHolderForm = CaseHolderForm()
    serviceTypeForm = ServieTypeForm()

    def get(self, request):
        clinicalServicesObj = ClinicalService.objects.all()
        distByKebele = self.getDistByKebele(Kebele.objects.all(), clinicalServicesObj)
        print(ClinicalService.objects.aggregate(Sum("service_type__price")))
        context = {
            "clinicalServicesObj": clinicalServicesObj,
            "dateForm": self.dateForm,
            "caseHolderForm": self.caseHolderForm,
            "serviceTypeForm": self.serviceTypeForm,
            "totalClinicalServices": clinicalServicesObj.count(),
            "totalPrice": clinicalServicesObj.aggregate(
                sum_price=Sum("service_type__price")
            ),
            "distByKebele": distByKebele,
        }

        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        caseHolderForm = CaseHolderForm(request.POST)
        serviceTypeForm = ServieTypeForm(request.POST)

        case_holder = caseHolderForm["case_holder"].value()

        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()

        clinicalServicesObj = ClinicalService.objects.filter(
            service_date__gte=start_date,
            service_date__lte=end_date,
            case_holder=case_holder,
            service_type=serviceTypeForm["service_type"].value(),
        )

        distByKebele = self.getDistByKebele(Kebele.objects.all(), clinicalServicesObj)

        context = {
            "clinicalServicesObj": clinicalServicesObj,
            "dateForm": dateForm,
            "caseHolderForm": caseHolderForm,
            "serviceTypeForm": serviceTypeForm,
            "totalClinicalServices": clinicalServicesObj.count(),
            "totalPrice": clinicalServicesObj.aggregate(
                sum_price=Sum("service_type__price")
            ),
            "distByKebele": distByKebele,
        }

        return render(request, self.templateUrl, context)

    def getDistByKebele(self, kebeles=None, ClinicalServicesObj=None):
        distByKebele = {}
        for kebele in kebeles:
            for t in ClinicalServicesObj:
                if t.getKebele() == kebele:
                    if kebele.name in distByKebele:
                        distByKebele[kebele.name] += 1
                    else:
                        distByKebele[kebele.name] = 1
        return distByKebele


class ClinicalServiceTypes(LoginRequiredMixin, View):
    def get(self, request):
        service_types = Service.objects.all()
        clinical_service = ClinicalService.objects.all()

        data = {
            "service_types": [
                service_names.getServiceName() for service_names in service_types
            ],
            "counts": [
                ClinicalService.objects.filter(service_type=service).count()
                for service in service_types
            ],
        }
        return JsonResponse(data)


class ParasiteTreatmentSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/parasite_treatment_summary.html"
    dateForm = DateRangeFrom()
    caseHolderForm = CaseHolderForm()
    treatmentTypeForm = TreatmentTypeForm()

    def get(self, request):
        parasiteTreatmentObj = ParasiteTreatment.objects.all()
        parasitePrescriptionObj = ParasitePrescription.objects.all()

        distByKebele = self.getDistByKebele(Kebele.objects.all(), parasiteTreatmentObj)

        context = {
            "parasiteTreatmentObj": parasiteTreatmentObj,
            "parasitePrescriptionObj": parasitePrescriptionObj,
            "dateForm": self.dateForm,
            "caseHolderForm": self.caseHolderForm,
            "treatmentTypeForm": self.treatmentTypeForm,
            "totalTreatments": parasiteTreatmentObj.count(),
            "totalPrice": self.getPrice(parasiteTreatmentObj),
            "distByKebele": distByKebele,
        }

        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        caseHolderForm = CaseHolderForm(request.POST)
        treatmentTypeForm = TreatmentTypeForm(request.POST)

        case_holder = caseHolderForm["case_holder"].value()

        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()

        parasiteTreatmentObj = ParasiteTreatment.objects.filter(
            service_date__gte=start_date,
            service_date__lte=end_date,
            case_holder=case_holder,
            treatment_type=treatmentTypeForm["treatment_type"].value(),
        )

        parasitePrescriptionObj = ParasitePrescription.objects.filter(
            treatment__service_date__gte=start_date,
            treatment__service_date__lte=end_date,
            treatment__case_holder=case_holder,
            treatment__treatment_type=treatmentTypeForm["treatment_type"].value(),
        )

        distByKebele = self.getDistByKebele(Kebele.objects.all(), parasiteTreatmentObj)

        context = {
            "parasiteTreatmentObj": parasiteTreatmentObj,
            "parasitePrescriptionObj": parasitePrescriptionObj,
            "dateForm": dateForm,
            "caseHolderForm": caseHolderForm,
            "treatmentTypeForm": treatmentTypeForm,
            "totalClinicalServices": parasiteTreatmentObj.count(),
            "totalPrice": self.getPrice(parasiteTreatmentObj),
            "distByKebele": distByKebele,
        }

        return render(request, self.templateUrl, context)

    def getDistByKebele(self, kebeles=None, ClinicalServicesObj=None):
        distByKebele = {}
        for kebele in kebeles:
            for t in ClinicalServicesObj:
                if t.getKebele() == kebele:
                    if kebele.name in distByKebele:
                        distByKebele[kebele.name] += 1
                    else:
                        distByKebele[kebele.name] = 1
        return distByKebele

    def getPrice(self, parasiteTreatmentObj):
        totalPrice = 0
        for pp in ParasitePrescription.objects.filter():
            for p in parasiteTreatmentObj:
                if pp.treatment == p:
                    print(pp.getPrice())
                    totalPrice += pp.getPrice()
        return totalPrice


class ParasiteTreatmentTypes(LoginRequiredMixin, View):
    diseases = Disease.objects.all()
    parasite_treatment = ParasiteTreatment.objects.all()

    def get(self, request):
        treatment_names = ["Internal", "External"]
        disease_name, count = self.getDiseasePrevalence()
        data = {
            "treatment_types": treatment_names,
            "treatment_count": [
                ParasiteTreatment.objects.filter(treatment_type=treatment).count()
                for treatment in treatment_names
            ],
            "disease_names": disease_name,
            "disease_count": count,
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
        return list(disease_count.keys()), list(disease_count.values())


class AbattoirExamSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/abattoir_exam_summary.html"
    dateForm = DateRangeFrom()
    hotelForm = HotelSelectForm()

    def get(self, request):
        abattoir_exam_ojb = AbattoirExam.objects.all()
        total = abattoir_exam_ojb.count()

        context = {
            "abattoir_exam": abattoir_exam_ojb,
            "dateForm": self.dateForm,
            "hotelForm": self.hotelForm,
            "total": total,
        }
        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        hotelForm = HotelSelectForm(request.POST)

        hotel = hotelForm["hotel"].value()
        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()

        abattoir_exam_ojb = AbattoirExam.objects.filter(
            date__gte=start_date, date__lte=end_date, hotel=hotel
        )
        total = abattoir_exam_ojb.count()

        context = {
            "abattoir_exam": abattoir_exam_ojb,
            "dateForm": self.dateForm,
            "hotelForm": self.hotelForm,
            "total": total,
        }
        return render(request, self.templateUrl, context)


class VaccinationSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/vaccination_summary.html"
    dateForm = DateRangeFrom()
    case_holder_form = CaseHolderForm()

    def get(self, request):
        vaccinationObj = Vaccination.objects.all()
        distByKebele = self.getDistByKebele(Kebele.objects.all(), vaccinationObj)

        context = {
            "vaccinationObj": vaccinationObj,
            "dateForm": self.dateForm,
            "case_holder_form": self.case_holder_form,
            "totalVaccinations": vaccinationObj.count(),
            "totalPrice": self.getPrice(vaccinationObj),
            "distByKebele": distByKebele,
        }

        return render(request, self.templateUrl, context)

    def post(self, request):
        case_holder_form = CaseHolderForm(request.POST)
        dateForm = DateRangeFrom(request.POST)

        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        case_holder = case_holder_form["case_holder"].value()

        vaccinationObj = Vaccination.objects.filter(
            service_date__gte=start_date,
            service_date__lte=end_date,
            case_holder=case_holder,
        )

        distByKebele = self.getDistByKebele(Kebele.objects.all(), vaccinationObj)

        context = {
            "vaccinationObj": vaccinationObj,
            "dateForm": dateForm,
            "case_holder_form": self.case_holder_form,
            "totalVaccination": vaccinationObj.count(),
            "totalPrice": self.getPrice(vaccinationObj),
            "distByKebele": distByKebele,
        }

        return render(request, self.templateUrl, context)

    def getDistByKebele(self, kebeles=None, vaccinationObj=None):
        distByKebele = {}
        for kebele in kebeles:
            for t in vaccinationObj:
                if t.getKebele() == kebele:
                    if kebele.name in distByKebele:
                        distByKebele[kebele.name] += 1
                    else:
                        distByKebele[kebele.name] = 1
        return distByKebele

    def getPrice(self, vaccinationObj):
        totalPrice = 0
        for v in vaccinationObj:
            for vaccine in v.vaccine_id.all():
                print(vaccine.getDispenceryPrice())
                totalPrice += vaccine.getDispenceryPrice() * v.quantity
        return totalPrice


class VaccinationTypes(LoginRequiredMixin, View):
    vaccines = Vaccine.objects.all()
    vaccinations = Vaccination.objects.all()

    def get(self, request):
        vaccine_names, count = self.getVaccinationPrevalence()
        data = {
            "vaccination_types": vaccine_names,
            "vaccination_count": count,
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

        return list(vaccine_count.keys()), list(vaccine_count.values())


class ArtificialInseminationSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/ai_summary.html"

    def get(self, request):
        dateForm = DateRangeFrom()
        case_holder_form = CaseHolderForm()
        ai_services = AIService.objects.all()
        distByKebele = self.getDistByKebele(Kebele.objects.all(), ai_services)

        context = {
            "ai_services": ai_services,
            "dateForm": dateForm,
            "case_holder_form": case_holder_form,
            "totalAIServices": ai_services.count(),
            "totalPrice": self.getPrice(ai_services),
            "totalServices": ai_services.count(),
            "distByKebele": distByKebele,
        }
        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        case_holder_form = CaseHolderForm(request.POST)

        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        case_holder = case_holder_form["case_holder"].value()

        ai_services = AIService.objects.filter(
            service_date__gte=start_date,
            service_date__lte=end_date,
            case_holder=case_holder,
        )
        distByKebele = self.getDistByKebele(Kebele.objects.all(), ai_services)

        context = {
            "ai_services": ai_services,
            "dateForm": dateForm,
            "case_holder_form": case_holder_form,
            "totalAIServices": ai_services.count(),
            "totalPrice": self.getPrice(ai_services),
            "totalServices": ai_services.count(),
            "distByKebele": distByKebele,
        }
        return render(request, self.templateUrl, context)

    def getDistByKebele(self, kebeles=None, ai_services=None):
        distByKebele = {}
        for kebele in kebeles:
            for t in ai_services:
                if t.getKebele() == kebele:
                    if kebele.name in distByKebele:
                        distByKebele[kebele.name] += 1
                    else:
                        distByKebele[kebele.name] = 1
        return distByKebele

    def getPrice(self, ai_services):
        totalPrice = 0
        for v in ai_services:
            totalPrice += v.getPrice()
        return totalPrice


class DrugInSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/drugin_summary.html"

    def get(self, request):
        dateForm = DateRangeFrom()
        drug_typeForm = DrugTypeForm()
        drug_sourceForm = DrugSourceForm()
        in_drugs = DrugIn.objects.all()
        # get total price for all in drugs
        total = getPrice(in_drugs)
        # context
        context = {
            "in_drugs": in_drugs,
            "total_price": total,
            "dateForm": dateForm,
            "drug_typeForm": drug_typeForm,
            "drug_sourceForm": drug_sourceForm,
            "expiringDrugs": getExpiringItems(in_drugs),
        }
        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        drug_typeForm = DrugTypeForm(request.POST)
        drug_sourceForm = DrugSourceForm(request.POST)
        # values
        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        drug_type = drug_typeForm["drug"].value()
        drug_source = drug_sourceForm["source"].value()
        in_drugs = DrugIn.objects.filter(
            date__gte=start_date, date__lte=end_date, drug=drug_type, source=drug_source
        )
        # get total price for all in drugs
        total = getPrice(in_drugs)
        # context
        context = {
            "in_drugs": in_drugs,
            "total_price": total,
            "dateForm": dateForm,
            "drug_typeForm": drug_typeForm,
            "drug_sourceForm": drug_sourceForm,
            "expiringDrugs": getExpiringItems(in_drugs),
        }
        return render(request, self.templateUrl, context)


class DrugOutSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/drugout_summary.html"

    def get(self, request):
        dateForm = DateRangeFrom()
        # drug_typeForm = DrugTypeForm()
        drug_receiverForm = DrugReceiverForm()
        out_drugs = DrugOut.objects.all()
        deposited_cash = DrugOutCashDeposit.objects.all()
        # get total price for all in drugs
        total = getPrice(out_drugs)
        # get total deposited cash
        total_deposit = deposited_cash.aggregate(amount_sum=Sum("amount")).get(
            "amount_sum"
        )
        if total_deposit == None:
            total_deposit = 0
        remaining_cash = total - total_deposit
        # context
        context = {
            "out_drugs": out_drugs,
            "total_price": total,
            "total_deposit": total_deposit,
            "remaining_cash": remaining_cash,
            "dateForm": dateForm,
            "drug_cash_deposit": deposited_cash,
            #'drug_typeForm':drug_typeForm,
            "drug_receiverForm": drug_receiverForm,
            "drug_destinations": getItembyDestination(out_drugs),
        }
        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        # drug_typeForm = DrugTypeForm(request.POST)
        drug_receiverForm = DrugReceiverForm(request.POST)
        # values
        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        # drug_type = drug_typeForm["drug"].value()
        drug_receiver = drug_receiverForm["kebele"].value()
        out_drugs = DrugOut.objects.filter(
            date__gte=start_date, date__lte=end_date, kebele=drug_receiver
        )
        deposited_cash = DrugOutCashDeposit.objects.filter(
            date_paid__gte=start_date,
            date_paid__lte=end_date,
        )
        # get total price for all in drugs
        total = getPrice(out_drugs)
        # get total deposited cash
        total_deposit = deposited_cash.aggregate(amount_sum=Sum("amount")).get(
            "amount_sum"
        )
        if total_deposit == None:
            total_deposit = 0
        remaining_cash = total - total_deposit
        # context
        context = {
            "out_drugs": out_drugs,
            "total_price": total,
            "total_deposit": total_deposit,
            "remaining_cash": remaining_cash,
            "dateForm": dateForm,
            "drug_cash_deposit": deposited_cash,
            #'drug_typeForm':drug_typeForm,
            "drug_receiverForm": drug_receiverForm,
            "drug_destinations": getItembyDestination(out_drugs),
        }
        return render(request, self.templateUrl, context)


class EquipmentInSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/equipmentin_summary.html"

    def get(self, request):
        dateForm = DateRangeFrom()
        equipment_typeForm = EquipmentTypeForm()
        equipment_sourceForm = EquipmentSourceForm()
        in_equipments = ClinicalEquipmentIn.objects.all()
        # context
        context = {
            "in_equipments": in_equipments,
            "total_quantity": in_equipments.count(),
            "dateForm": dateForm,
            "equipment_typeForm": equipment_typeForm,
            "equipment_sourceForm": equipment_sourceForm,
        }
        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        equipment_typeForm = EquipmentTypeForm(request.POST)
        equipment_sourceForm = EquipmentSourceForm(request.POST)
        # values
        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        equipment_type = equipment_typeForm["equipment"].value()
        equipment_source = equipment_sourceForm["source"].value()
        print(equipment_source)

        in_equipments = ClinicalEquipmentIn.objects.filter(
            date_received__gte=start_date,
            date_received__lte=end_date,
            equipment=equipment_type,
            source=equipment_source,
        )

        # context
        context = {
            "in_equipments": in_equipments,
            "total_quantity": in_equipments.count(),
            "dateForm": dateForm,
            "equipment_typeForm": equipment_typeForm,
            "equipment_sourceForm": equipment_sourceForm,
        }
        return render(request, self.templateUrl, context)


class EquipmentOutSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/equipmentout_summary.html"

    def get(self, request):
        dateForm = DateRangeFrom()
        equipment_typeForm = EquipmentTypeForm()
        equipment_receiverForm = EquipmentReceiverForm()
        out_equipments = ClinicalEquipmentOut.objects.all()

        # context
        context = {
            "out_equipments": out_equipments,
            "total_quantity": out_equipments.count(),
            "dateForm": dateForm,
            "equipment_typeForm": equipment_typeForm,
            "equipment_receiverForm": equipment_receiverForm,
            "equipment_destinations": getItembyDestination(out_equipments),
        }
        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        equipment_typeForm = EquipmentTypeForm(request.POST)
        equipment_receiverForm = EquipmentReceiverForm(request.POST)
        # values
        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        equipment_type = equipment_typeForm["equipment"].value()
        equipment_receiver = equipment_receiverForm["kebele"].value()
        print(equipment_receiver)
        out_equipments = ClinicalEquipmentOut.objects.filter(
            date__gte=start_date,
            date__lte=end_date,
            equipment=equipment_type,
            kebele=equipment_receiver,
        )

        context = {
            "out_equipments": out_equipments,
            "total_quantity": out_equipments.count(),
            "dateForm": dateForm,
            "equipment_typeForm": equipment_typeForm,
            "equipment_receiverForm": equipment_receiverForm,
            "equipment_destinations": getItembyDestination(out_equipments),
        }
        return render(request, self.templateUrl, context)


class VaccineInSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/vaccinein_summary.html"

    def get(self, request):
        dateForm = DateRangeFrom()
        vaccine_typeForm = VaccineTypeForm()
        vaccine_sourceForm = VaccineSourceForm()
        in_vaccine = VaccineIn.objects.all()
        # get total price for all in drugs
        total = getPrice(in_vaccine)
        # context
        context = {
            "in_vaccines": in_vaccine,
            "total_price": total,
            "dateForm": dateForm,
            "vaccine_typeForm": vaccine_typeForm,
            "vaccine_sourceForm": vaccine_sourceForm,
            "expiringVaccines": getExpiringItems(in_vaccine),
        }
        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        vaccine_typeForm = VaccineTypeForm(request.POST)
        vaccine_sourceForm = VaccineSourceForm(request.POST)
        # values
        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        vaccine_type = vaccine_typeForm["vaccine"].value()
        vaccine_source = vaccine_sourceForm["source"].value()
        in_vaccine = VaccineIn.objects.filter(
            date_received__gte=start_date,
            date_received__lte=end_date,
            vaccine=vaccine_type,
            source=vaccine_source,
        )
        # get total price for all in drugs
        total = getPrice(in_vaccine)
        # context
        context = {
            "in_vaccines": in_vaccine,
            "total_price": total,
            "dateForm": dateForm,
            "vaccine_typeForm": vaccine_typeForm,
            "vaccine_sourceForm": vaccine_sourceForm,
            "expiringVaccines": getExpiringItems(in_vaccine),
        }
        return render(request, self.templateUrl, context)


class VaccineOutSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/vaccineout_summary.html"

    def get(self, request):
        dateForm = DateRangeFrom()
        # vaccine_typeForm = VaccineTypeForm()
        vaccine_receiverForm = VaccineReceiverForm()
        out_vaccines = VaccineOut.objects.all()
        deposited_cash = VaccineOutCashDeposit.objects.all()
        # get total price for all in drugs
        total = getPrice(out_vaccines)
        # get total deposited cash
        total_deposit = deposited_cash.aggregate(amount_sum=Sum("amount")).get(
            "amount_sum"
        )
        if total_deposit == None:
            total_deposit = 0
        remaining_cash = total - total_deposit
        # context
        context = {
            "out_vaccines": out_vaccines,
            "total_price": total,
            "total_deposit": total_deposit,
            "remaining_cash": remaining_cash,
            "dateForm": dateForm,
            "vaccine_cash_deposit": deposited_cash,
            #'vaccine_typeForm':vaccine_typeForm,
            "vaccine_receiverForm": vaccine_receiverForm,
            "vaccine_destinations": getItembyDestination(out_vaccines),
        }
        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        # vaccine_typeForm = VaccineTypeForm(request.POST)
        vaccine_receiverForm = VaccineReceiverForm(request.POST)

        # values
        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        # vaccine_type = vaccine_typeForm["vaccine"].value()
        vaccine_receiver = vaccine_receiverForm["kebele"].value()

        out_vaccines = VaccineOut.objects.filter(
            date__gte=start_date, date__lte=end_date, kebele=vaccine_receiver
        )
        deposited_cash = VaccineOutCashDeposit.objects.filter(
            date_paid__gte=start_date,
            date_paid__lte=end_date,
        )
        # get total price for all in drugs
        total = getPrice(out_vaccines)
        # get total deposited cash
        total_deposit = deposited_cash.aggregate(amount_sum=Sum("amount")).get(
            "amount_sum"
        )
        if total_deposit == None:
            total_deposit = 0
        remaining_cash = total - total_deposit
        # context
        context = {
            "out_vaccines": out_vaccines,
            "total_price": total,
            "total_deposit": total_deposit,
            "remaining_cash": remaining_cash,
            "dateForm": dateForm,
            "vaccine_cash_deposit": deposited_cash,
            #'vaccine_typeForm':vaccine_typeForm,
            "vaccine_receiverForm": vaccine_receiverForm,
            "vaccine_destinations": getItembyDestination(out_vaccines),
        }
        return render(request, self.templateUrl, context)


class LabExamSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/lab_exam_summary.html"

    def get(self, request):
        dateForm = DateRangeFrom()
        case_holder_form = CaseHolderForm()
        lab_exam_Obj = LabExamRequest.objects.filter(paid=True)
        lab_results = LabResult.objects.all()

        dist_by_exam_technique = self.getDistByTechnique(
            LabTechnique.objects.all(), lab_exam_Obj
        )
        print(f"Dist = {dist_by_exam_technique}")
        context = {
            "lab_results": lab_results,
            "dateForm": dateForm,
            "case_holder_form": case_holder_form,
            "total_lab_exam": lab_exam_Obj.count(),
            "totalPrice": lab_exam_Obj.aggregate(sum_price=Sum("lab_technique__price")),
            "dist_by_exam_technique": dist_by_exam_technique,
        }

        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        case_holder_form = CaseHolderForm(request.POST)

        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        case_holder = case_holder_form["case_holder"].value()

        lab_results = LabResult.objects.filter(
            date__gte=start_date, date__lte=end_date, case_holder=case_holder
        )
        lab_exam_Obj = LabExamRequest.objects.filter(paid=True)
        dist_by_exam_technique = self.getDistByTechnique(
            LabTechnique.objects.all(), lab_exam_Obj
        )

        context = {
            "lab_results": lab_results,
            "dateForm": dateForm,
            "case_holder_form": case_holder_form,
            "total_lab_exam": lab_exam_Obj.count(),
            "totalPrice": lab_exam_Obj.aggregate(sum_price=Sum("lab_technique__price")),
            "dist_by_exam_technique": dist_by_exam_technique,
        }
        return render(request, self.templateUrl, context)

    def getDistByTechnique(self, Techniques=None, lab_exam_Obj=None):
        distByTechnique = {}
        for technique in Techniques:
            for exam in lab_exam_Obj:
                if exam.lab_technique == technique:
                    if technique.lab_technique in distByTechnique:
                        distByTechnique[technique.lab_technique] += 1
                    else:
                        distByTechnique[technique.lab_technique] = 1
        return distByTechnique


class ReceiptInSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/receiptin_summary.html"

    def get(self, request):
        dateForm = DateRangeFrom()
        receipt_typeForm = ReceiptTypeForm()
        in_receipt = ReceiptIn.objects.all()

        total_quantity = in_receipt.count()
        # context
        context = {
            "in_receipt": in_receipt,
            "total_quantity": total_quantity,
            "dateForm": dateForm,
            "receipt_typeForm": receipt_typeForm,
        }
        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        receipt_typeForm = ReceiptTypeForm(request.POST)

        # values
        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        receipt_type = receipt_typeForm["receipt_type"].value()

        in_receipt = ReceiptIn.objects.filter(
            date__gte=start_date, date__lte=end_date, receipt_type=receipt_type
        )
        # get total quantity
        total_quantity = in_receipt.count()
        # context
        context = {
            "in_receipt": in_receipt,
            "total_quantity": total_quantity,
            "dateForm": dateForm,
            "receipt_typeForm": receipt_typeForm,
        }
        return render(request, self.templateUrl, context)


class ReceiptOutSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/receiptout_summary.html"

    def get(self, request):
        dateForm = DateRangeFrom()
        kebeleForm = KebeleTypeForm()
        out_receipt = ReceiptOut.objects.all()

        total_quantity = out_receipt.count()
        # context
        context = {
            "out_receipt": out_receipt,
            "total_quantity": total_quantity,
            "dateForm": dateForm,
            "kebeleForm": kebeleForm,
        }
        return render(request, self.templateUrl, context)

    def post(self, request):
        dateForm = DateRangeFrom(request.POST)
        kebeleForm = KebeleTypeForm(request.POST)

        # values
        start_date = dateForm["start_date"].value()
        end_date = dateForm["end_date"].value()
        kebele = kebeleForm["kebele"].value()

        out_receipt = ReceiptOut.objects.filter(
            date__gte=start_date, date__lte=end_date, kebele=kebele
        )
        # get total quantity
        total_quantity = out_receipt.count()
        # context
        context = {
            "out_receipt": out_receipt,
            "total_quantity": total_quantity,
            "dateForm": dateForm,
            "kebeleForm": kebeleForm,
        }
        return render(request, self.templateUrl, context)


# Stock Summary
class StockSummary(LoginRequiredMixin, View):
    login_url = "/"
    templateUrl = "dashboard/stock_summary.html"

    def get(self, request):
        stock_select_form = StockSelectForm()
        drug_stock = DrugStock.objects.all()
        total_price = sum([s.quantity * s.drug.stock_price for s in drug_stock])

        # context
        context = {
            "stock_type": "Drug",
            "stock": drug_stock,
            "total": total_price,
            "stock_select_form": stock_select_form,
        }
        return render(request, self.templateUrl, context)

    def post(self, request):
        stock_select_form = StockSelectForm(request.POST)

        stock_type = stock_select_form["stock_type"].value()
        stock = None
        total_price = 0

        if stock_type == "Drug":
            stock = DrugStock.objects.all()
            total = sum([s.quantity * s.drug.stock_price for s in stock])
            stock_type = "Drug"

        elif stock_type == "Equipment":
            stock = ClinicalEquipmentStock.objects.all()
            total = sum([s.quantity for s in stock])
            stock_type = "Equipment"

        elif stock_type == "Vaccine":
            stock = VaccineStock.objects.all()
            total = sum([s.quantity * s.vaccine.stock_price for s in stock])
            print(total_price)
            stock_type = "Vaccine"

        # context
        context = {
            "stock_type": stock_type,
            "stock": stock,
            "total": total,
            "stock_select_form": stock_select_form,
        }
        return render(request, self.templateUrl, context)
