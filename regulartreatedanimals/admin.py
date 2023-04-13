from django.contrib import admin

from .models import TreatedAnimal, Prescription,Disease,Treatment

# Register your models here.

admin.site.register(TreatedAnimal)
admin.site.register(Treatment)
admin.site.register(Prescription)
admin.site.register(Disease)
