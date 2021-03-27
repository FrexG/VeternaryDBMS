from django.db import models

# Create your models here.


class Kebele(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return name


class Breed(models.Model):
    breed_name = models.CharField(max_length=100)

    def __str__(self):
        return breed_name


class Species(models.Model):
    species_type = models.CharField(max_length=100)

    def __str__(self):
        return self.species_type


class Vaccine(models.Model):
    vaccine_type = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6, decimal_places=4, default=000000.0000)

    def __str__(self):
        return self.vaccine_type


class Service(models.Model):
    service_type = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6, decimal_places=4, default=000000.0000)

    def __str__(self):
        return self.service_type


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    sub_kebele = models.CharField(max_length=100)
    kebele_id = models.ForeignKey(Kebele, on_delete=models.CASCADE)
    case_number = models.IntegerField(primary_key=True, null=False)
    species_id = models.ForeignKey(Species, on_delete=models.CASCADE)
    breed_id = models.ForeignKey(Breed, on_delete=models.CASCADE)
    number_of_animals = models.IntegerField()
    sex = models.CharField(max_length=2)
    service_data = models.DateField(auto_now=False, auto_now_add=True)
    treatment_history = models.CharField(max_length=250, null=True)
    mobile_number = models.IntegerField()

    def __str__(self):
        return f'{self.customer_name} : {str(self.case_number)}'
