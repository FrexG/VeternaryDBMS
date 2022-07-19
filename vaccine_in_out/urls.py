from django.urls import path
from . import views

app_name = "vaccine_in_out"

urlpatterns = [
    path('vaccinein', views.VaccineInView.as_view(), name="vaccinein"),
    path('vaccineout', views.VaccineOutView.as_view(), name="vaccineout"),
    path('vaccineoutcashdeposit', views.VaccineOutCashDeposit.as_view(), name="vaccineoutcashdeposit"),
]
