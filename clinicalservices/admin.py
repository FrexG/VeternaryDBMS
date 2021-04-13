from django.contrib import admin

from .models import ClinicalService, AIService, ServiceProvided
# Register your models here.
admin.site.register(ClinicalService)
admin.site.register(AIService)
admin.site.register(ServiceProvided)
