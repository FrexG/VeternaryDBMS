from django.contrib import admin
from .models import VaccineIn,VaccineOut,VaccineOutCashDeposit
# Register your models here.
admin.site.register(VaccineIn)
admin.site.register(VaccineOut)
admin.site.register(VaccineOutCashDeposit)