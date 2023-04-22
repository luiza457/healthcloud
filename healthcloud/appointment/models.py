from django.db import models

# Create your models here.


from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User

from accounts.models import Doctor, Pacient



doctors = Doctor.objects.all()

DOCTOR_CHOICES = [(doctor.last_name,doctor.last_name) for doctor in doctors]

# take no duplicates 
SERVICE_CHOICES = [(doctor.department,doctor.department) for doctor in doctors]

today = datetime.today().date()


TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    
 
)

class Appointment(models.Model):
    first_name =   models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    username =  models.CharField(max_length=50,blank=True,null=True)

    patient = models.ForeignKey(Pacient, on_delete=models.CASCADE,null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True)

    department = models.CharField(max_length=50, choices=Doctor.DEPARTMENT_CHOICES)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")

   # dataset fields
    description =  models.CharField(max_length=200)
    sample_name =  models.CharField(max_length=50)
    transcription =  models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)





    def __str__(self):
        return f"{self.first_name}  | time: {self.time}"