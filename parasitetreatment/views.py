from django.shortcuts import render, redirect
from django.views import View
from .forms import ParasiteTreatmentForm
from .forms import PrescriptionFormSet

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class index(LoginRequiredMixin, View):
    login_url = "/"

    templateURL = 'parasitetreatment/treatment.html'
    rx_formset = PrescriptionFormSet()

    def get(self, request):
        form = ParasiteTreatmentForm(initial={'case_holder': request.user})

        context = {'form': form,
                   'rx_formset': self.rx_formset}
        return render(request, self.templateURL, context)

    def post(self, request):
        filledForm = ParasiteTreatmentForm(request.POST)

        if filledForm.is_valid():
            treatmentID = filledForm.save()

            initial_treatment = [{'treatment': treatmentID,"duration":1}]

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

    def get(self, request):
        return redirect("/parasitetreatment")

    def post(self, request):

        prescriptionFormSet = PrescriptionFormSet(data=request.POST)

        for formset in prescriptionFormSet:
            if formset.is_valid():
                print("It is valid")
                formset.save()

        return redirect("/parasitetreatment")
