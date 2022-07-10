from encodings import search_function
from django.shortcuts import render, redirect
from django.views import View
from .models import TreatedAnimal
from .forms import TreatedAnimalsForm,PrescriptionFormSet,SearchTreatmentHistoryForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class index(LoginRequiredMixin, View):
    login_url = "/"

    templateURL = 'regulartreatedanimals/regular.html'
    rx_formset = PrescriptionFormSet()
    form = TreatedAnimalsForm()
    search_form = SearchTreatmentHistoryForm()

    def get(self, request):  
        context = {'search_form': self.search_form,
                    'form': self.form,
                   'rx_formset': self.rx_formset}

        return render(request, self.templateURL, context)

    def post(self, request):
        filledForm = TreatedAnimalsForm(request.POST)

        if filledForm.is_valid():
            treatmentID = filledForm.save()

            initial_treatment = [{'treatment': treatmentID,"duration":10}]

            filled_rx_formset = PrescriptionFormSet(initial=initial_treatment)

            context = {'search_form':self.search_form,
                        'form': filledForm,
                       'rx_formset': filled_rx_formset}

            return render(request, self.templateURL, context)

        else:
            context = {'search_form':self.search_form,
                        'form': filledForm,
                       'rx_formset': self.rx_formset}
            return render(request, self.templateURL, context)


class handlePrescription(LoginRequiredMixin, View):
    login_url = "/"

    def get(self,request):
        return redirect("/regular")

    def post(self, request):
        prescriptionFormSet = PrescriptionFormSet(data=request.POST)

        for formset in prescriptionFormSet:
            if formset.is_valid():
                formset.save()
                
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

