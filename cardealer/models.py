# All necessary imports for creating models.
from django.db import models

# Importing all necessary components from this app.
from stationery.models import CompanyModel
from workorder.models import WorkOrdersModel

#-----------------------------------------------------------------------------------------------------------------------

class CarDealerModel(models.Model):
    company_info = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, verbose_name="Company Info")

    def related_wo_history(self):
        return WorkOrdersModel.objects.filter(car_dealer=self)
    # It will return only the workorder objects related to this car dealer.

    def __str__(self):
        return self.company_info.name

#-----------------------------------------------------------------------------------------------------------------------
