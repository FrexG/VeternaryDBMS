from django.shortcuts import render
from .forms import LabExamRequestForm
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Index(LoginRequiredMixin,View):
    login_url = "/"
    templateURL = "lab_exam/index.html"

    def get(self,request):
        form = LabExamRequestForm(initial={'case_holder': request.user})
        context = {
            'form':form
        }
        return render(request,self.templateURL,context=context)

    def post(self,request):
        form = LabExamRequestForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {
            'form':form
                 }
            return render(request,self.templateURL,context=context)

        return redirect("lab_exam:index")
       