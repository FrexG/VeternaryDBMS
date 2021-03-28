from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import NewCustomerForm

# Create your views here.


class index(View):
    def get(self, request):
        form = NewCustomerForm()
        context = {"form": form}
        return render(request, 'registernewuser/index.html', context)
