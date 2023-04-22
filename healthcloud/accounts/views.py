import json
import re
from django.db.models import F, Max
from django.contrib import messages,auth
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import ContactForm, PacientRegistrationForm,DoctorRegistrationForm
from appointment.models import Appointment
from .models import  Pacient ,Doctor
from django.http import HttpResponse

# Create your views here.
def dashboard_pacient(request):
    return render(request,'dashboard/dashboard_pacient')

def dashboard_doctor(request):
    return render(request,'dashboard/dashboard_doctor')

def register_pacient(request):
    user = "none"

    if request.method == 'POST' :
        form = PacientRegistrationForm(request.POST)
        

        if form.is_valid():
            # fetch the values from the request with cleaned data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']






            #make the user based on email 
            username = email.split("@")[0]
           


            try:
                if password == confirm_password:
          
                    pacient = Pacient.objects.create(first_name=first_name,last_name=last_name,email=email,username=username,phone_number=phone_number)
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=email,password=password)
                    pat_group = Group.objects.get(name='Pacient')
                    pat_group.user_set.add(user)
                    user.save()
                    # update user object with phone number
                    pacient.phone_number = phone_number

                 #   pacient.save()
                    messages.success(request,'Registration successful!')
                    return redirect('register_pacient')

            except Exception as e:
                 raise e 
                 
         

    else:
            form = PacientRegistrationForm()



    context = {
            'form': form,
        }
    return render(request,'accounts/register_pacient.html',context)


def login_pacient(request):
     
     if request.method == "POST":
          u = request.POST['email']
          p = request.POST['password']
     
          user = authenticate(request,username=u,password=p)
      #    try:
          if user is not None:
                    login(request,user)
                    # group name of user 
                    g = request.user.groups.all()[0].name
                    if g == 'Pacient':
                         pacient = Pacient.objects.get(email=u)




                         request.session['pacient_name'] = pacient.first_name
                         request.session['pacient_last_name'] = pacient.last_name
                         request.session['pacient_username'] = pacient.username
                         request.session['pacient_email'] = pacient.email
                         request.session['pacient_phone_number'] = pacient.phone_number

                         appointments = Appointment.objects.filter(patient=pacient)

                         count = appointments.count()

                         request.session['count'] = count
                         numbers = list(range(1, count + 1))

                         request.session['numbers'] = numbers



                         #get departments and store them as session variable
                         appointment_departments = []
                         for appointment in appointments:
                            appointment_departments.append(appointment.department)

                         request.session['appointment_department'] = appointment_departments


                        #get doctors 
                         appointment_doctors = []
                         for appointment in appointments:
                            appointment_doctor = json.dumps( appointment.doctor.last_name, default=str)
                            appointment_doctor =  re.sub(r'[""]', '', appointment_doctor)
                            appointment_doctors.append(appointment_doctor)

                            

                         request.session['appointment_doctor'] = appointment_doctors

                             # make the date serializable
                         appointment_days = []
                         for appointment in appointments:
                            appointment_day = json.dumps( appointment.day, default=str)
                            appointment_day =  re.sub(r'[""]', '', appointment_day)
                            appointment_days.append(appointment_day)


                         request.session['appointment_day'] =appointment_days


                         appointment_times = []
                         for appointment in appointments:
                            appointment_time = json.dumps( appointment.time, default=str)
                            appointment_time =  re.sub(r'[""]', '', appointment_time)
                            appointment_times.append(appointment_time)


                         request.session['appointment_time'] =appointment_times
                         




                         



                         return redirect('dashboard_pacient')
                    
          else:
                messages.error(request,"Invalid login credentials.")
                return redirect('login_pacient')
                
       #   except Exception as e:
       #    print(e)
     
     # session variable which stores pacient's name 

     return render(request,'accounts/login_pacient.html')
     


def register_doctor(request):
    user = "none"

    if request.method == 'POST' :
        form = DoctorRegistrationForm(request.POST)
        

        if form.is_valid():
            # fetch the values from the request with cleaned data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            department = form.cleaned_data['department']
            birthdate = form.cleaned_data['birthdate']


            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']






            #make the user based on email 
            username = email.split("@")[0]
           


            try:
                if password == confirm_password:
            
                        doctor = Doctor.objects.create(first_name=first_name,last_name=last_name,department=department,birthdate=birthdate,email=email,username=username,phone_number=phone_number)
                        user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=email,password=password)
                        pat_group = Group.objects.get(name='Doctor')
                        pat_group.user_set.add(user)
                        user.save()
                        # update user object with phone number
                        doctor.phone_number = phone_number

                    #   pacient.save()
                        messages.success(request,'Registration successful!')
                        return redirect('register_doctor')
                
           
            except Exception as e:
                 raise e 
                 
         

    else:
            form = DoctorRegistrationForm()



    context = {
            'form': form,
        }
    return render(request,'accounts/register_doctor.html',context)


