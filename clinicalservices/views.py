from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Import Models and Forms

from .forms import ClinicalServiceForm, ServiceProvidedForm, ServiceProvidedFormSet, AIServiceForm
# Clinical Service Home page


class index(View):
    templateURL = 'clinicalservices/index.html'

    ai_form = AIServiceForm()
    service_formset = ServiceProvidedFormSet()

    def get(self, request):
        form = ClinicalServiceForm()

        context = {'form': form,
                   'service_form': self.service_formset,
                   'ai_form': self.ai_form}

        return render(request, self.templateURL, context)

    def post(self, request):
        # Process ClinicalServiceForm
        serviceFormRequest = ClinicalServiceForm(request.POST)
        # Check if it is a valid
        if serviceFormRequest.is_valid():
            print("is valid!!")
            # save the form values to model
            service_form = serviceFormRequest.save()

            prefilled_service_type = ServiceProvidedFormSet(
                initial=[{'clinical_service': service_form}])

            context = {'form': serviceFormRequest,
                       'service_form': prefilled_service_type,
                       'ai_form': self.ai_form}

            return render(request, self.templateURL, context)
        else:
            context = {'form': serviceFormRequest,
                       'service_form': self.service_formset,
                       'ai_form': self.ai_form}
            return render(request, self.templateURL, context)
