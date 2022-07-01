from django.contrib import admin

from .models import Unit, TreatedAnimal, Prescription,Disease

# Register your models here.

admin.site.register(Unit)
admin.site.register(TreatedAnimal)
admin.site.register(Prescription)
admin.site.register(Disease)
