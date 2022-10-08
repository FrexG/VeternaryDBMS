from django.urls import path

from .views import index,SearchCustomer

app_name = "registernewuser"

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('search_customer',SearchCustomer.as_view(),name="search_customer")
]
