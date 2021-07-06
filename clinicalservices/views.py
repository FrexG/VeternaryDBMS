from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Import Models and Form
from .forms import ClinicalServiceForm, AIServiceForm

# Clinical Service Home page


class index(LoginRequiredMixin, View):
    login_url = "/"
    templateURL = 'clinicalservices/index.html'
    ai_form = AIServiceForm()

    def get(self, request):
        form = ClinicalServiceForm()

        context = {'form': form,
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

            context = {'form': serviceFormRequest,
                       'ai_form': self.ai_form}

            return render(request, self.templateURL, context)
        else:
            context = {'form': serviceFormRequest,
                       'ai_form': self.ai_form}
            return render(request, self.templateURL, context)


class AIServiceView(View):

    templateURL = 'clinicalservices/index.html'

    form = ClinicalServiceForm()
    ai_form = AIServiceForm()

    def get(self, request):
        context = {'form': self.form,
                   'ai_form': self.ai_form}

        return render(request, self.templateURL, context)

    def post(self, request):
        AIServiceFormRequest = AIServiceForm(data=request.POST)
        # Check for validity of form
        print("Called")
        if AIServiceFormRequest.is_valid():
            print("Is valid called")
            # save model
            AIServiceFormRequest.save()
            AIServiceFormRequest = AIServiceForm()

        context = {'form': self.form,
                   'ai_form': AIServiceFormRequest}

        return render(request, self.templateURL, context)
