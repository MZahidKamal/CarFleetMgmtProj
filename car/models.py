# All necessary imports for creating models.
from django.db import models
import random

# Importing all necessary components from this app.
from .constants import *
from workorder.models import WorkOrdersModel

#-----------------------------------------------------------------------------------------------------------------------

class CarModel(models.Model):
    brand = models.CharField(max_length=25, verbose_name="Brand")
    model = models.CharField(max_length=25, verbose_name="Model")
    color = models.CharField(max_length=5, choices=CHOICES_COLOR, verbose_name="Color")
    vin_number = models.CharField(max_length=25, unique=True, null=False, blank=False, verbose_name="VIN Number")
    registration_number = models.CharField(max_length=10, null=False, blank=False, verbose_name='Registration Number')
    tuv_expire_date = models.DateField(null=False, blank=False, verbose_name="Tuv Expire Date")
    # wo_history = models.ForeignKey(WorkOrdersModel, on_delete=models.CASCADE, verbose_name="Work Orders History")

    def related_wo_history(self):
        return WorkOrdersModel.objects.filter(car_vin=self.vin_number)
    # This should return a queryset containing all the WorkOrdersModel instances associated with that car's VIN number.

    def __str__(self):
        return f"{self.brand} - {self.model} - {self.vin_number} - {self.registration_number} - {self.tuv_expire_date}"

#-----------------------------------------------------------------------------------------------------------------------
