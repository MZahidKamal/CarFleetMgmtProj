# All necessary imports for admin registration.
from django.contrib import admin

# Importing all necessary components from this app.
from .models import DeliveryAgentModel

#-----------------------------------------------------------------------------------------------------------------------

# Register your models here.
class DeliveryAgentModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth',)

    @staticmethod
    def full_name(self):
        return f'{self.personal_info.first_name} {self.personal_info.last_name}'

    @staticmethod
    def date_of_birth(self):
        return f'{self.personal_info.date_of_birth}'

admin.site.register(DeliveryAgentModel, DeliveryAgentModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------
