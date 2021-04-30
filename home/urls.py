from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('login', views.login.as_view(), name="login"),
    path('signup', views.signup.as_view(), name="signup"),
]
