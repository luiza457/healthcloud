from django import forms 
from .models import Contact, Pacient,Doctor


class PacientRegistrationForm(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password'
    }))


  


    class Meta:
        model = Pacient
        fields = ['first_name','last_name','phone_number','email','password']
        

    # loop through all fields and assign the widget attribute class
    # for a nicer look
    def __init__(self,*args,**kwargs):
        super(PacientRegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


    def clean(self):
        # super class changes the way the fields are saved
        cleaned_data = super(PacientRegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # check if passwords match 
        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match'
            )


class DoctorRegistrationForm(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Confirm Password'
    }))

  

    class Meta:
        model = Doctor
        fields = ['first_name','last_name','department','phone_number','birthdate','email','password']
        

    # loop through all fields and assign the widget attribute class
    # for a nicer look
    def __init__(self,*args,**kwargs):
        super(DoctorRegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'

        department_choices = Doctor.DEPARTMENT_CHOICES
        department = forms.ChoiceField(choices=department_choices)

        self.fields['birthdate'].widget = forms.DateInput(attrs={'type':'date'})




        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


    def clean(self):
        # super class changes the way the fields are saved
        cleaned_data = super(DoctorRegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # check if passwords match 
        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match'
            )


class ContactForm(forms.ModelForm):


    
    class Meta:
        model = Contact
        fields = ['first_name',"last_name","subject"]
        
    first_name =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter Your First Name'
    }))

    last_name =  forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter Your Last Name'
    }))


    subject =  forms.CharField(widget=forms.Textarea(attrs={
        'placeholder' : 'Write something here...'
    }))





    def __init__(self,*args,**kwargs):
        super(ContactForm,self).__init__(*args,**kwargs)

        
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'