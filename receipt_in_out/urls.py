from django.urls import path
from .views import ReceiptInView,ReceiptOutView

app_name = "receipt_in_out"

urlpatterns = [
    path('',ReceiptInView.as_view(),name="receipt_in"),
     path('receipt_out',ReceiptOutView.as_view(),name="receipt_out")
]
