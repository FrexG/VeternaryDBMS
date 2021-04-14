from django.urls import path

from .views import index, ProcessService, AIServiceView

app_name = "clinicalservices"

urlpatterns = [
    path('/', index.as_view()),
    path('/processservice', ProcessService.as_view()),
    path('/aiservice', AIServiceView.as_view()),
]
