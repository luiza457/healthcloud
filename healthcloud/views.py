from django.shortcuts import redirect, render

from accounts.forms import PacientRegistrationForm
from accounts.models import Pacient


def home(request):
    
    
    return render(request,'home.html')



def services(request):
    
    
    return render(request,'services.html')


def contact(request):
    
    
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')

