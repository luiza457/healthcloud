"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
  #  path('admin/', admin.site.urls),
    path('dashboard/dashboard_pacient/', views.dashboard_pacient, name='dashboard_pacient'),
    path('dashboard/dashboard_doctor/', views.dashboard_doctor, name='dashboard_doctor'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_profile_doctor/', views.edit_profile_doctor, name='edit_profile_doctor'),


    path('radiography_doctor/', views.radiography_doctor, name='radiography_doctor'),
    path('reports_pacient/', views.reports_pacient, name='reports_pacient'),
    path('my_patients/', views.my_patients, name='my_patients'),




]
