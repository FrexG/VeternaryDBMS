from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path('', views.Login.as_view(), name="login"),
    path('signup', views.Signup.as_view(), name="signup"),
    path('logout', views.Logout.as_view(), name="logout"),
]
