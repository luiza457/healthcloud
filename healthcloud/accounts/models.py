import datetime
from django.db import models 
from django.contrib.auth.models import User

# account for pacient, doctor and superadmin 
    
class Pacient(models.Model):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)

    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
   
  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']


    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email



class Doctor(models.Model):

    DEPARTMENT_CHOICES = (
        ('Allergy / Immunology', 'Allergy / Immunology'),
        ('Cardiovascular / Pulmonary ', 'Cardiovascular / Pulmonary'),
        ('Consult - History and Phy.','Consult - History and Phy.'),
        ('Dermatology', 'Dermatology'),
        ('Endocrinology', 'Endocrinology'),
        ('Gastroenterology', 'Gastroenterology'),
        ('General Medicine','General Medicine'),
        ('Genomics', 'Genomics'),
        ('Hematology', 'Hematology'),
        ('Immunology', 'Immunology'),
        ('Infectious Diseases', 'Infectious Diseases'),
        ('Neurology', 'Neurology'),
        ('Obstetrics / Gynecology ', 'Obstetrics / Gynecology '),
        ('Hematology - Oncology', 'Hematology - Oncology'),
        ('Orthopedic','Orthopedic'),
        ('Psychiatry / Psychology', 'Psychiatry / Psychology'),
        ('Radiology', 'Radiology'),
        ('Routine Check-Up', 'Routine Check-Up'),
        ('Surgery','Surgery'),
        ('Urology', 'Urology'),
        ('Vaccines','Vaccines'),
    )
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    birthdate = models.DateField(null=True)

    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email
    

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.TextField(max_length=300)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'subject']


   