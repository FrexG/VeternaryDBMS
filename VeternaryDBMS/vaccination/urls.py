from django.urls import path

from .views import Index,SearchVaccinationHistory

app_name = "vaccination"
urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('search_vaccination_history/',SearchVaccinationHistory.as_view(),name="search_vaccination_history"),
]
