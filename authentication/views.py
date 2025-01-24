from django.shortcuts import render, redirect
from .forms import UserRegisterForm, profileForm
from django.contrib import messages
from .models import User

from django.http import HttpResponse


# Create your views here.
#add checks to see if the user is already logged in 
#add signals to create extended user profile without saving any data to it
def Register(request): #For reguistration of new users
    if request.method == 'POST':
        userform = UserRegisterForm(request.POST)
        userprofileform = profileForm(request.POST, request.FILES)
        
        if userform.is_valid() and userprofileform.is_valid():
            new_user = userform.save(commit=False)
            new_user.role = User.CUSTOMER
            new_user.save()
            
            profile = userprofileform.save(commit=False)
            profile.user = new_user #Assigning the profile form to the newly created user
            profile.save()
            
            messages.success(request, 'Your account has been saved succesfully')
            return redirect('Register')
        else:
              print(userform.errors)
            
    else:
        userform = UserRegisterForm()
        userprofileform = profileForm()
        
    context = {
        'userform': userform,
        'userprofileform': userprofileform
        
    }
        
    return render(request, 'authentication/register.html', context)


