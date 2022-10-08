from django.contrib import admin
from .models import LabExamRequest,LabResult,LabTechnique,LabSample
# Register your models here.
admin.site.register(LabExamRequest)
admin.site.register(LabTechnique)
admin.site.register(LabSample)
admin.site.register(LabResult)