from django.urls import path

from .views import index

app_name = "clinicalservices"

urlpatterns = [
    path('/', index.as_view()),
]
