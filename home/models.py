from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# profile model
# for specifying Role of each user

USER_ROLES = [('Admin', 'Adminstrator'),
              ('Cashier', 'Cashier'), 
              ('Vet', 'Veternarian'),
              ('Pharmacist', 'Pharmacist'),
              ('Stock_Keeper', 'Stock Keeper')]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(choices=USER_ROLES, max_length=100)

    def __str__(self):
        return f"{self.user}:{self.role}"
