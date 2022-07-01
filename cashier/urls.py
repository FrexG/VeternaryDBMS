from django.urls import path

from .views import *

app_name = "cashier"

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('update_service/<int:pk>/',UpdateService.as_view(),name="update_service"),
    path('delete_service/<int:pk>/',DeleteService.as_view(),name="delete_service"),

    path('update_prescription/<int:pk>/',UpdatePrescription.as_view(),name="update_prescription"),
    path('delete_prescription/<int:pk>/',DeletePrescription.as_view(),name="delete_prescription"),

    path('update_parasite_prescription/<int:pk>/',UpdateParasitePrescription.as_view(),name="update_parasite_prescription"),
    path('delete_parasite_prescription/<int:pk>/',DeleteParasitePrescription.as_view(),name="delete_parasite_prescription"),
]
