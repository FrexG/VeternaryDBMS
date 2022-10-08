from django.db import models
from regulartreatedanimals.models import TreatedAnimal
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

class LabExamRequest(models.Model):
    treated_animal = models.ForeignKey(TreatedAnimal,on_delete=models.CASCADE)
    lab_sample = models.ForeignKey(LabSample,on_delete=models.CASCADE)
    lab_technique = models.ForeignKey(LabTechnique,on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    lab_result_arrived = models.BooleanField(default=False)

class LabResult(models.Model):
    lab_exam_request = models.ForeignKey(LabExamRequest,on_delete=models.CASCADE)
    lab_result = models.CharField(max_length=100)
    case_holder = models.ForeignKey(User,on_delete=models.PROTECT,null=False)
    treatment_delivered = models.BooleanField(default=False)
    date = models.DateField(auto_now=False,auto_now_add=True)
    def __str__(self) -> str:
        return self.lab_result