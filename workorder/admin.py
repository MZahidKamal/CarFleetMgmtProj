# All necessary imports for admin registration.
from django.contrib import admin

# Importing all necessary components from this app.
from .models import (ProofImagesModel,
                     VehicleConditionModel,
                     CarReceivingVCModel,
                     CarGivingVCModel,
                     CarExpensesModel,
                     OverheadExpensesModel,
                     WorkOrdersModel)

#-----------------------------------------------------------------------------------------------------------------------

# Registering all models here.
class ProofImagesModelAdmin(admin.ModelAdmin):
    list_display = ('wo_number', 'created_on',)

    def wo_number(self, obj):
        return obj.workorder.wo_number
    wo_number.short_description = 'Work Order Number'

    def created_on(self, obj):
        if obj.vehicleconditionmodel.carreceivingvcmodel:
            return obj.vehicleconditionmodel.carreceivingvcmodel.created_on
        elif obj.vehicleconditionmodel.cargivingvcmodel:
            return obj.vehicleconditionmodel.cargivingvcmodel.created_on
        else:
            return None
    created_on.short_description = 'Created On'

admin.site.register(ProofImagesModel, ProofImagesModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class VehicleConditionModelAdmin(admin.ModelAdmin):
    list_display = ('wo_number', 'created_on',)

    def wo_number(self, obj):
        return obj.workorder.wo_number
    wo_number.short_description = 'Work Order Number'

    def created_on(self, obj):
        if obj.carreceivingvcmodel:
            return obj.carreceivingvcmodel.created_on.strftime("%d %B %Y")
        elif obj.cargivingvcmodel:
            return obj.cargivingvcmodel.created_on.strftime("%d %B %Y")
        else:
            return None
    created_on.short_description = 'Created On'

admin.site.register(VehicleConditionModel, VehicleConditionModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class CarReceivingVCModelAdmin(admin.ModelAdmin):
    list_display = ('wo_number', 'custom_created_on')
    list_filter = ('created_on',)

    def wo_number(self, obj):
        return obj.workorder.wo_number
    wo_number.short_description = 'Work Order Number'

    @staticmethod
    def custom_created_on(obj):
        return f'{obj.created_on.strftime("%d %B %Y")} at {obj.created_on.strftime("%H:%M")}'

admin.site.register(CarReceivingVCModel, CarReceivingVCModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class CarGivingVCModelAdmin(admin.ModelAdmin):
    list_display = ('wo_number', 'custom_created_on')
    list_filter = ('created_on',)

    def wo_number(self, obj):
        return obj.workorder.wo_number
    wo_number.short_description = 'Work Order Number'

    @staticmethod
    def custom_created_on(obj):
        return f'{obj.created_on.strftime("%d %B %Y")} at {obj.created_on.strftime("%H:%M")}'

admin.site.register(CarGivingVCModel, CarGivingVCModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class CarExpensesModelAdmin(admin.ModelAdmin):
    list_display = ('wo_number', 'expense_type', 'amount', 'custom_created_on',)
    list_filter = ('expense_type', 'created_on',)

    def wo_number(self, obj):
        return obj.workorder.wo_number
    wo_number.short_description = 'Work Order Number'

    @staticmethod
    def custom_created_on(obj):
        return f'{obj.created_on.strftime("%d %B %Y")} at {obj.created_on.strftime("%H:%M")}'

admin.site.register(CarExpensesModel, CarExpensesModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class OverheadExpensesModelAdmin(admin.ModelAdmin):
    list_display = ('wo_number', 'expense_type', 'amount', 'custom_created_on',)
    list_filter = ('expense_type', 'created_on',)

    def wo_number(self, obj):
        return obj.workorder.wo_number
    wo_number.short_description = 'Work Order Number'

    @staticmethod
    def custom_created_on(obj):
        return f'{obj.created_on.strftime("%d %B %Y")} at {obj.created_on.strftime("%H:%M")}'

admin.site.register(OverheadExpensesModel, OverheadExpensesModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class WorkOrdersModelAdmin(admin.ModelAdmin):
    list_display = ('wo_number', 'type', 'custom_created_on', 'receiving_from', 'giving_to',)
    list_filter = ('type', 'created_on',)

    def receiving_from(self, obj):
        return obj.car_receiving_vc.receiving_from if obj.car_receiving_vc else None
    receiving_from.short_description = 'Car Receiving From'

    def giving_to(self, obj):
        return obj.car_giving_vc.giving_to if obj.car_giving_vc else None
    giving_to.short_description = 'Car Giving To'

    def custom_created_on(self, obj):
        return f'{obj.created_on.strftime("%d %B %Y")} at {obj.created_on.strftime("%H:%M")}'
    custom_created_on.short_description = 'Created On'

admin.site.register(WorkOrdersModel, WorkOrdersModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------
