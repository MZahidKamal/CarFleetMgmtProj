# All necessary imports for creating models.
from django.db import models
import random
import uuid

# Importing all necessary components from this app.
from stationery.models import PersonModel

#-----------------------------------------------------------------------------------------------------------------------

class CustomerModel(models.Model):
    customer_number = models.CharField(max_length=8, unique=True, editable=False, verbose_name="Customer Number", null=True, blank=True,)
    personal_info = models.ForeignKey(PersonModel, on_delete=models.CASCADE, verbose_name="Personal Info")
    eligibility_check = models.BooleanField(verbose_name="Eligibility Check", default=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.customer_number:
            self.customer_number = f"CR{str(uuid.uuid4().int)[:6]}"
        super().save(*args, **kwargs)
    # Dynamically creating a Customer number and saving it in this model's instance.

    def related_wo_history(self):
        return self.workordersmodel_set.filter(customer=self)
    # It will return only the work orders related to this customer. Don't do circular import.

    def __str__(self):
        return f"{self.personal_info.first_name} {self.personal_info.last_name}"

#-----------------------------------------------------------------------------------------------------------------------
