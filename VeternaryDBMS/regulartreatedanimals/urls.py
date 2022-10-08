from django.urls import path

from .views import Index, handlePrescription,LabRequestView,LabResultView,TreatmentView

app_name = "regulartreatedanimals"

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('labrequest/', LabRequestView.as_view(), name="labrequest"),
    path('prescribe/', handlePrescription.as_view(),name="prescribe"),
    path('lab_result/<int:pk>/', LabResultView.as_view(), name="lab_result"),
    path('treatment/', TreatmentView.as_view(), name="treatment"),
]
