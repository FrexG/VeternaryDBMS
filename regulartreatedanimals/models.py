from django.db import models
# Import tables from registernewuser app
from registernewuser.models import Customer, Drug, Vaccine

# Model definition for regular treated animals app


class Unit(models.Model):
    unit_name = models.CharField(max_length=100,null=False)
    def __str__(self) -> str:
        return str(self.unit_name)
class Disease(models.Model):
    disease_name = models.CharField(max_length=100,null=False)
    def __str__(self) -> str:
        return str(self.disease_name)
class TreatedAnimal(models.Model):
    case_number = models.ForeignKey(
        Customer, verbose_name="Case Number", on_delete=models.CASCADE)
    t0 = models.DecimalField(verbose_name="T0", max_digits=3,
                             decimal_places=2,)

    pr = models.DecimalField(verbose_name="PR", max_digits=3,
                             decimal_places=2)

    rr = models.DecimalField(verbose_name="RR", max_digits=3,
                             decimal_places=2)

    clinical_finding = models.TextField(
        verbose_name="Clinical Finding", max_length=200, blank=True)

    dx = models.ManyToManyField(Disease, verbose_name="Dx", blank=True)
    differential_diag = models.TextField(
        "Differential Diagnosis", max_length=100)

    rumen_motility = models.TextField("Rumen Motility", max_length=100)

    service_date = models.DateField(
        "Service Date", auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(f'{self.id} : {self.case_number}')

    def getTreatmentID(self):
        return self.id

    def getKebele(self):
        return self.case_number.kebele

class Prescription(models.Model):
    # Prescrition for the corresponding treatment
    # A Treatment can have multiple prescription
    
    rx = models.ForeignKey(Drug, verbose_name="RX", on_delete=models.CASCADE)

    treatment = models.ForeignKey(
        TreatedAnimal, verbose_name="Treatment ID", on_delete=models.CASCADE)

    unit = models.ForeignKey(Unit, verbose_name="Unit",
                             on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField("Quantity")

    duration = models.PositiveIntegerField("Follow Up Duration")

    total = models.DecimalField(
        max_digits=8, decimal_places=4, default=000000.0000)

    paid = models.BooleanField(null=False, default=False)

    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(f'{self.rx} : {self.treatment}')
