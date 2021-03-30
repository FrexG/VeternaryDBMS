from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import TreatedAnimalsForm

# Create your views here.


class index(View):

    def get(self, request):
        form = TreatedAnimalsForm()
        context = {'form': form}
        return render(request, 'regulartreatedanimals/regular.html', context)
