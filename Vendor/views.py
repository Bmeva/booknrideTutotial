from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import vendorform
from authentication.forms import profileForm, UserRegisterForm
from authentication.models import User
from django.template.defaultfilters import slugify



def VendorReg(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already resgitered')
        
        return redirect('home')
    elif request.method == 'POST':
        userform = UserRegisterForm(request.POST)
        profileform = profileForm(request.POST, request.FILES)
        V_form = vendorform(request.POST, request.FILES)
       
       
        
        if V_form.is_valid() and userform.is_valid() and profileform.is_valid():
            password = userform.cleaned_data['password1']
            theuser = userform.save(commit=False)
            theuser.set_password(password)
            theuser.role = User.VENDOR
            theuser.save()
            
            #saving the profile of the vendor
            profile = profileform.save(commit = False)
            profile.user = theuser
            profile.save()
                                             
            thevendor =V_form.save(commit=False)
            thevendor.user = theuser
            thevendor.user_profile = profile
            thevendorname = V_form.cleaned_data['vendorname']
            thevendor.vendorslug = slugify(thevendorname) + '-'+str(theuser.id)
            thevendor.save()
            
            messages.success(request, "Your vendor account has been created successfully")
            return redirect('home')
        else:
            print('invalid forms')
            print(V_form.errors, userform.errors, profileform.errors)
    else:
        userform = UserRegisterForm()
        profileform = profileForm()
        V_form = vendorform()
        
    data ={
        'userregform':UserRegisterForm,
        'profileform': profileForm,
        'vendorform': vendorform
       
        
    }
        
           
    return render(request, 'Vendor/vendorReg.html', data)
