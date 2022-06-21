from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import NewCustomerForm

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class index(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = NewCustomerForm()
        context = {"form": form}
        return render(request, 'registernewuser/index.html', context)

    def post(self, request):
        form = NewCustomerForm(request.POST)

        if form.is_valid():
            obj = form.save()
            messages.success(
                request, f"User:{form.cleaned_data.get('customer_name')} Case Num:{obj.pk}")

        context = {"form": form}
        return render(request, 'registernewuser/index.html', context)
