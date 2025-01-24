from django import forms
from .models import VendorRegistration
from authentication.validators import allow_imageonly_validators



class vendorform(forms.ModelForm): 
    vendorlicense = forms.FileField(label='Vendor License',  help_text='Please your vendor license, image only', widget=forms.FileInput(), validators=[allow_imageonly_validators])
        
    
           
    class Meta:
        model = VendorRegistration
        fields = ['vendorname', 'vendorlicense', 'vendorType']  
        
        widgets = {
            'VendorName': forms.TextInput(attrs={'placeholder': 'Enter your vendor name'}),
          
            'vendorType': forms.Select(), 
            
                    
        }
        help_text = {
            'vendorType': 'Please select your vendor type'
        }
        
    