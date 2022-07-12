from django.contrib import admin
from .models import VaccineIn,VaccineOut
# Register your models here.
admin.site.register(VaccineIn)
admin.site.register(VaccineOut)