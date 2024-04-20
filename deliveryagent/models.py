# All necessary imports for creating models.
from django.db import models

# Importing all necessary components from this app.
from stationery.models import PersonModel

#-----------------------------------------------------------------------------------------------------------------------

class DeliveryAgentModel(models.Model):
    personal_info = models.ForeignKey(PersonModel, on_delete=models.CASCADE, verbose_name="Personal Info")

    def related_wo_history(self):
        return self.workordersmodel_set.filter(delivery_agent=self)
    # It will return only the work orders related to this delivery agent. Don't do circular import.

    def __str__(self):
        return f"{self.personal_info.first_name} {self.personal_info.last_name}"

#-----------------------------------------------------------------------------------------------------------------------
