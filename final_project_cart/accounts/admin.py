from django.contrib import admin
from .models import *

# Register your models here.
 
 # trial versions
 
# @admin.register(Cust)
# class CustomerModelAdmin(admin.ModelAdmin):
#     list_display = ['id','user','locality']
    
# admin.site.register(Cust)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality', 'city','state','zipcode']