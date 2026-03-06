from django.contrib import admin
from .models import feedback, Property, register

@admin.register(Property)
class propertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'property_type', 'beds', 'baths', 'sqft')
    
    
@admin.register(feedback)
class feedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    
@admin.register(register)
class registerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'country')        
