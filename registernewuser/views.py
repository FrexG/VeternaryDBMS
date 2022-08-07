from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import NewCustomerForm,SearchForm
from .models import Customer
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class index(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = NewCustomerForm()
        search_form = SearchForm()

        context = {
                    "form": form,
                    "search_form":search_form
                    }

        return render(request, 'registernewuser/index.html', context)

    def post(self, request):
        form = NewCustomerForm(request.POST)
        search_form = SearchForm()

        if form.is_valid():
            obj = form.save()
            messages.success(
                request, f"User:{form.cleaned_data.get('customer_name')} Case Num:{obj.pk}")

        context = {
                    "form": form,
                    "search_form":search_form
                    }
        return render(request, 'registernewuser/index.html', context)

# Search registered customer by mobile number or name
class SearchCustomer(LoginRequiredMixin,View):
    def post(self,request):
        form = NewCustomerForm()
        search_form = SearchForm(request.POST)
        # data
        customer_name = search_form['customer_name'].value()
        mobile_number = search_form['mobile_number'].value()
        print(customer_name,mobile_number)

        if search_form.is_valid():
            # find customer
            customer_by_name = Customer.objects.filter(customer_name=customer_name)
            customer_by_mobile = Customer.objects.filter(mobile_number=mobile_number)
            context = {
                    "form": form,
                    "search_form":search_form,
                    "customer_by_name":customer_by_name,
                    "customer_by_mobile":customer_by_mobile
                    }
        return render(request, 'registernewuser/index.html', context)

