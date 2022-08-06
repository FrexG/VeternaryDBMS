from django.db import models
from registernewuser.models import Customer
from django.contrib.auth.models import User
# Create your models here.

class LabSample(models.Model):
    lab_sample = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.lab_sample

class LabTechnique(models.Model):
    lab_technique = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.lab_technique

class LabExam(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    lab_sample = models.ForeignKey(LabSample,on_delete=models.CASCADE)
    lab_technique = models.ForeignKey(LabTechnique,on_delete=models.CASCADE)
    lab_result = models.CharField(max_length=100,null=False)
    paid = models.BooleanField(default=False)
    case_holder = models.ForeignKey(User,on_delete=models.PROTECT,null=False)
    date = models.DateField(auto_now=False,auto_now_add=True)
