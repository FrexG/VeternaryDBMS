from django.urls import path

from .views import index, ProcessService, AIServiceView

app_name = "clinicalservices"

urlpatterns = [
    path('/', index.as_view(), name="index"),
    path('/processservice', ProcessService.as_view(), name="processservice"),
    path('/aiservice', AIServiceView.as_view(), name="aiservice"),
]
