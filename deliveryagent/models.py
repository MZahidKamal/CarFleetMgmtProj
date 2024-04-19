# All necessary imports for creating models.
from django.db import models

# Importing all necessary components from this app.
from stationery.models import PersonModel
from workorder.models import WorkOrdersModel

#-----------------------------------------------------------------------------------------------------------------------

class DeliveryAgentModel(models.Model):
    personal_info = models.ForeignKey(PersonModel, on_delete=models.CASCADE, verbose_name="Personal Info")
    # wo_history = models.ForeignKey(WorkOrdersModel, on_delete=models.CASCADE, verbose_name="Work Orders History")

    def related_wo_history(self):
        return WorkOrdersModel.objects.filter(delivery_agent=self.personal_info)
    # It will return only the workorder objects related to this delivery agent.

    def __str__(self):
        return f"{self.personal_info.first_name} {self.personal_info.last_name} - {self.personal_info.date_of_birth}"

#-----------------------------------------------------------------------------------------------------------------------
