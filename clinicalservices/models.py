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


class ServiceProvided(models.Model):
    # Services Table
    service_type = models.ForeignKey(
        Service, verbose_name="Service Type", on_delete=models.CASCADE)
    # Many to One r/n ship with ClinicalService Table
    clinical_service = models.ForeignKey(
        ClinicalService, verbose_name="Service ID", on_delete=models.CASCADE)

    # Quantity of Services
    quantity = models.PositiveIntegerField("Quantity")
