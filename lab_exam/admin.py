from django.contrib import admin
from .models import LabExam,LabTechnique,LabSample
# Register your models here.
admin.site.register(LabExam)
admin.site.register(LabTechnique)
admin.site.register(LabSample)