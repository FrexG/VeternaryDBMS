from django.urls import path

from .views import Index,UpdateService

app_name = "cashier"

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('update_service/<int:pk>/',UpdateService.as_view(),name="update_service"),
]
