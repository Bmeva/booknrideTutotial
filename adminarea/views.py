from django.shortcuts import render, redirect
from Vendor.models import VendorRegistration
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.

def view_all_vendors(req):
    
    thevendors = VendorRegistration.objects.all() 
   #thevendors_approved = VendorRegistration.objects.filter(Isapproved =True)   
    
    context = {
        'thevendors': thevendors
    }
    
    return render(req, 'adminarea/viewallrec.html', context)


def view_single_record(request, pk):
    
    try:
        
        thesinglevendor = VendorRegistration.objects.get(pk = pk)
        
    except VendorRegistration.DoesNotExist:
        return HttpResponse('the record you are trying to view does not exist')
        
    
    context = {
        
        'thesinglevendor': thesinglevendor,
    }
    
    return render(request, 'adminarea/view_single_record.html', context)

def delete_single_vendor(request, pk):
    theven = get_object_or_404(VendorRegistration, pk=pk)
    theven.delete()
    themessage = 'vendor account deleted succesfully'
    messages.info(request, 'account deleted succesfully')
    return redirect('view_all_vendors')



