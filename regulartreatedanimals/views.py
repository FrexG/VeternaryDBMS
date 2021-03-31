from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import TreatedAnimalsForm, PrescriptionForm

# Create your views here.


class index(View):

    def get(self, request):
        form = TreatedAnimalsForm()
        rx = PrescriptionForm()

        context = {'form': form,
                   'rx': rx}
        return render(request, 'regulartreatedanimals/regular.html', context)
