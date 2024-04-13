# All necessary imports for admin registration.
from django.contrib import admin

# Importing all necessary components from this app.
from .models import CarModel

#-----------------------------------------------------------------------------------------------------------------------

# Register your models here.
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'vin_number', 'registration_number', 'tuv_expire_date',)
    list_filter = ('brand', 'model', 'vin_number', 'registration_number',)

admin.site.register(CarModel, CarModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------
