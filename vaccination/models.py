from django.db import models
from registernewuser.models import Customer
from regulartreatedanimals.models import Unit,Disease
from django.contrib.auth.models import User

# Create your models here.
class Vaccine(models.Model):
    vaccine_type = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6, decimal_places=4, default=000000.0000)

    def __str__(self):
        return self.vaccine_type

    def getVaccineName(self): return str(self.vaccine_type)
    def getPrice(self):return self.price

class Vaccination(models.Model):
    case_number = models.ForeignKey(Customer,on_delete=models.PROTECT)
    vaccine_id = models.ManyToManyField(Vaccine)
    vaccine_batch_num = models.CharField(max_length=100,null=False)
    quantity = models.IntegerField(default=0,null=False)
    unit = models.ForeignKey(Unit,on_delete=models.PROTECT)
    dx = models.ManyToManyField(Disease,verbose_name="Dx",blank=True)
    service_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.case_number.customer_name)

    def getKebele(self):
        return self.case_number.kebele