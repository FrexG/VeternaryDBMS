from django.contrib import admin
from .models import VaccineStock,DrugStock,ClinicalEquipment,ClinicalEquipmentStock
# Register your models here.
admin.site.register(VaccineStock)
admin.site.register(DrugStock)
admin.site.register(ClinicalEquipment)
admin.site.register(ClinicalEquipmentStock)
