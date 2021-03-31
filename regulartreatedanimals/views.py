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
