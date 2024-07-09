#from django.core import validators 
from django import forms 
from .models import Register 
from django.contrib.auth.password_validation import validate_password 
from django.core.exceptions import ValidationError
import re 
class UserModelForm(forms.ModelForm):
    class Meta:
        model = Register 
        fields = ['name','email','mobile','password','re_renter_password'] 
        labels = {'name':"Enter Your Name ",
                  'email':'Enter Your Email ',
                  'mobile':'Enter Your Mobile Number ', 
                  'password':'Enter Password ', 
                  're_renter_password':"Re-Enter Paswword "
                  } 
        widgets = {'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control','placeholder':"Enter Password"}),
                   're_renter_password':forms.PasswordInput(render_value=True, attrs={'class':'form-control','placeholder':"Enter password Again"}),
                   'name':forms.TextInput(attrs={'class':'form-control','placeholder':"Enter your Name"}),
                   'email':forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter your Email"}),
                   'mobile':forms.NumberInput(attrs={'class':'form-control','placeholder':"Enter your Mobile Number"})
                   }   
   # password = forms.CharField(forms.PasswordInput,validators=[validators.MinLengthValidator(8)])
    def clean(self):  
        cleaned_data  = super().clean() 
        pass1 = cleaned_data.get('password') 
        pass2 = cleaned_data.get('re_renter_password')  
        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError("Password Do Not Match") 
        if pass1:
            if len(pass1)<8:
                raise ValidationError("Password length must coontains 8 characters") 
            if not re.findall('[A-Z]', pass1):
                raise ValidationError("This password must contain at least one uppercase letter.")
            if not re.findall('[a-z]', pass1):
                raise ValidationError("This password must contain at least one lowercase letter.")
            if not re.findall('[0-9]', pass1):
                raise ValidationError("This password must contain at least one digit.")
            if not re.findall('[^A-Za-z0-9]', pass1):
                raise ValidationError("This password must contain at least one special character.")
        return self.cleaned_data
        
