from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Import Models and Forms

from .forms import ClinicalServiceForm, ServiceProvidedForm, ServiceProvidedFormSet, AIServiceForm

# Create your views here.


class index(View):
    def get(self, request):
        form = ClinicalServiceForm()
        service_formset = ServiceProvidedFormSet()
        ai_form = AIServiceForm()

        context = {'form': form,
                   'service_form': service_formset,
                   'ai_form': ai_form}

        return render(request, 'clinicalservices/index.html', context)
