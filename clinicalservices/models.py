from django.db import models
from registernewuser.models import Customer
from django.contrib.auth.models import User

# MODEL DEFINITION FOR CLINICAL SERVICES


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
        Customer, verbose_name="Case Number", on_delete=models.CASCADE)
    # refernce to user id will be added later
    service_date = models.DateField(
        "Service Date", auto_now_add=True)

    # Service type
    service_type = models.ForeignKey(Service,on_delete=models.PROTECT)

    case_holder = models.ForeignKey(User,on_delete=models.PROTECT,null=True)

    paid = models.BooleanField(null=False,default=False)

    def __str__(self):
        return str(self.case_number)
    
    def getKebele(self):
        return self.case_number.kebele

# Artificial Insemination model


class AIService(models.Model):

    case_number = models.ForeignKey(
        Customer, verbose_name="Case Number", on_delete=models.CASCADE)
    # Service type, this will be prefield by service type = AI
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=10.0000)
        
    total= models.DecimalField(
        max_digits=6, decimal_places=2, default=10.0000)

    service_date = models.DateField(
        "Service Date", auto_now=False, auto_now_add=True)

    last_calving_date = models.DateField(verbose_name="Last Calving Date")

    color = models.CharField(max_length=20)

    ai_frequency = models.CharField(max_length=30)

    bull_number = models.PositiveBigIntegerField()

    pd_result = models.CharField(max_length=50)

    qnty = models.IntegerField()

    case_holder = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return str(self.case_number)

    def getKebele(self):
        return self.case_number.kebele
        
    def getPrice(self):
        return self.price
