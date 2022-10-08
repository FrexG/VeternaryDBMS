from django.db import models

from datetime import date
# Create your models here.

class Kebele(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def getKebeleName(self): return str(self.name)


class Breed(models.Model):
    breed_name = models.CharField(max_length=100)

    def __str__(self):
        return self.breed_name

    def getBreedName(self): return str(self.breed_name)


class Species(models.Model):
    species_type = models.CharField(max_length=100)

    def __str__(self):
        return self.species_type

    def getSpeciesName(self): return str(self.species_type)

class Drug(models.Model):
    drug_type = models.CharField(max_length=100)
    stock_price = models.DecimalField(
        max_digits=8, decimal_places=2, default=000000.00)
        
    dis_price = models.DecimalField(
        max_digits=8, decimal_places=2, default=000000.00)

    dis_unit = models.CharField(max_length=50,default="ML")

    stock_unit = models.CharField(max_length=50,default="BOX")

    def __str__(self):
        return self.drug_type

    def getDrugName(self): return str(self.drug_type)


class Customer(models.Model):
    case_number = models.AutoField(primary_key=True, null=False)
    customer_name = models.CharField(max_length=100)
    sub_kebele = models.CharField(max_length=100)
    kebele = models.ForeignKey(Kebele, on_delete=models.CASCADE)

    #species = models.ForeignKey(Species, on_delete=models.CASCADE)

    #breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    #number_of_animals = models.PositiveIntegerField()

    #sex = models.CharField(max_length=10, choices=SEX_CHOICES)

    #history = models.CharField(max_length=200,null=True)

    service_date = models.DateField(auto_now=False, auto_now_add=True)
    # make mobile number unique
    mobile_number = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(f"{self.customer_name}({self.case_number})")

    def getServiceDate(self): return self.service_date

