from django.urls import path
from .views import Index

app_name = "abattoir_exam"

urlpatterns = [
    path('',Index.as_view(),name="index"),
]
