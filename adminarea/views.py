from django.shortcuts import render
from Vendor.models import VendorRegistration
from django.http import HttpResponse
# Create your views here.

def view_all_vendors(req):
    
    thevendors = VendorRegistration.objects.all() 
   #thevendors_approved = VendorRegistration.objects.filter(Isapproved =True)   
    
    context = {
        'thevendors': thevendors
    }
    
    return render(req, 'adminarea/viewallrec.html', context)

