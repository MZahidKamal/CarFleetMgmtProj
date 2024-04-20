# All necessary imports for admin registration.
from django.contrib import admin

# Importing all necessary components from this app.
from .models import ManufacturerModel

#-----------------------------------------------------------------------------------------------------------------------

# Register your models here.
class ManufacturerModelAdmin(admin.ModelAdmin):
    list_display = ('company_name',)

    @staticmethod
    def company_name(self):
        return self.company_info.name

admin.site.register(ManufacturerModel, ManufacturerModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------
