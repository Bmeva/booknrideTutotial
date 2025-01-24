from django.db import models
from authentication.models import User, UserProfile

# Create your models here.

vendor_type = (
    ('Individual', 'Individual'),
    ('Business', 'Business'),
)


class VendorRegistration(models.Model):
    user = models.OneToOneField(User, related_name='user',on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name='thevendor', on_delete=models.CASCADE)
    vendorname =models.CharField(max_length=300)
    vendorType = models.CharField(max_length=100, choices=vendor_type, default='Individual')
    vendorlicense= models.ImageField(upload_to='Vendor/license') 
    
    vendorslug = models.SlugField(max_length=50, unique=True) 
    Isapproved = models.BooleanField(default=False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.vendorname
    
  
    