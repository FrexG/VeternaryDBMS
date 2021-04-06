from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


class index(View):
    def get(self, request):
        return HttpResponse('<h2> Clinical Services Page </h2>')
