from django.contrib import admin
from .models import ReceiptIn,ReceiptOut,Receipt
# Register your models here.

admin.site.register(Receipt)
admin.site.register(ReceiptIn)
admin.site.register(ReceiptOut)