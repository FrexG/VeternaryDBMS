from operator import mod
from django.db import models
from registernewuser.models import Customer,Drug
from regulartreatedanimals.models import Disease
from django.contrib.auth.models import User
from registernewuser.models import Breed,Species

# Create your models here.
SEX_CHOICES = [('M', 'Male'), ('F', 'Female'),]
class ParasiteTreatment(models.Model):

    TREATMENT_OPTION = [("Internal","Internal Parasite"),("External","External Parasite")]

    treatment_type = models.CharField(max_length=100,choices=TREATMENT_OPTION,null=False)
    case_number = models.ForeignKey(Customer,on_delete=models.PROTECT,null=False)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    number_of_animals = models.PositiveIntegerField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    history = models.CharField(max_length=200,null=True)
    case_holder = models.ForeignKey(User,on_delete=models.PROTECT,null=False)
    dx = models.ManyToManyField(Disease,verbose_name="Dx",blank=True)
    service_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(f"{self.case_number.customer_name}:{self.treatment_type}")
        
    def getKebele(self):
        return self.case_number.kebele

    class Meta:
        verbose_name = "Parasite Treatment"

class ParasitePrescription(models.Model):
    # Prescrition for the corresponding parasite treatment
    # A Treatment can have multiple prescription
    
    rx = models.ForeignKey(Drug, verbose_name="RX", on_delete=models.CASCADE,null=False)

    treatment = models.ForeignKey(
        ParasiteTreatment, verbose_name="Treatment ID", on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField("Quantity",null=False)

    duration = models.PositiveIntegerField("Follow Up Duration",null=False)

    total = models.DecimalField(
        max_digits=8, decimal_places=2, default=000000.00)

    paid = models.BooleanField(null=False, default=False)
    
    delivered = models.BooleanField(null=False, default=False)
    
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(f'{self.rx} : {self.treatment}')

    def getRX(self):
        return self.rx.objects.all()

    def getPrice(self):
        return self.total