"""VeternaryDBMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('register/', include('registernewuser.urls')),
    path('regular/', include('regulartreatedanimals.urls')),
    path('clinicalservice/', include('clinicalservices.urls')),
    path('parasitetreatment/', include('parasitetreatment.urls')),
    path('cashier/',include('cashier.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('vaccination/',include('vaccination.urls')),
    path('pharmacy/',include('pharmacy.urls')),
    path('drug_in_out/',include('drug_in_out.urls')),
    path('equipment_in_out/',include('equipment_in_out.urls')),
    path('vaccine_in_out/',include('vaccine_in_out.urls')),
    path('abattoir_exam/',include('abattoir_exam.urls')),
    path('lab_exam/',include('lab_exam.urls')),
    path('receipt_in_out/',include('receipt_in_out.urls')),
    path('stock/',include('stock.urls')),
    path('search/',include('search.urls')),
    path('opd/',include('opd.urls')),
    path('admin/', admin.site.urls),
]
