from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AbattoirExam
from .forms import AbattoirExamForm
from utils.printout import abattoir_printout
# Create your views here.
class Index(View):
    login_url = "/"
    templateUrl = "abattoir_exam/index.html"

    def get(self,request):
        form = AbattoirExamForm()
        context = {
            'form':form
        }
        return render(request,self.templateUrl,context=context)

    def post(self,request):
        form = AbattoirExamForm(request.POST)
        if form.is_valid():
            obj = form.save()
            printout_fields = {
                'hotel':obj.hotel.hotel_name,
                'hotel_code':obj.hotel.hotel_code,
                'species':obj.species.species_type,
                'sex':obj.sex,
                'origin':obj.origin.origin,
                'color':obj.color.color,
                'weight':obj.body_weight,
                't0':obj.t0,
                'pr':obj.pr,
                'rr':obj.rr,
                'result':obj.result,
                'date':obj.date,
            }
            return abattoir_printout(request,printout_fields)

