from django import forms
from accounts.models import Doctor

from appointment.models import  DOCTOR_CHOICES, SERVICE_CHOICES, TIME_CHOICES, Appointment



class AppointmentForm(forms.ModelForm):


    
    class Meta:
        model = Appointment
        fields = ["first_name","last_name","department","time"]
        
    first_name =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter Your First Name'
    }))

    last_name =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter Your Last Name'
    }))


    username =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter Your Username'
    }))

    day = forms.DateField(label='Select a day', widget=forms.DateInput(attrs={
        'type': 'date'
    }))




    department = forms.CharField(label='What is your favorite department?',
                                  widget=forms.Select(choices=Doctor.DEPARTMENT_CHOICES))
    





    time =  forms.CharField(label='What is your favorite time?',
                                  widget=forms.Select(choices=TIME_CHOICES))

  




    def __init__(self,*args,**kwargs):
        super(AppointmentForm,self).__init__(*args,**kwargs)

        
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'