from django.shortcuts import render, redirect
from django.views import View
from .forms import TreatedAnimalsForm,PrescriptionFormSet
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class index(LoginRequiredMixin, View):
    login_url = "/"

    templateURL = 'regulartreatedanimals/regular.html'
    rx_formset = PrescriptionFormSet()
    form = TreatedAnimalsForm()

    def get(self, request):  
        context = {'form': self.form,
                   'rx_formset': self.rx_formset}
        return render(request, self.templateURL, context)

    def post(self, request):
        filledForm = TreatedAnimalsForm(request.POST)

        if filledForm.is_valid():
            treatmentID = filledForm.save()

            initial_treatment = [{'treatment': treatmentID,"duration":10}]

            filled_rx_formset = PrescriptionFormSet(initial=initial_treatment)

            context = {'form': filledForm,
                       'rx_formset': filled_rx_formset}

            return render(request, self.templateURL, context)

        else:
            context = {'form': filledForm,
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
