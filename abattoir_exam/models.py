from django.db import models
from registernewuser.models import Species
# Create your models here.

SEX_CHOICES = [('Male', 'Male'), ('Female', 'Female')]


RESULT_CHOICES = [("Rejected","Rejected"),("Confirmed","Confirmed")]
class Color(models.Model):
    color = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.color

class Origin(models.Model):
    origin = models.CharField(max_length=100,null=False)

    def __str__(self) -> str:
        return self.origin

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100,null=False)
    hotel_code = models.IntegerField(primary_key=True,null=False)

    def __str__(self) -> str:
        return self.hotel_name

class AbattoirExam(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,null=False)
    species = models.ForeignKey(Species,on_delete=models.PROTECT,null=False)
    sex = models.CharField(max_length=10,choices=SEX_CHOICES,null=False)
    #########################################################
    origin = models.ForeignKey(Origin,on_delete=models.PROTECT,null=False)
    color = models.ForeignKey(Color,on_delete=models.PROTECT,null=False)
    body_weight = models.PositiveIntegerField(null=False)
    #########################################################
    t0 = models.DecimalField(verbose_name="T0", max_digits=5,
                             decimal_places=2,null=False)
    pr = models.DecimalField(verbose_name="PR", max_digits=5,
                             decimal_places=2,null=False)
    rr = models.DecimalField(verbose_name="RR", max_digits=5,
                             decimal_places=2,null=False)
    #########################################################
    date = models.DateField(auto_now=False,auto_now_add=True)
    result = models.CharField(max_length=100,choices=RESULT_CHOICES,null=False)

    def __str__(self) -> str:
        return self.hotel.hotel_name


