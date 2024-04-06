# All necessary imports for admin registration.
from django.contrib import admin

# Importing all database models from this app.
from .models import AddressModel, PersonModel, EmployeeModel, CompanyModel

#-----------------------------------------------------------------------------------------------------------------------

# Registering all models here.
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ('street', 'house', 'zip_code', 'city', 'state', 'country',)
    list_filter = ('street', 'house', 'zip_code', 'city', 'state', 'country',)

admin.site.register(AddressModel, AddressModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'age', 'email_address',)
    list_filter = ('first_name', 'last_name', 'date_of_birth', 'email_address',)

admin.site.register(PersonModel, PersonModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'designation',)
    list_filter = ('designation',)

admin.site.register(EmployeeModel, EmployeeModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
    list_filter = ('name', 'address',)

admin.site.register(CompanyModel, CompanyModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------
