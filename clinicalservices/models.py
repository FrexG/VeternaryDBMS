from django.db import models

from registernewuser.models import Customer, Service

# MODEL DEFINITION FOR CLINICAL SERVICES


class ClinicalService(models.Model):
    # Fields for ClinicalService table
    case_number = models.ForeignKey(
        Customer, verbose_name="Case Number", on_delete=models.CASCADE)
    # refernce to user id will be added later
    service_date = models.DateField(
        "Service Date", auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.case_number)

# Artificial Insemination model


class AIService(models.Model):

    case_number = models.ForeignKey(
        Customer, verbose_name="Case Number", on_delete=models.CASCADE)
    # Service type, this will be prefield by service type = AI
    service_type = models.ForeignKey(
        Service, verbose_name="Service Type", on_delete=models.CASCADE)

    service_date = models.DateField(
        "Service Date", auto_now=False, auto_now_add=True)

    last_calving_date = models.DateField(verbose_name="Last Calving Date")

    color = models.CharField(verbose_name="Color", max_length=20)

    ai_frequency = models.CharField(verbose_name="AI Frequency", max_length=30)

    bull_number = models.PositiveBigIntegerField(verbose_name="Bull Number")

    pd_result = models.CharField(verbose_name="PD Result", max_length=50)

    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    # Quantity of Services
    quantity = models.PositiveIntegerField("Quantity")

    def __str__(self):
        return str(self.case_number)


class ServiceProvided(models.Model):
    # Services Table
    service_type = models.ForeignKey(
        Service, verbose_name="Service Type", on_delete=models.CASCADE)
    # Many to One r/n ship with ClinicalService Table
    clinical_service = models.ForeignKey(
        ClinicalService, verbose_name="Service ID", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.service_type)
