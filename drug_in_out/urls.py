from django.urls import path
from . import views

app_name = "drug_in_out"

urlpatterns = [
    path('drugin', views.DrugInView.as_view(), name="drugin"),
    path('drugout', views.DrugOutView.as_view(), name="drugout"),
    path('drugoutcashdeposit', views.DrugOutCashDeposit.as_view(), name="drugoutcashdeposit"),
]
