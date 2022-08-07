from encodings import search_function
from django.shortcuts import render, redirect
from django.views import View
from .models import TreatedAnimal
from .forms import *
from lab_exam.forms import LabExamRequestForm
from django.contrib.auth.mixins import LoginRequiredMixin

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

        context = {'treated_animals_form':treated_animals_form,
                    'lab_exam_request_form':lab_exam_request_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset}

        return render(request, self.templateURL, context)

    def post(self, request):
        treated_animals_form = TreatedAnimalsForm(request.POST)
        rx_formset = PrescriptionFormSet()
        treatment_form = TreatmentForm()
        lab_exam_request_form = LabExamRequestForm()
        search_form = SearchTreatmentHistoryForm()

        if treated_animals_form.is_valid():
            treatmentID = treated_animals_form.save()

            treatment_form = TreatmentForm(initial={'treatment_id': treatmentID})
            lab_exam_request_form = LabExamRequestForm(initial={'treatment_animal': treatmentID})

            context = {'treated_animals_form':treated_animals_form,
                    'lab_exam_request_form':lab_exam_request_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset}

            return render(request, self.templateURL, context)

        else:
            context = {'treated_animals_form':treated_animals_form,
                    'treatment_form':treatment_form,
                    'search_form': search_form,
                    'rx_formset': rx_formset}
            return render(request, self.templateURL, context)

class handlePrescription(LoginRequiredMixin, View):
    login_url = "/"
    templateURL = 'regulartreatedanimals/regular.html'
    rx_formset = PrescriptionFormSet()
    form = TreatedAnimalsForm()
    search_form = SearchTreatmentHistoryForm()

    def get(self,request):
        return redirect("/regular")

    def post(self, request):
        prescriptionFormSet = PrescriptionFormSet(data=request.POST)

        for form in prescriptionFormSet:
            if form.is_valid():
                print("VALID!!!")
                form.save()
            else:
                context = {'search_form':self.search_form,
                            'form': self.form,
                        'rx_formset': prescriptionFormSet
                        } 
                return render(request, self.templateURL, context)
            
        return redirect("/regular")
        
class SearchTreatmentHistory(LoginRequiredMixin,View):
    login_url = "/"
    templateURL = 'regulartreatedanimals/regular.html'
    rx_formset = PrescriptionFormSet()
    form = TreatedAnimalsForm()
    search_form = SearchTreatmentHistoryForm()
    
    def get(self,request):
        return redirect("/regular")

    def post(self,request):
        search_form = SearchTreatmentHistoryForm(request.POST)
        if search_form.is_valid():
            case_number = search_form["case_number"].value()
            treatment_history = TreatedAnimal.objects.filter(case_number=case_number)
      
            context = {'treatment_history': treatment_history,
                        'search_form':self.search_form,
                        'form': self.form,
                        'rx_formset': self.rx_formset}

            return render(request, self.templateURL, context)
        return redirect("/regular")

