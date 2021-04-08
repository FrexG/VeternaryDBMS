from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import ClinicalServiceForm, ServiceProvidedForm

# Create your views here.


class index(View):
    def get(self, request):
        form = ClinicalServiceForm()
        service_form = ServiceProvidedForm()

        context = {'form': form,
                   'service_form': service_form}

        return render(request, 'clinicalservices/index.html', context)
