from django.contrib import admin
from .models import driver

# Register your models here.

class driverAdmin(admin.ModelAdmin):
    list_display= ('user', 'plate_number', 'vehicle_type')
    list_display_links =('user',)
    list_editable = ('vehicle_type', 'plate_number')

admin.site.register(driver, driverAdmin)
