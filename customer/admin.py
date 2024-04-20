# All necessary imports for admin registration.
from django.contrib import admin

# Importing all necessary components from this app.
from .models import CustomerModel

#-----------------------------------------------------------------------------------------------------------------------

# Register your models here.
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'eligibility_check')

    @staticmethod
    def full_name(self):
        return f'{self.personal_info.first_name} {self.personal_info.last_name}'

admin.site.register(CustomerModel, CustomerModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------
