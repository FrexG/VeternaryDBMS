from statistics import mode
from django.db import models

# import drug and vaccine models
from registernewuser.models import Drug
from vaccination.models import Vaccine
# Create your models here.
# create a clinical equipment model
class ClinicalEquipment(models.Model):
    # create a field for the name of the clinical equipment
    name = models.CharField(max_length=100)
    # create a field for the description of the clinical equipment
    unit = models.CharField(max_length=100,default="PCS")
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.name)

# create a stock model for the clinical equipment
class ClinicalEquipmentStock(models.Model):
    # create a field for the type clinical equipment
    equipment = models.ForeignKey(ClinicalEquipment, on_delete=models.CASCADE)
    # create a field for the quantity of the clinical equipment
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.equipment.name}:{self.quantity}"

class DrugStock(models.Model):
    # create a field for the type drug
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    # create a field for the quantity of the drug
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.drug.drug_type}:{self.quantity}"

class VaccineStock(models.Model):
    # creata a field for the type of vaccine
    vaccine = models.ForeignKey(Vaccine,on_delete=models.CASCADE)
    # create a field for the quantity in stock for the vaccine 
    quantity = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.vaccine.vaccine_type}:{self.quantity}"
    
    