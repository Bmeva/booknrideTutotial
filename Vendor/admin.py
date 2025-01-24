from django.contrib import admin

from .models import VendorRegistration

# Register your models here.

class vendoradmin(admin.ModelAdmin):
    list_display = ('user', 'vendorname', 'vendorType', 'CreatedAt',)
    list_display_links = ('vendorname', 'user',)
    
    
admin.site.register(VendorRegistration, vendoradmin)
