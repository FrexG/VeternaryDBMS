from django.contrib import admin

# Register your models here.
from .models import ParasiteTreatment,Vaccination,ParasitePrescription

admin.site.register(ParasiteTreatment)
admin.site.register(Vaccination)
admin.site.register(ParasitePrescription)
