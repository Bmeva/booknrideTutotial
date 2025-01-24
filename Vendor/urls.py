from django.urls import path
from .import views




urlpatterns = [
     
    path('vendorReg/', views.VendorReg, name='VendorReg'),
    
    
    
] 