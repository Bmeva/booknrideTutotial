from django.contrib import admin

from .models import User, UserProfile


#from authentication.models import User



class userAdmin(admin.ModelAdmin):
    list_display =('username', 'email', 'is_staff', 'is_superuser',)
    list_editable = ('email', 'is_staff', 'is_superuser',)
    #readonly_fields = ('email', 'password',) to make fields uneditable
   
    
    

class userProfileadmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'nationality',)
    list_editable = ('first_name', 'last_name',)
    list_display_links = ('nationality', 'user',)
    
    

admin.site.register(User, userAdmin)



admin.site.register(UserProfile, userProfileadmin)