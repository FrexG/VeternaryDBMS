from django.urls import path
from .views import Index,OpdRegularView,OpdParasiteView

app_name = "opd"

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('opd_regular_prescription/<int:pk>/',OpdRegularView.as_view(),name="opd_regular_prescription"),
    path('opd_parasite_prescription/<int:pk>/',OpdParasiteView.as_view(),name="opd_parasite_prescription"),
]