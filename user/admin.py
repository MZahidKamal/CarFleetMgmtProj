from django.contrib import admin
from .models import (CustomUserModel,
                     ManufacturerAccountModel,
                     CarDealerAccountModel,
                     DeliveryAgentAccountModel,
                     CustomerAccountModel,)

#-----------------------------------------------------------------------------------------------------------------------

# Register your models here.
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'date_joined', 'last_login', ]

admin.site.register(CustomUserModel, CustomUserModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class ManufacturerAccountModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'date_joined', 'last_login', ]

admin.site.register(ManufacturerAccountModel, ManufacturerAccountModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class CarDealerAccountModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'date_joined', 'last_login', ]

admin.site.register(CarDealerAccountModel, CarDealerAccountModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class DeliveryAgentAccountModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'date_joined', 'last_login', ]

admin.site.register(DeliveryAgentAccountModel, DeliveryAgentAccountModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class CustomerAccountModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'date_joined', 'last_login', ]

admin.site.register(CustomerAccountModel, CustomerAccountModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------
"""
In this model I can do some experiment and will do so, but in the next tab I will have to write some test codes for this
models. This is the only way I can regain the expertise of software testing, otherwise I will forget this skill set. For
the unit test I a using PyTest and for the frontend, I will be using Selenium.
"""
