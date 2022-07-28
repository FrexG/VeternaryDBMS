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
    path('vaccination_summary/',VaccinationSummary.as_view(),name="vaccination_summary"),
    path('vaccination_types/',VaccinationTypes.as_view(),name="vaccination_types"),
    path('artificial_insemination_summary/',ArtificialInseminationSummary.as_view(),name="artificial_insemination_summary"),
    path('drugin_summary/',DrugInSummary.as_view(),name="drug_in_summary"),
    path('drugout_summary/',DrugOutSummary.as_view(),name="drug_out_summary"),
    path('equipmentin_summary/',EquipmentInSummary.as_view(),name="equipment_in_summary"),
    path('equipmentout_summary/',EquipmentOutSummary.as_view(),name="equipment_out_summary"),
    path('vaccinein_summary/',VaccineInSummary.as_view(),name="vaccine_in_summary"),
    path('vaccineout_summary/',VaccineOutSummary.as_view(),name="vaccine_out_summary"),
]
