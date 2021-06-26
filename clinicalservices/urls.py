from django.urls import path

from .views import index, AIServiceView

app_name = "clinicalservices"

urlpatterns = [
    path('/', index.as_view(), name="index"),
    path('/aiservice', AIServiceView.as_view(), name="aiservice"),
]
