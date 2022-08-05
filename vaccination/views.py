from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .forms import VaccinationForm

# Create your views here.
class Index(View):
    templateUrl = 'vaccination/vaccination.html'
    def get(self, request):
        form = VaccinationForm()
        return render(request, self.templateUrl, {'form': form})
    
    def post(self, request):
        form = VaccinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vaccination/')

        return render(request, self.templateUrl, {'form': form})