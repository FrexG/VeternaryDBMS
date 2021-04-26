from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# import default django user creation form
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.


class login(View):
    def get(self, request):
        return HttpResponse("<h1>Login</h1")


class signup(View):
    def get(self, request):
        form = CreateUserForm()

        context = {'form': form}

        return render(request, 'home/signup.html', context)
