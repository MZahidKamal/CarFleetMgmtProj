"""# All necessary imports for admin registration.
from django.contrib import admin

# Importing all database models from this app.
from .models import ProofImagesModel, VehicleConditionModel, CarReceivingVCModel, CarGivingVCModel

#-----------------------------------------------------------------------------------------------------------------------

# Registering all models here.
class ProofImagesModelAdmin(admin.ModelAdmin):
    list_display = ('proof_image_set_id',)
    list_filter = ('id',)

    @staticmethod
    def proof_image_set_id(self):
        return f'Proof Image Set ID No. {self.id}'

admin.site.register(ProofImagesModel, ProofImagesModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class VehicleConditionModelAdmin(admin.ModelAdmin):
    list_display = ('vin_number', 'registration_number', 'mileage',)
    list_filter = ('vin_number', 'registration_number',)

admin.site.register(VehicleConditionModel, VehicleConditionModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class CarReceivingVCModelAdmin(admin.ModelAdmin):
    list_display = ('receiving_from', 'created_on')
    list_filter = ('created_on',)

admin.site.register(CarReceivingVCModel, CarReceivingVCModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class CarGivingVCModelAdmin(admin.ModelAdmin):
    list_display = ('giving_to', 'created_on')
    list_filter = ('created_on',)

admin.site.register(CarGivingVCModel, CarGivingVCModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------
"""