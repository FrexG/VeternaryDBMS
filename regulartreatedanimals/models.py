from django.db import models
# Import tables from registernewuser app
from registernewuser.models import Customer,Drug,Breed,Species
from django.contrib.auth.models import User

# Model definition for regular treated animals app
SEX_CHOICES = [('M', 'Male'), ('F', 'Female'), ]

class Disease(models.Model):
    disease_name = models.CharField(max_length=100,null=False)
    def __str__(self) -> str:
        return str(self.disease_name)
        
class TreatedAnimal(models.Model):
    case_number = models.ForeignKey(
        Customer, verbose_name="Case Number", on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    number_of_animals = models.PositiveIntegerField()

    sex = models.CharField(max_length=10, choices=SEX_CHOICES)

    history = models.CharField(max_length=200,null=True)

    case_holder = models.ForeignKey(User,on_delete=models.PROTECT,null=False)

    service_date = models.DateField("Service Date", auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(f'Treatment for->{self.case_number}')

    def getTreatmentID(self):
        return self.id

    def getKebele(self):
        return self.case_number.kebele

class Treatment(models.Model):
    # Treatment for a treated animal
    treatment_id = models.ForeignKey(TreatedAnimal, on_delete=models.CASCADE)
  
    t0 = models.DecimalField(verbose_name="T0", max_digits=5,
                             decimal_places=2,)

    pr = models.DecimalField(verbose_name="PR", max_digits=5,
                             decimal_places=2)

    rr = models.DecimalField(verbose_name="RR", max_digits=5,
                             decimal_places=2)

    clinical_finding = models.TextField(
        verbose_name="Clinical Finding", max_length=200, blank=True)

    dx = models.ManyToManyField(Disease, verbose_name="Dx", blank=True)

    differential_diag = models.TextField(max_length=200, blank=True)

    rumen_motility = models.TextField("Rumen Motility", max_length=100)

class Prescription(models.Model):
    """ Prescrition for the corresponding treatment,
        a treatment can have multiple prescription """
    treatment = models.ForeignKey(
        Treatment, verbose_name="Treatment ID", on_delete=models.CASCADE,null=False)

    rx = models.ForeignKey(Drug, verbose_name="RX", on_delete=models.CASCADE,null=False)

    quantity = models.PositiveIntegerField("Quantity",null=False)

    duration = models.PositiveIntegerField("Follow Up Duration",null=False)

    total = models.DecimalField(
        max_digits=8, decimal_places=2, default=000000.00)

    paid = models.BooleanField(default=False)

    delivered = models.BooleanField(default=False)
    
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(f'{self.rx} : {self.treatment}')
