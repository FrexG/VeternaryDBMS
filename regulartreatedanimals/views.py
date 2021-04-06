from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import TreatedAnimalsForm, PrescriptionForm, PrescriptionFormSet

# Create your views here.


class index(View):
    rx_formset = PrescriptionFormSet()

    def get(self, request):
        form = TreatedAnimalsForm()

        context = {'form': form,
                   'rx_formset': self.rx_formset}
        return render(request, 'regulartreatedanimals/regular.html', context)

    def post(self, request):
        filledForm = TreatedAnimalsForm(request.POST)

        if filledForm.is_valid():
            treatmentID = filledForm.save()

            initial_treatment = [{'treatment': treatmentID}]

            filled_rx_formset = PrescriptionFormSet(initial=initial_treatment)

            context = {'form': filledForm,
                       'rx_formset': filled_rx_formset}

            return render(request, 'regulartreatedanimals/regular.html', context)

        else:
            context = {'form': filledForm,
                       'rx_formset': self.rx_formset}
            return render(request, 'regulartreatedanimals/regular.html', context)


class handlePrescription(View):

    def get(self, request):
        return redirect("/regular")

    def post(self, request):
        print("Here")

        prescriptionFormSet = PrescriptionFormSet(data=request.POST)

        for formset in prescriptionFormSet:
            if formset.is_valid():
                formset.save()
                print("Valid")

        return redirect("/regular")
