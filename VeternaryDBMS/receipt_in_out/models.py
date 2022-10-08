from django.db import models
from registernewuser.models import Kebele
# Create your models here.

UNIT_CHOICE = [('Pad','Pad')]

class Receipt(models.Model):
    receipt_type = models.CharField(max_length=100)

    def __str__(self):
        return self.receipt_type

class ReceiptIn(models.Model):
    receipt_type = models.ForeignKey(Receipt,on_delete=models.CASCADE)
    deliverer_name = models.CharField(max_length=100)
    kebele = models.ForeignKey(Kebele,on_delete=models.CASCADE)
    unit = models.CharField(max_length=100,choices=UNIT_CHOICE,default="Pad")
    quantity = models.IntegerField(default=1)
    serial_num_init = models.CharField(max_length=100)
    serial_num_last = models.CharField(max_length=100)
    date = models.DateField(auto_now=False,auto_now_add=True)

class ReceiptOut(models.Model):
    receipt_type = models.ForeignKey(Receipt,on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=100)
    kebele = models.ForeignKey(Kebele,on_delete=models.CASCADE)
    unit = models.CharField(max_length=100,choices=UNIT_CHOICE,default="Pad")
    quantity = models.IntegerField(default=1)
    serial_num_init = models.CharField(max_length=100)
    serial_num_last = models.CharField(max_length=100)
    date = models.DateField(auto_now=False,auto_now_add=True)