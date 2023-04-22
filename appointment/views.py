import json
import random
import re
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from accounts.models import Doctor, Pacient
from django.contrib.auth.models import User, Group

from appointment.forms import AppointmentForm
from appointment.models import Appointment

# Create your views here.
pacients = Pacient.objects.all()

usernames = [pacient.username for pacient in pacients]
def dashboard_pacient(request):
    return render(request,'dashboard/dashboard_pacient')

def make_appointment(request):



    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            department = form.cleaned_data['department']

            day = form.cleaned_data['day']
            time = form.cleaned_data['time']

            if not Pacient.objects.filter(username=username).exists():
                messages.error(request,"Not a valid username")
                return redirect('make_appointment')
            
            # Check if the chosen day is already taken
            appointments = Appointment.objects.filter(day=day,department=department)

            
            available_doctors = Doctor.objects.filter(department=department)

            # appointment has not been created yet
            available_doctors = available_doctors.exclude(appointment__day=day, appointment__time=time)

            for appointment in appointments:

                if appointment.time == time and appointment.department == department and available_doctors is None:
                    messages.error(request, f"The time slot {time} on {day} is already taken for your chosen department.")
                
                    return redirect('make_appointment')
                

            pacient = Pacient.objects.get(username=username)



            # get available doctor randomly 
            doctor =  random.choice(available_doctors)
   
        

            appointment = Appointment.objects.create(first_name=first_name, last_name=last_name, username=username, patient=pacient,doctor=doctor,department=department, day=day, time=time)
            appointment.save()
            messages.success(request, 'Thank you for completing this form! We will come back with a reply as soon as possible.')
            return redirect('make_appointment')


    else:

            
        form = AppointmentForm()
        context = {'form': form}
        return render(request, 'appointment/make_appointment.html', context)




def my_appointments(request):



    pacient_name = request.session.get('pacient_name')
    pacient_last_name = request.session.get('pacient_last_name')
    pacient_username = request.session.get('pacient_username')
    pacient_email = request.session.get('pacient_email')
    pacient_phone_number = request.session.get('pacient_phone_number')


    appointment_doctor =  request.session.get('appointment_doctor') 
    appointment_department =  request.session.get('appointment_department')
    appointment_time =   request.session.get('appointment_time') 
    
    appointment_day =  request.session.get('appointment_day') 
    appointment_doctor =  request.session.get('appointment_doctor') 
    count =  request.session.get('count') 
    numbers =  request.session.get('numbers') 





    context = {'pacient_name': pacient_name,
               'pacient_last_name' : pacient_last_name,
               'pacient_username' : pacient_username,
               'pacient_email' : pacient_email,
                'pacient_phone_number' : pacient_phone_number,
                'appointment_doctor' : appointment_doctor,
                'appointment_department': appointment_department,
                'appointment_day' : appointment_day,
                'appointment_time' : appointment_time,
                 'count' : count,
                 'numbers' : numbers,



               
               
               
               }
    return render(request, 'dashboard/my_appointments.html', context)


def my_appointments_doctor(request):


    doctor_name = request.session.get('doctor_name')
    doctor_last_name = request.session.get('doctor_last_name')
    doctor_username = request.session.get('doctor_username')
    doctor_email = request.session.get('doctor_email')
    doctor_phone_number = request.session.get('doctor_phone_number')

    appointment_pacient =  request.session.get('appointment_pacient') 
    appointment_contact =   request.session.get('appointment_contact') 

    appointment_time =   request.session.get('appointment_time') 
    
    appointment_day =  request.session.get('appointment_day') 
    count =  request.session.get('count') 
    numbers =  request.session.get('numbers') 


    username =  request.session.get('username') 
    first_name =  request.session.get('first_name') 







    context = {'doctor_name': doctor_name,
               'doctor_last_name' : doctor_last_name,
               'doctor_username' : doctor_username,
               'doctor_email' : doctor_email,
                'doctor_phone_number' : doctor_phone_number,
                'appointment_pacient' : appointment_pacient,
                'appointment_contact' : appointment_contact,
                'appointment_day' : appointment_day,
                'appointment_time' : appointment_time,
                 'count' : count,
                 'numbers' : numbers,
                 
                 'username': username,
                 'first_name' : first_name,
    }

    return render(request,'dashboard/my_appointments_doctor.html',context)