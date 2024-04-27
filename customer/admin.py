# All necessary imports for admin registration.
from django.contrib import admin

# Importing all necessary components from this app.
from .models import PersonalDocumentsModel, CustomerModel

#-----------------------------------------------------------------------------------------------------------------------

# Register your models here.
class PersonalDocumentsModelAdmin(admin.ModelAdmin):
    list_display = ('cr_number', 'full_name', 'custom_last_updated')

    def cr_number(self, obj):
        return obj.customer.cr_number
    cr_number.short_description = 'Customer Number'

    @staticmethod
    def full_name(self):
        if self.customer.personal_info:
            return f'{self.customer.personal_info.first_name} {self.customer.personal_info.last_name}'
        else:
            return None

    def custom_last_updated(self, obj):
        return f'{obj.last_updated.strftime("%d %B %Y")} at {obj.last_updated.strftime("%H:%M")}'
    custom_last_updated.short_description = 'Last Updated On'

admin.site.register(PersonalDocumentsModel, PersonalDocumentsModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('cr_number', 'full_name', 'eligibility_check', 'custom_created_on')

    @staticmethod
    def full_name(self):
        if self.personal_info:
            return f'{self.personal_info.first_name} {self.personal_info.last_name}'
        else:
            return None

    def custom_created_on(self, obj):
        return f'{obj.created_on.strftime("%d %B %Y")} at {obj.created_on.strftime("%H:%M")}'
    custom_created_on.short_description = 'Created On'

admin.site.register(CustomerModel, CustomerModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------
