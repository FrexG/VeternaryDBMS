from django.shortcuts import render,redirect
from .forms import LabResult
from .models import LabExamRequest
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Index(LoginRequiredMixin,View):
    login_url = "/"
    templateURL = "lab_exam/index.html"

    def get(self,request):
        lab_requests = LabExamRequest.objects.filter(paid=True,lab_result_arrived=False)
        print(lab_requests)
        context = {
            'lab_requests':lab_requests
        }
        return render(request,self.templateURL,context=context)

    def post(self,request,pk):
        lab_request = LabExamRequest.objects.get(id=pk)
        lab_request.lab_result_arrived = True
        lab_request.save()

        lab_requests = LabExamRequest.objects.filter(paid=True,lab_result_arrived=False)
        form = LabResult(initial={'lab_exam_request':lab_request,'case_holder':request.user})

        context = {
            'lab_requests':lab_requests,
            'form':form
        }
        return render(request,self.templateURL,context=context)
       
class SubmitLabResults(LoginRequiredMixin,View):
    login_url = "/"
    templateURL = "lab_exam/index.html"

    def post(self,request):
        form = LabResult(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lab_exam/')
        else:
            return redirect('/lab_exam/')