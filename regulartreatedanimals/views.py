from encodings import search_function
from django.shortcuts import render, redirect
from django.views import View
from .models import TreatedAnimal
from .forms import *
from lab_exam.forms import LabExamRequestForm
from lab_exam.models import LabResult
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

# Create your views here.

class Index(LoginRequiredMixin, View):
    login_url = "/"
    templateURL = 'regulartreatedanimals/regular.html'
    def get(self, request):  
        treated_animals_form = TreatedAnimalsForm(initial={'case_holder': request.user})
        treatment_form = TreatmentForm()
        rx_formset = PrescriptionFormSet()
        lab_exam_request_form = LabExamRequestForm()
        search_form = SearchTreatmentHistoryForm()
        lab_results = LabResult.objects.filter(date=datetime.now().date(),treatment_delivered=False)

        context = {'treated_animals_form':treated_animals_form,
                    'lab_exam_request_form':lab_exam_request_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset,
                    'lab_results':lab_results}

        return render(request, self.templateURL, context)

    def post(self, request):
        treated_animals_form = TreatedAnimalsForm(request.POST)
        rx_formset = PrescriptionFormSet()
        treatment_form = TreatmentForm()
        lab_exam_request_form = LabExamRequestForm()
        search_form = SearchTreatmentHistoryForm()
        lab_results = LabResult.objects.filter(date=datetime.now().date())

        if treated_animals_form.is_valid():
            treatmentID = treated_animals_form.save()

            treatment_form = TreatmentForm(initial={'treatment_id': treatmentID})
            lab_exam_request_form = LabExamRequestForm(initial={'treated_animal': treatmentID})
            lab_results = LabResult.objects.filter(date=datetime.now().date(),treatment_delivered=False)

            context = {'treated_animals_form':treated_animals_form,
                    'lab_exam_request_form':lab_exam_request_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset,
                    'lab_results':lab_results}

            return render(request, self.templateURL, context)

        else:
            context = {'treated_animals_form':treated_animals_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset}
            return render(request, self.templateURL, context)

class LabRequestView(LoginRequiredMixin,View):
    login_url = "/"
    templateURL = 'regulartreatedanimals/regular.html'
    def post(self, request):
        treated_animals_form = TreatedAnimalsForm()
        rx_formset = PrescriptionFormSet()
        treatment_form = TreatmentForm()
        lab_exam_request_form = LabExamRequestForm(request.POST)
        search_form = SearchTreatmentHistoryForm()
        lab_results = LabResult.objects.filter(date=datetime.now().date(),treatment_delivered=False)

        if lab_exam_request_form.is_valid():
            lab_request_id = lab_exam_request_form.save()
            treatment_form = TreatmentForm(initial={'treatment_id': lab_request_id.treated_animal})
            
            context = {'treated_animals_form':treated_animals_form,
                    'lab_exam_request_form':lab_exam_request_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset,
                    'lab_results':lab_results}

            return render(request, self.templateURL, context)

        else:
            context = {'treated_animals_form':treated_animals_form,
                    'lab_exam_request_form':lab_exam_request_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset,
                    'lab_results':lab_results}
            return render(request, self.templateURL, context)

class LabResultView(LoginRequiredMixin,View):
    login_url = "/"
    templateURL = 'regulartreatedanimals/regular.html'
    def post(self, request, pk):
        lab_result = LabResult.objects.get(pk=pk)
        lab_result.treatment_delivered = True
        lab_result.save()

        treated_animals_form = TreatedAnimalsForm()
        rx_formset = PrescriptionFormSet()
        treatment_form = TreatmentForm()
        lab_exam_request_form = LabExamRequestForm()
        search_form = SearchTreatmentHistoryForm()
        lab_results = LabResult.objects.filter(date=datetime.now().date(),treatment_delivered=False)

        treatment_form = TreatmentForm(initial={'treatment_id': lab_result.lab_exam_request.treated_animal})
            
        context = {'treated_animals_form':treated_animals_form,
                    'lab_exam_request_form':lab_exam_request_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset,
                    'lab_results':lab_results}

        return render(request, self.templateURL, context)
class TreatmentView(LoginRequiredMixin,View):
    login_url = "/"
    templateURL = 'regulartreatedanimals/regular.html'
    def post(self, request):
        treated_animals_form = TreatedAnimalsForm()
        treatment_form = TreatmentForm(request.POST)
        lab_exam_request_form = LabExamRequestForm()
        search_form = SearchTreatmentHistoryForm()
        lab_results = LabResult.objects.filter(date=datetime.now().date(),treatment_delivered=False)

        if treatment_form.is_valid():
            obj = treatment_form.save()
            rx_formset = PrescriptionFormSet(initial=[{'treatment': obj,"duration":2}])

            context = {'treated_animals_form':treated_animals_form,
                    'lab_exam_request_form':lab_exam_request_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset,
                    'lab_results':lab_results}

            return render(request, self.templateURL, context)

        else:
            context = {'treated_animals_form':treated_animals_form,
                    'lab_exam_request_form':lab_exam_request_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset,
                    'lab_results':lab_results}
            return render(request, self.templateURL, context)

class handlePrescription(LoginRequiredMixin, View):
    login_url = "/"
    def get(self,request):
        return redirect("/regular")

    def post(self, request):
        templateURL = 'regulartreatedanimals/regular.html'
        treated_animals_form = TreatedAnimalsForm(initial={'case_holder': request.user})
        treatment_form = TreatmentForm()
        rx_formset = PrescriptionFormSet()
        lab_exam_request_form = LabExamRequestForm()
        search_form = SearchTreatmentHistoryForm()
        lab_results = LabResult.objects.filter(date=datetime.now().date(),treatment_delivered=False)
        prescriptionFormSet = PrescriptionFormSet(data=request.POST)

        for form in prescriptionFormSet:
            if form.is_valid():
                print("VALID!!!")
                form.save()
            else:
                context = {'treated_animals_form':treated_animals_form,
                    'lab_exam_request_form':lab_exam_request_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset,
                    'lab_results':lab_results}

                return render(request, templateURL, context)
            
        return redirect("/regular")
 