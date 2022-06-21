from django.db import models
from registernewuser.models import Customer,Drug,Vaccine
from regulartreatedanimals.models import Unit
from django.contrib.auth.models import User

# Create your models here.
class ParasiteTreatment(models.Model):

    TREATMENT_OPTION = [("Internal","Internal Parasite"),("External","External Parasite")]

    treatment_type = models.CharField(max_length=100,choices=TREATMENT_OPTION)
    case_number = models.ForeignKey(Customer,on_delete=models.PROTECT)
    case_holder = models.ForeignKey(User,on_delete=models.PROTECT)
    dx = models.CharField(max_length=200,null=False)
    service_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(f"{self.case_number.customer_name}:{self.treatment_type}")

    class Meta:
        verbose_name = "Parasite Treatment"


class Vaccination(models.Model):
    case_number = models.ForeignKey(Customer,on_delete=models.PROTECT)
    vaccine_id = models.ForeignKey(Vaccine,on_delete=models.PROTECT)
    vaccine_batch_num = models.CharField(max_length=100,null=False)
    quantity = models.IntegerField(default=0,null=False)
    unit = models.ForeignKey(Unit,on_delete=models.PROTECT)
    dx = models.CharField(max_length=200,null=False)
    service_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.case_number.customer_name)
