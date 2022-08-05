from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','password1', 'password2']

class UserRoleForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role']
        widgets = {'role': forms.Select()}