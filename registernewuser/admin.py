from django.contrib import admin

# Import Models
from .models import Breed, Kebele, Species,Drug, Customer

# Register your models here.
admin.site.register(Breed)
admin.site.register(Kebele)
admin.site.register(Species)
admin.site.register(Drug)
admin.site.register(Customer)
