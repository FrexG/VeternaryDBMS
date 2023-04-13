from django.urls import path
from . import views

app_name = "equipment_in_out"

urlpatterns = [
    path('equipmentin', views.EquipmentInView.as_view(), name="equipmentin"),
    path('equipmentout', views.EquipmentOutView.as_view(), name="equipmentout"),
   # path('equipmentoutcashdeposit', views.EquipmentOutCashDeposit.as_view(), name="equipmentoutcashdeposit"),
]
