from django.urls import path

from . import views
app_name = "vaccineandparasite"
urlpatterns = [
    path('/', views.index, name='index'),
]
