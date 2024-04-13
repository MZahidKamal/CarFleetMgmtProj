# All necessary imports for admin registration.
from django.contrib import admin

# Importing all necessary components from this app.
from .models import CarExpensesModel, OverheadExpensesModel, WorkOrdersModel

#-----------------------------------------------------------------------------------------------------------------------

# Register your models here.
class CarExpensesModelAdmin(admin.ModelAdmin):
    list_display = ('expense_type', 'amount', 'custom_created_on',)
    list_filter = ('expense_type', 'created_on',)

    @staticmethod
    def custom_created_on(obj):
        return obj.created_on.strftime("%d-%m-%Y %H:%M")

admin.site.register(CarExpensesModel, CarExpensesModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class OverheadExpensesModelAdmin(admin.ModelAdmin):
    list_display = ('expense_type', 'amount', 'custom_created_on',)
    list_filter = ('expense_type', 'created_on',)

    @staticmethod
    def custom_created_on(obj):
        return obj.created_on.strftime("%d-%m-%Y %H:%M")

admin.site.register(OverheadExpensesModel, OverheadExpensesModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------

class WorkOrdersModelAdmin(admin.ModelAdmin):
    list_display = ('wo_number', 'custom_created_on',)
    list_filter = ('created_on',)

    @staticmethod
    def custom_created_on(obj):
        return obj.created_on.strftime("%d-%m-%Y %H:%M")

admin.site.register(WorkOrdersModel, WorkOrdersModelAdmin)

#-----------------------------------------------------------------------------------------------------------------------
