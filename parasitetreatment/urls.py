from django.urls import path

from .views import index, handlePrescription,SearchParasiteTreatmentHistory

app_name = "parasitetreatment"
urlpatterns = [
    path('', index.as_view(), name="index"),
    path('prescribe', handlePrescription.as_view()),
    path('search_treatment_history',SearchParasiteTreatmentHistory.as_view(),name="search_treatment_history"),
]
