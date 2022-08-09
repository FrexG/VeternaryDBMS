from django.urls import path

from .views import Index, handlePrescription,SearchTreatmentHistory,LabRequestView,LabResultView

app_name = "regulartreatedanimals"

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('labrequest/', LabRequestView.as_view(), name="labrequest"),
    path('prescribe/', handlePrescription.as_view(),name="prescribe"),
    path('lab_result/<int:pk>/', LabResultView.as_view(), name="lab_result"),
    path('search_treatment_history/',SearchTreatmentHistory.as_view(),name="search_treatment_history"),
]
