from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# import default django user creation form
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class login(View):
    def get(self, request):
        form = UserCreationForm()

        context = {'form': form}

        return render(request, 'home/login.html', context)
