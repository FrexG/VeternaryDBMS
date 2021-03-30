from django.db import models

# Import tables from registernewuser app
from registernewuser.models import Customer, Drug, Vaccine

# Model definition for regular treated animals app


class Unit(models.Model):
    unit_name = models.TextField("Unit Name", max_length=50)

    def __str__(self):
        return str(self.unit_name)


class TreatedAnimal(models.Model):
    case_number = models.ForeignKey(
        Customer, verbose_name="Case Number", on_delete=models.CASCADE)
    t0 = models.DecimalField(verbose_name="T0", max_digits=3,
                             decimal_places=2, blank=True)

    pr = models.DecimalField(verbose_name="PR", max_digits=3,
                             decimal_places=2, blank=True)

    rr = models.DecimalField(verbose_name="RR", max_digits=3,
                             decimal_places=2, blank=True)

    clinical_finding = models.TextField(
        verbose_name="Clinical Finding", max_length=200, blank=True)

    dx = models.TextField(verbose_name="DX", max_length=100)

    differential_diag = models.TextField(
        "Differential Diagnosis", max_length=100)

    rumen_motility = models.TextField("Rumen Motility", max_length=100)

    service_date = models.DateField(
        "Service Date", auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(f'{self.case_number}: { self.service_date }')


class Prescription(models.Model):
    # Prescrition for the corresponding treatment
    # A Treatment can have multiple prescription

    rx = models.ForeignKey(Drug, verbose_name="RX", on_delete=models.CASCADE)

    treatment = models.ForeignKey(
        TreatedAnimal, verbose_name="Treatment", on_delete=models.CASCADE)

    unit = models.ForeignKey(Unit, verbose_name="Unit",
                             on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField("Quantity")

    duration = models.PositiveIntegerField("Follow Up Duration")

    def __str__(self):
        return str(f'{self.rx} : {self.treatment}')
