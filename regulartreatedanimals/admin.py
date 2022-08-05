from django.contrib import admin

from .models import TreatedAnimal, Prescription,Disease

# Register your models here.

admin.site.register(TreatedAnimal)
admin.site.register(Prescription)
admin.site.register(Disease)
