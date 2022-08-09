from django.urls import path

from .views import Index, handlePrescription,SearchTreatmentHistory,LabRequestView

app_name = "regulartreatedanimals"

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('labrequest/', LabRequestView.as_view(), name="labrequest"),
    path('prescribe/', handlePrescription.as_view(),name="prescribe"),
    path('search_treatment_history/',SearchTreatmentHistory.as_view(),name="search_treatment_history"),
]
