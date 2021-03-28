from django.contrib import admin

# Import Models
from .models import Breed, Service, Kebele, Species, Vaccine

# Register your models here.
admin.site.register(Breed)
admin.site.register(Service)
admin.site.register(Kebele)
admin.site.register(Species)
admin.site.register(Vaccine)
