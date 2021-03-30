from django.contrib import admin

from .models import Unit, TreatedAnimal, Prescription

# Register your models here.

admin.site.register(Unit)
admin.site.register(TreatedAnimal)
admin.site.register(Prescription)
