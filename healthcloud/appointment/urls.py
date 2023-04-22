from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('make_appointment/', views.make_appointment, name='make_appointment'),
    path('dashboard_pacient/', views.dashboard_pacient, name='dashboard_pacient'),
    path('my_appointments/',views.my_appointments,name='my_appointments'),
    path('my_appointments_doctor/',views.my_appointments_doctor,name='my_appointments_doctor'),


   

 
]