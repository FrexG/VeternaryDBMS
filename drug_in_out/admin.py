from django.contrib import admin
from .models import DrugIn,DrugOut,DrugOutCashDeposit
# Register your models here.
admin.site.register(DrugIn)
admin.site.register(DrugOut)
admin.site.register(DrugOutCashDeposit)