from django.urls import path

from .views import *

app_name = "stock"

urlpatterns = [
    path('select_printouts',StockPrintOutView.as_view(),name="select_printouts"),
]
