# All necessary imports for creating models.
from django.db import models

# Importing all necessary components from this app.
from stationery.models import CompanyModel
from cardealer.models import CarDealerModel
from deliveryagent.models import DeliveryAgentModel

#-----------------------------------------------------------------------------------------------------------------------

class ManufacturerModel(models.Model):
    company_info = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, verbose_name="Company Info")

    def car_collection(self):
        return self.carmodel_set.filter(brand=self)
    # It will return all cars of this manufacturer. Don't do circular import.

    @staticmethod
    def car_dealer_collection():
        return CarDealerModel.objects.all()
    # It will return all car dealers of this manufacturer. Don't do circular import.

    @staticmethod
    def delivery_agent_collection():
        return DeliveryAgentModel.objects.all()
    # It will return all delivery agents of this manufacturer. Don't do circular import.

    def workorder_collection(self):
        return self.workordersmodel_set.all()
    # It will return all work orders of this manufacturer. Don't do circular import.

    def __str__(self):
        return self.company_info.name

#-----------------------------------------------------------------------------------------------------------------------
