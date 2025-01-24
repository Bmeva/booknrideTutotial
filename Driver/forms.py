from django import forms
from .models import driver
from authentication.validators import allow_imageonly_validators

class driverregform(forms.ModelForm):
    
    Driver_license = forms.FileField(label='Driver License', 
                                     help_text='Please upload image only', widget=forms.FileInput(),
                                     validators=[allow_imageonly_validators])
    
    class Meta:
        
        model = driver
        fields= ['plate_number', 'vehicle_type', 'Driver_license' ]
        #exclude = ['user', 'user_profile', 'driver_slug', 'isApproved', 'Created_at', 'Modified_at' ]
        
        widgets = {
            'plate_number': forms.TextInput(attrs={'placeholder': 'Enter your vehicle plate number'}),
            'vehicle_type': forms.Select(),
        }
        help_text = {
            'vehicle_type': 'Please select your vehicle type from the drop down'
        }
