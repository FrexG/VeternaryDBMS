import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Import Models and Form
from .forms import ClinicalServiceForm, AIServiceForm,ClinicalServiceFormset

# Clinical Service Home page


class index(LoginRequiredMixin, View):
    login_url = "/"
    templateURL = 'clinicalservices/index.html'
    ai_form = AIServiceForm()
    form = ClinicalServiceFormset()

    def get(self, request):
        context = {'form': self.form,
                   'ai_form': self.ai_form}

        return render(request, self.templateURL, context)

    def post(self, request):
        # Process ClinicalServiceForm
        serviceFormset = ClinicalServiceFormset(request.POST)
        # Check if it is a valid
        if serviceFormset.is_valid():
            # Save the data
            serviceFormset.save()
            # Redirect to the index page
            return redirect('/clinicalservice')
        # If not valid, return the form with errors
        context = {'form': serviceFormset,
                   'ai_form': self.ai_form}
        return render(request, self.templateURL, context)
        """
        for formset in serviceFormset:
            if formset.is_valid():
                # save the form values to model
                service_form = formset.save()
            else:
                # return the form with errors
                context = {'form': serviceFormset,
                           'ai_form': self.ai_form}
                return render(request, self.templateURL, context)

        return redirect("/clinicalservice")
        """
        

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
