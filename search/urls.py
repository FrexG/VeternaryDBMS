from django.urls import path
from .views import SearchHistory

app_name = "search"

urlpatterns = [
    path('',SearchHistory.as_view(),name="search"),
]
