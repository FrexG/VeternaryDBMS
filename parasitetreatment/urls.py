from django.urls import path

from .views import index, handlePrescription

app_name = "parasitetreatment"
urlpatterns = [
    path('', index.as_view(), name="index"),
    path('prescribe', handlePrescription.as_view()),
]
