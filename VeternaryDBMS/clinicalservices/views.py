import re
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Import Models and Form
from .forms import AIServiceForm,ClinicalServiceFormset

# Clinical Service Home page


class index(LoginRequiredMixin, View):
    login_url = "/"
    templateURL = 'clinicalservices/index.html'
    
    def get(self, request):
        form = ClinicalServiceFormset()
        ai_form = AIServiceForm(initial={'case_holder': request.user})
        context = {'form': form,
                   'ai_form': ai_form}

        return render(request, self.templateURL, context)

    def post(self, request):
        # Process ClinicalServiceForm
        serviceFormset = ClinicalServiceFormset(request.POST)
        # Set initial valuus for formset case_holder
         
        for formset in serviceFormset:
            if formset.is_valid():
                # save the form values to model
                service_form = formset.save(commit=False)
                # set the case_holder to the current user
                service_form.case_holder = request.user
                # save the form
                service_form.save()
            else:
                # return the form with errors
                context = {'form': serviceFormset,
                           'ai_form': self.ai_form}
                return render(request, self.templateURL, context)

        return redirect("/clinicalservice")
        

class AIServiceView(View):
    templateURL = 'clinicalservices/index.html'

    def get(self, request):
        form = ClinicalServiceFormset()
        ai_form = AIServiceForm(initial={'case_holder': request.user})
        context = {'form': form,
                   'ai_form': ai_form}

        return render(request, self.templateURL, context)

    def post(self, request):
        form = ClinicalServiceFormset()
        AIServiceFormRequest = AIServiceForm(request.POST)
        # Check for validity of form
        if AIServiceFormRequest.is_valid():
            print("Is valid called")
            # save model
            ai_form = AIServiceFormRequest.save(commit=False)
            ai_form.case_holder = request.user
            ai_form.save()
            return redirect("/clinicalservice")
        else:
            context = {'form':form,
                   'ai_form': AIServiceFormRequest}
            return render(request, self.templateURL, context)

        