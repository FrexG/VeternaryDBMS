from unicodedata import name
from django.urls import path
from .views import Index

app_name = "lab_exam"

urlpatterns = [
    path('',Index.as_view(),name="index"),
]