def login_doctor(request):
     
     if request.method == "POST":
          u = request.POST['email']
          p = request.POST['password']
     
          user = authenticate(request,username=u,password=p)
        #  try:
          if user is not None:
                    login(request,user)
                    # group name of user 
                    g = request.user.groups.all()[0].name
                    if g == 'Doctor':
                         doctor = Doctor.objects.get(email=u)


                         request.session['doctor_name'] = doctor.first_name
                         request.session['doctor_last_name'] = doctor.last_name
                         request.session['doctor_username'] = doctor.username
                         request.session['doctor_email'] = doctor.email
                         request.session['doctor_phone_number'] = doctor.phone_number
                         request.session['doctor_department'] = doctor.department


                         doctor_birthdate = json.dumps( doctor.birthdate, default=str)
                         doctor_birthdate =  re.sub(r'[""]', '', doctor_birthdate)
                         request.session['doctor_birthdate'] = doctor_birthdate

                        # get all appointments for our doctor and group by patient field 
                        # add new column last_appointment 
                        # values() to only select the last field 
                         distinct_appointments = Appointment.objects.filter(doctor=doctor) \
                            .values('patient') \
                            .annotate(last_appointment=Max('id')) \
                            .values('last_appointment')

                        # filter to get distinct appointments 
                         appointmentss = Appointment.objects.filter(id__in=distinct_appointments)
                         apps = Appointment.objects.filter(doctor=doctor)


                         appointments = set()

                         for appointment in appointmentss:
                              appointments.add(appointment)
                              

                         distinct_patients = set()
                         usernames = []
                         first_names = []
                         last_names = []
                         emails = []
                         phone_numbers = []



                         for appointment in appointments:
                            # il iau distinct de aici 
                            patient = appointment.patient
                            patient = json.dumps( patient, default=str)

                            patient =  re.sub(r'[""]', '', patient)


                            distinct_patients.add(patient)
                            patients = list(distinct_patients)

                            print(patients)
                            username = appointment.patient.username
                            first_name = appointment.patient.first_name
                            last_name = appointment.patient.last_name
                            email = appointment.patient.email
                            phone_number = appointment.patient.phone_number

                            first_names.append(first_name)
                            last_names.append(last_name)
                            emails.append(email)
                            usernames.append(username)

                            phone_numbers.append(phone_number)

                
                            print(patient)

                             

                         request.session['patient'] = patients
                         request.session['username'] = usernames
                         request.session['first_name'] = first_names
                         request.session['last_name'] = last_names
                         request.session['email'] = emails
                         request.session['phone_number'] = phone_numbers




                              

                         count = apps.count()

                         request.session['count'] = count
                         numbers = list(range(1, count + 1))

                         request.session['numbers'] = numbers






                        #get patients 
                         all_appointments = Appointment.objects.filter(doctor=doctor)
                         appointment_pacients = []
                         appointment_contacts = []

                         for appointment in all_appointments:
                            appointment_pacient = json.dumps( appointment.patient.last_name, default=str)
                            appointment_contact = json.dumps( appointment.patient.phone_number, default=str)
                            appointment_contact =  re.sub(r'[""]', '', appointment_contact)

                            appointment_pacient =  re.sub(r'[""]', '', appointment_pacient)
                            appointment_pacients.append(appointment_pacient)
                            appointment_contacts.append(appointment_contact)

                            

                         request.session['appointment_pacient'] = appointment_pacients
                         request.session['appointment_contact'] = appointment_contacts


                             # make the date serializable
                         appointment_days = []
                         for appointment in all_appointments:
                            appointment_day = json.dumps( appointment.day, default=str)
                            appointment_day =  re.sub(r'[""]', '', appointment_day)
                            appointment_days.append(appointment_day)


                         request.session['appointment_day'] =appointment_days


                         appointment_times = []
                         for appointment in all_appointments:
                            appointment_time = json.dumps( appointment.time, default=str)
                            appointment_time =  re.sub(r'[""]', '', appointment_time)
                            appointment_times.append(appointment_time)


                         request.session['appointment_time'] =appointment_times
                         




                         return redirect('dashboard_doctor')
                    
          else:
                messages.error(request,"Invalid login credentials.")
                return redirect('login_doctor')
          
     return render(request,'accounts/login_doctor.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
          #  country = form.cleaned_data['country']


            subject = form.cleaned_data['subject']
          
            messages.success(request,'Thank you for completing this form! We will come back with a reply as soon as possible.')
            return redirect('contact')
    else:
        form = ContactForm()

        context = {
            'form': form,
        }
    return render(request, 'accounts/contact.html',context)


@login_required(login_url = 'login_pacient')
def logout_pacient(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login_pacient')


@login_required(login_url = 'login_doctor')
def logout_doctor(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login_doctor')