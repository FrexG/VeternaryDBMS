from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
# import default django user creation form
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm,UserRoleForm
# Create your views here.


class Login(View):
    def get(self, request):
        return render(request, 'home/login.html')

    def post(self, request):
        # get username
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate user

        authenticated_user = authenticate(
            request, username=username, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user)

            if Profile.objects.get(user=authenticated_user).role == 'Vet':
                return redirect('/regular')
            elif Profile.objects.get(user=authenticated_user).role == 'Cashier':
                return redirect('/cashier')
            elif Profile.objects.get(user=authenticated_user).role == 'Pharmacist':
                return redirect('/pharmacy')
            elif Profile.objects.get(user=authenticated_user).role == 'Stock_Keeper':
                return redirect('/drug_in_out')
            elif Profile.objects.get(user=authenticated_user).role == 'Admin':
                return redirect('/dashboard')
            elif Profile.objects.get(user=authenticated_user).role == 'Lab':
                return redirect('/lab_exam')
            else:
               messages.info(request, "Incorrect Username or Password")
               return redirect('/') 
        else:
            messages.info(request, "Please enter your Username or Password")
            return redirect('/')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class Signup(View):
    def get(self, request):
        form = CreateUserForm()
        role_form = UserRoleForm()


        context = {'form': form,
                   'role_form': role_form}

        return render(request, 'home/signup.html', context)

    def post(self, request):
        form = CreateUserForm(request.POST)
        role_form = UserRoleForm(request.POST)

        # get role
        role = role_form['role'].value()

        context = {'form': form,
                   'role_form': role_form}

        if form.is_valid():
            obj = form.save()
            user = form.cleaned_data.get("username")
            # assign role to user
            Profile.objects.create(user=obj, role=role)
            messages.success(request, f"Account created for {user}")

            return redirect('/')

        return render(request, 'home/signup.html', context)
