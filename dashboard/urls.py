from django.urls import path
from .views import *

app_name = "dashboard"
urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('dashboard_data/',DashboardData.as_view(),name="dashboard_data"),
    path('regular_treatment_summary/',RegularTreatmentSummary.as_view(),name="regular_treatment_summary"),
    path('clinical_service_summary/',ClinicalServiceSummary.as_view(),name="clinical_service_summary"),
    path('clinical_service_types/',ClinicalServiceTypes.as_view(),name="clinical_service_types"),
    path('parasite_treatment_summary/',ParasiteTreatmentSummary.as_view(),name="parasite_treatment_summary"),
    path('parasite_treatment_types/',ParasiteTreatmentTypes.as_view(),name="parasite_treatment_types"),
]
