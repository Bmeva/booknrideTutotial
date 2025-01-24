from django.db import models

from django.contrib.auth.models import AbstractUser

# this is a user model for creating log in details
class User(AbstractUser):
    VENDOR = 1
    CUSTOMER = 2
    DRIVER = 3
    
    ROLE_CHOICE = (
    (VENDOR, 'Vendor'),
    (CUSTOMER, 'Customer'),
    (DRIVER, 'Driver')
    )
    
    username = models.CharField( max_length=40)
    email = models.EmailField(unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    def __str__(self):
        return self.username
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    profile_picture = models.ImageField(upload_to='Userfolder/profile_pictures', blank=True, null=True)
    # cover_photo = models.ImageField(upload_to='Userfolder/cover_photos', blank=True, null=True)
    DOB = models.DateTimeField(auto_now_add=False, null= False, blank=False)
    address_line1 = models.CharField(max_length=200)
    adress_line2 = models.CharField(max_length=200)
    nationality =  models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    zip_or_postcode = models.CharField(max_length= 20, blank=True, null=True)
    mobile_number = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name  #this code would return first name
        #return self.first_name + ' ' + self.last_name 
   
