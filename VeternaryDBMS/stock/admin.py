from django.contrib import admin
from .models import VaccineStock,DrugStock,ClinicalEquipment,ClinicalEquipmentStock
from import_export.admin import ExportActionMixin

# Register your models here.

class VaccineStockAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('vaccine','quantity')
    actions = ['export_as_csv']

admin.site.register(VaccineStock, VaccineStockAdmin)
admin.site.register(DrugStock)
admin.site.register(ClinicalEquipment)
admin.site.register(ClinicalEquipmentStock)
