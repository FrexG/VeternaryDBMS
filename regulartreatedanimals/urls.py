from django.urls import path

from .views import index, handlePrescription,SearchTreatmentHistory

app_name = "regulartreatedanimals"

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('prescribe/', handlePrescription.as_view(),name="prescribe"),
    path('search_treatment_history/',SearchTreatmentHistory.as_view(),name="search_treatment_history"),
]
