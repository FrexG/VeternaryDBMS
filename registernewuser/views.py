from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import NewCustomerForm

# Create your views here.


class index(CreateView):
    def get(self, request):
        form = NewCustomerForm()
        context = {"form": form}
        return render(request, 'registernewuser/index.html', context)
