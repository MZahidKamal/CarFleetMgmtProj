# All necessary imports for admin registration.
from django.contrib import admin

# Importing all necessary components from this app.
from .models import CarDealerModel

#-----------------------------------------------------------------------------------------------------------------------

# Register your models here.
class CarDealerModelAdmin(admin.ModelAdmin):
    list_display = ('company_name',)

    @staticmethod
    def company_name(self):
        return self.company_info.name

admin.site.register(CarDealerModel, CarDealerModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------
