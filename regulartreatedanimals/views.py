from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import TreatedAnimalsForm, PrescriptionForm, PrescriptionFormSet

# Create your views here.


class index(View):

    def get(self, request):
        form = TreatedAnimalsForm()
        rx_formset = PrescriptionFormSet()

        context = {'form': form,
                   'rx_formset': rx_formset}
        return render(request, 'regulartreatedanimals/regular.html', context)

    def post(self, request):
        filledForm = TreatedAnimalsForm(request.POST)

        if filledForm.is_valid():
            filledForm.save()

            case_number = filledForm.cleaned_data.get("case_number")

            print(case_number.case_number)

            initial_CaseNumber = [{'treatment': case_number.case_number}]

            rx_formset = PrescriptionFormSet(initial=initial_CaseNumber)

            context = {'form': filledForm,
                       'rx_formset': rx_formset}

            return render(request, 'regulartreatedanimals/regular.html', context)
