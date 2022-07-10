from django.contrib import admin

# Register your models here.
from .models import ParasiteTreatment,ParasitePrescription

admin.site.register(ParasiteTreatment)
admin.site.register(ParasitePrescription)
