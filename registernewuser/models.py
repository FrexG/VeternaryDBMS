from django.db import models
from datetime import date
# Create your models here.

SEX_CHOICES = [('M', 'Male'), ('F', 'Female'), ]


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

    def getBreedName(self): return str(breed_name)


class Species(models.Model):
    species_type = models.CharField(max_length=100)

    def __str__(self):
        return self.species_type

    def getSpeciesName(self): return str(self.species_type)


class Vaccine(models.Model):
    vaccine_type = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6, decimal_places=4, default=000000.0000)

    def __str__(self):
        return self.vaccine_type

    def getVaccineName(self): return str(self.vaccine_type)


class Drug(models.Model):
    drug_type = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6, decimal_places=4, default=000000.0000)

    def __str__(self):
        return self.drug_type

    def getDrugName(self): return str(self.drug_type)


class Service(models.Model):

    service_type = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6, decimal_places=4, default=000000.0000)

    def __str__(self):
        return self.service_type

    def getServiceName(self): return str(self.service_type)


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    sub_kebele = models.CharField(max_length=100)
    kebele = models.ForeignKey(Kebele, on_delete=models.CASCADE)
    case_number = models.IntegerField(primary_key=True, null=False)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    number_of_animals = models.IntegerField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    service_date = models.DateField(auto_now=False, auto_now_add=True)
    treatment_history = models.TextField(max_length=500, null=True)
    mobile_number = models.IntegerField()

    def __str__(self):
        return f'{self.customer_name} : {str(self.case_number)}'

    def getCaseNumber(self): return case_number

    def getSex(self): return sex

    def getServiceDate(self): return service_date
