from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import driverregform
from authentication.forms import profileForm, UserRegisterForm
from authentication.models import User, UserProfile
from django.template.defaultfilters import slugify

def driverreg(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('home')
    elif request.method == 'POST':
        d_form = driverregform(request.POST, request.FILES)
        theprofile_form = profileForm(request.POST, request.FILES)
        userregform = UserRegisterForm(request.POST)
        
        if d_form.is_valid() and theprofile_form.is_valid() and userregform.is_valid():
            password = userregform.cleaned_data['password1']
            theuser = userregform.save(commit=False)
            theuser.set_password(password)
            theuser.role = User.DRIVER
            theuser.save()
            
            
            profile = theprofile_form.save(commit=False)
            profile.user = theuser
            profile.save()
            
            
            driverR = d_form.save(commit=False)
            driverR.user = theuser
            driverR.user_profile = profile
            the_plate_number = d_form.cleaned_data['plate_number']
            driverR.driver_slug = slugify(the_plate_number)+ '-' + str(theuser.id)
            driverR.save()
            
                     
            thefirstname = profile.first_name 
            theusername = theuser.username
                       
            
            messages.success(request, f'{thefirstname}, {theusername}, Your account has been created succesfully')
            
            return redirect('home')
        else:
            print('Invald form')
            messages.error(request, 'Invalid form')
    else:
        d_form = driverregform()
        theprofile_form = profileForm()
        userregform = UserRegisterForm
        
        
    context = {
        'd_form': d_form,
        'theprofile_form': theprofile_form,
        'userregform': userregform
        
        
    }
                    
    
    return render(request, 'Driver/driverreg.html', context)