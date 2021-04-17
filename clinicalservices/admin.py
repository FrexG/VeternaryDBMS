from django.contrib import admin

from .models import ClinicalService, Service, AIService, ServiceProvided
# Register your models here.
admin.site.register(Service)
admin.site.register(ClinicalService)
admin.site.register(AIService)
admin.site.register(ServiceProvided)
