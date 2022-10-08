from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View

from vaccination.models import Vaccination
from .forms import VaccinationForm,SearchVaccinationHistoryForm

# Create your views here.
class Index(View):
    templateUrl = 'vaccination/vaccination.html'
    search_form = SearchVaccinationHistoryForm()
    def get(self, request):
        form = VaccinationForm(initial={'case_holder': request.user})
        return render(request, self.templateUrl, {'form': form,'search_form':self.search_form})
    
    def post(self, request):
        form = VaccinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vaccination/')

        return render(request, self.templateUrl, {'form': form})

class SearchVaccinationHistory(LoginRequiredMixin,View):
    login_url = "/"
    templateUrl = 'vaccination/vaccination.html'
    
    def get(self,request):
        return redirect("/vaccination/")

    def post(self,request):
        search_form = SearchVaccinationHistoryForm(request.POST)
        form = VaccinationForm(initial={'case_holder': request.user})

        if search_form.is_valid():
            case_number = search_form["case_number"].value()
            vaccination_history = Vaccination.objects.filter(case_number=case_number)
      
            context = {'vaccination_history': vaccination_history,
                        'search_form':search_form,
                        'form': form,
                        }

            return render(request, self.templateUrl, context)
        return redirect("/vaccination/")