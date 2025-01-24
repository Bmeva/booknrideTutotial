from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User
from .models import UserProfile
from django.forms import ImageField, FileInput, DateInput
from .validators import allow_imageonly_validators






class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets ={
            
            'username': forms.TextInput(attrs={'placeholder': 'User Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter your email'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Enter your password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'epeat password'}),
            
                    
            
        }
    
        
 
        

class profileForm(forms.ModelForm):
    
    profile_picture = ImageField(widget = FileInput(), validators=[allow_imageonly_validators])  
    cover_photo = ImageField(widget=FileInput(), validators=[allow_imageonly_validators])
    DOB = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'DOB', 'address_line1', 'profile_picture', 'cover_photo',
                  
                  'adress_line2', 'nationality', 'city', 'zip_or_postcode', 'mobile_number']
        
        widgets ={
            
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'address_line1': forms.TextInput(attrs={'placeholder': 'Address One'}),
            'adress_line2': forms.TextInput(attrs={'placeholder': 'Address two'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'Nationality'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'zip_or_postcode': forms.TextInput(attrs={'placeholder': 'Enter Zip or post code'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Mobile number'}),
       
        }
    