from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('', views.login.as_view(), name="login"),
]
