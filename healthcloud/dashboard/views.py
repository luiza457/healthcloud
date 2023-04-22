from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group

from accounts.models import Doctor, Pacient


def dashboard_pacient(request):



    pacient_name = request.session.get('pacient_name')
    pacient_last_name = request.session.get('pacient_last_name')
    pacient_username = request.session.get('pacient_username')
    pacient_email = request.session.get('pacient_email')
    pacient_phone_number = request.session.get('pacient_phone_number')


    context = {'pacient_name': pacient_name,
               'pacient_last_name' : pacient_last_name,
               'pacient_username' : pacient_username,
               'pacient_email' : pacient_email,
                'pacient_phone_number' : pacient_phone_number,
               
               
               
               }
    return render(request, 'dashboard/dashboard_pacient.html', context)


def dashboard_doctor(request):



    doctor_name = request.session.get('doctor_name')
    doctor_last_name = request.session.get('doctor_last_name')
    doctor_username = request.session.get('doctor_username')
    doctor_email = request.session.get('doctor_email')
    doctor_phone_number = request.session.get('doctor_phone_number')
    doctor_birthdate = request.session.get('doctor_birthdate')
    doctor_department = request.session.get('doctor_department')



    context = {'doctor_name': doctor_name,
               'doctor_last_name' : doctor_last_name,
               'doctor_username' : doctor_username,
               'doctor_email' : doctor_email,
                'doctor_phone_number' : doctor_phone_number,
                'doctor_birthdate' : doctor_birthdate,
                'doctor_department' : doctor_department,  


               
               
               
               }
    return render(request, 'dashboard/dashboard_doctor.html', context)

def edit_profile(request):
    # Get current user's profile data from session
    pacient = Pacient.objects.get(username=request.session.get('pacient_username'))
    user = User.objects.get(email=pacient.email)


    if request.method == 'POST':
        # Update profile data based on form submission
        pacient.first_name = request.POST.get('pacient_name')
        pacient.last_name = request.POST.get('pacient_last_name')
        pacient.username = request.POST.get('pacient_username')
        pacient.email = request.POST.get('pacient_email')
        pacient.phone_number = request.POST.get('pacient_phone_number')

        # Save updated pacient instance to the database
        pacient.save()

        

        # Update session data
        request.session['pacient_name'] = pacient.first_name
        request.session['pacient_last_name'] = pacient.last_name
        request.session['pacient_username'] = pacient.username
        request.session['pacient_email'] = pacient.email
        request.session['pacient_phone_number'] = pacient.phone_number

        user.first_name = pacient.first_name
        user.last_name = pacient.last_name
        user.username = pacient.email
        user.email = pacient.email

        user.save()


        # Redirect to dashboard_pacient view or any other desired page
        return redirect('dashboard_pacient')

    context = {'pacient': pacient}
    return render(request, 'dashboard/edit_profile.html', context)


def edit_profile_doctor(request):
    # Get current user's profile data from session
    doctor = Doctor.objects.get(username=request.session.get('doctor_username'))
    user = User.objects.get(email=doctor.email)


    if request.method == 'POST':
        # Update profile data based on form submission
        doctor.first_name = request.POST.get('doctor_name')
        doctor.last_name = request.POST.get('doctor_last_name')
        doctor.username = request.POST.get('doctor_username')
        doctor.email = request.POST.get('doctor_email')
        doctor.phone_number = request.POST.get('doctor_phone_number')

        # Save updated pacient instance to the database
        doctor.save()

        

        # Update session data
        request.session['doctor_name'] = doctor.first_name
        request.session['doctor_last_name'] = doctor.last_name
        request.session['doctor_username'] = doctor.username
        request.session['doctor_email'] = doctor.email
        request.session['doctor_phone_number'] = doctor.phone_number



        user.first_name = doctor.first_name
        user.last_name = doctor.last_name
        user.username = doctor.email
        user.email = doctor.email

        user.save()


        # Redirect to dashboard_pacient view or any other desired page
        return redirect('dashboard_doctor')

    context = {'doctor': doctor}
    return render(request, 'dashboard/edit_profile_doctor.html', context)


def radiography_doctor(request):
    return render(request, 'dashboard/radiography_doctor.html')



def reports_pacient(request):
    return render(request, 'dashboard/reports_pacient.html')


def my_patients(request):

    patient =  request.session.get('patient') 

    username =  request.session.get('username') 
    first_name =  request.session.get('first_name') 
    last_name =  request.session.get('last_name') 
    email =  request.session.get('email') 
    phone_number =  request.session.get('phone_number') 




    context = { 
        'patient' : patient,

        'username': username,
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : email ,
        'phone_number' : phone_number,
    }

    return render(request, 'dashboard/my_patients.html',context)