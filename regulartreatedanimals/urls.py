from django.urls import path

from .views import index

app_name = "regulartreatedanimals"

urlpatterns = [
    path('/', index.as_view()),
]
