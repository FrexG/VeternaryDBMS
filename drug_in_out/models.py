from django.db import models
# import users model
from django.contrib.auth.models import User
from registernewuser.models import Drug,Kebele

# Create your models here.

class DrugIn(models.Model):
    # source options
    SOURCE = [("Regular","Regular Fund"),
                ("Revolving","Revolving Fund"),
                ("Zone","Zone Support"),
                ("Regional","Regional Support"),
                ("NGO","Non-Govermental"),
                ("Other","Other")]

    drug = models.ForeignKey(Drug,on_delete=models.PROTECT)
    source = models.CharField(max_length=50,choices=SOURCE)
    receiver = models.ForeignKey(User,on_delete=models.PROTECT,related_name="receiver")
    dropped_by = models.CharField(max_length=100,null=True)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=8,decimal_places=2,default=000000.00)
    total = models.DecimalField(max_digits=8,decimal_places=2,default=000000.00)
    batch_number = models.CharField(max_length=100,null=False)
    date = models.DateField(auto_now=False,auto_now_add=True)
    expiration_data = models.DateField(auto_now=False,auto_now_add=False)
    remark = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.drug.getDrugName()+"_"+str(self.batch_number)
   

class DrugOut(models.Model):
    DESTINATION = [
        ("HP","Health Post"),
        ("ZR","Zone Reverse"),
        ("Emergency","Emergency"),
        ("Expired","Expired Drugs"),
        ("General","General Sale")
    ]
    drug = models.ForeignKey(Drug,on_delete=models.PROTECT)
    destination = models.CharField(max_length=50,choices=DESTINATION)
    receiver = models.ForeignKey(Kebele,on_delete=models.PROTECT)
    approved_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name="approved_by")
    store_man = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    #unit_price = models.DecimalField(max_digits=8,decimal_places=2,default=000000.00)
    total = models.DecimalField(max_digits=8,decimal_places=2,default=000000.00)
    batch_number = models.CharField(max_length=100,null=False)
    date = models.DateField(auto_now=False,auto_now_add=True)
    remark = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.drug.drug_type + "-" + self.receiver.name + "-" + self.batch_number


class DrugOutCashDeposit(models.Model):
    payment_for = models.ForeignKey(DrugOut,on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=8,decimal_places=2,default=000000.00)
    bank_slip_number = models.CharField(max_length=100,null=False)
    date_paid = models.DateField(auto_now=False,auto_now_add=True)
    remaining_amount = models.DecimalField(max_digits=8,decimal_places=2,default=000000.00)
    confirmed_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name="drug_out_confirmed_by")
    remark = models.CharField(max_length=200,null=True)



