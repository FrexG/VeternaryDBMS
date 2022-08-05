from django.urls import path

from .views import *

app_name = "pharmacy"

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('update_prescription/<int:pk>/',DeliverPrescription.as_view(),name="deliver_prescription"),
    path('cancel_prescription/<int:pk>/',CancelPrescription.as_view(),name="cancel_prescription"),

    path('update_parasite_prescription/<int:pk>/',DeliverParasitePrescription.as_view(),name="deliver_parasite_prescription"),
    path('cancel_parasite_prescription/<int:pk>/',CancelParasitePrescription.as_view(),name="cancel_parasite_prescription"),
]
