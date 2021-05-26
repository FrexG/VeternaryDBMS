from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
# import default django user creation form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

# Create your views here.


class login(View):
    def get(self, request):
        return render(request, 'home/login.html')

    def post(self, request):
        # get username
        username = request.POST.get('username')
        password = request.POST.get('password')

        return HttpResponse(f'<h1>{password}</h1>')


class signup(View):
    def get(self, request):
        form = CreateUserForm()

        context = {'form': form}

        return render(request, 'home/signup.html', context)

    def post(self, request):
        form = CreateUserForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {user}")

            return redirect('/')

        return render(request, 'home/signup.html', context)
