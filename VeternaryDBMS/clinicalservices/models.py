from django.db import models
from registernewuser.models import Customer
from django.contrib.auth.models import User
from registernewuser.models import Breed,Species
from abattoir_exam.models import Color

# MODEL DEFINITION FOR CLINICAL SERVICES
SEX_CHOICES = [('M', 'Male'), ('F', 'Female'),]

class Service(models.Model):
    service_type = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=000000.0000)

    def __str__(self):
        return self.service_type

    def getServiceName(self): return str(self.service_type)


class ClinicalService(models.Model):
    # Fields for ClinicalService table
    id = models.AutoField(primary_key=True)

    case_number = models.ForeignKey(
        Customer, verbose_name="Case Number", on_delete=models.CASCADE,null=False)
    # refernce to user id will be added later
    service_date = models.DateField(
        "Service Date", auto_now_add=True)

    # Service type
    service_type = models.ForeignKey(Service,on_delete=models.PROTECT,null=False)

    case_holder = models.ForeignKey(User,on_delete=models.PROTECT,null=True)

    paid = models.BooleanField(null=False,default=False)

    def __str__(self):
        return str(self.case_number)
    
    def getKebele(self):
        return self.case_number.kebele

# Artificial Insemination model


class AIService(models.Model):

    case_number = models.ForeignKey(
        Customer, verbose_name="Case Number", on_delete=models.CASCADE,null=False)
    # Service type, this will be prefield by service type = AI
    service_type = models.ForeignKey(Service,on_delete=models.PROTECT,null=False)

    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    number_of_animals = models.PositiveIntegerField()

    sex = models.CharField(max_length=10, choices=SEX_CHOICES)

    history = models.CharField(max_length=200,null=True)

    service_date = models.DateField(
        "Service Date", auto_now=False, auto_now_add=True)

    last_calving_date = models.DateField(verbose_name="Last Calving Date")

    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    
    ai_frequency = models.CharField(max_length=30)

    bull_number = models.PositiveIntegerField()

    pd_result = models.CharField(max_length=50)

    qnty = models.PositiveIntegerField()

    case_holder = models.ForeignKey(User,on_delete=models.PROTECT)

    total= models.DecimalField(
        max_digits=6, decimal_places=2, default=000000.00)

    paid = models.BooleanField(null=False,default=False)

    def __str__(self):
        return str(self.case_number)

    def getKebele(self):
        return self.case_number.kebele
        
    def getPrice(self):
        return self.total
