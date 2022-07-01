from django.urls import path

from .views import index, handlePrescription

app_name = "regulartreatedanimals"

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('prescribe/', handlePrescription.as_view(),name="prescribe"),
]
