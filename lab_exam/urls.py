from unicodedata import name
from django.urls import path
from .views import Index,SubmitLabResults

app_name = "lab_exam"

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('/<int:pk>',Index.as_view(),name="get_result"),
    path('/submit_result',SubmitLabResults.as_view(),name="submit_result"),
]
