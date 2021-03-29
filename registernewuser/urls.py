from django.urls import path

from .views import index

app_name = "registernewuser"

urlpatterns = [
    path('/', index.as_view()),
]
