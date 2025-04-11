from django.urls import path
from .import views



urlpatterns = [
     
    path('view_all_vendors/', views.view_all_vendors, name='view_all_vendors'),
    
 
    
] 