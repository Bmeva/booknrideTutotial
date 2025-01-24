from django.db import models

from authentication.models import User, UserProfile

class driver(models.Model):
    
    Vehicle_Type = (
        ('Bike', 'Bike'),
        ('Car', 'Car'),
    )
    
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='theuser')
    user_profile = models.OneToOneField(UserProfile, on_delete= models.CASCADE, related_name='thedriverprof')
    plate_number = models.CharField(max_length=40)
    vehicle_type = models.CharField(max_length=100, choices =  Vehicle_Type)
    driver_slug = models.SlugField(max_length=100, unique = True)
    Driver_license = models.ImageField(upload_to='driver/license')
    isApproved = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)
    Modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Driver'
    
  
    def __str__(self):
        return f"{self.plate_number} - {self.user.username}"