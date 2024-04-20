# All necessary imports for creating models.
from django.db import models

# Importing all necessary components from this app.
from stationery.models import CompanyModel
from car.models import CarModel
from cardealer.models import CarDealerModel
from deliveryagent.models import DeliveryAgentModel
from workorder.models import WorkOrdersModel

#-----------------------------------------------------------------------------------------------------------------------

class ManufacturerModel(models.Model):
    company_info = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, verbose_name="Company Info")

    @staticmethod
    def related_cars():
        return CarModel.objects.all()
    # It will return all car related to this manufacturer.

    @staticmethod
    def related_car_dealers():
        return CarDealerModel.objects.all()
    # It will return all car dealers related to this manufacturer.

    @staticmethod
    def related_delivery_agents():
        return DeliveryAgentModel.objects.all()
    # It will return all delivery agents related to this manufacturer.

    @staticmethod
    def related_wo_history():
        return WorkOrdersModel.objects.all()
    # It will return all work orders related to this manufacturer.

    def __str__(self):
        return self.company_info.name

#-----------------------------------------------------------------------------------------------------------------------
