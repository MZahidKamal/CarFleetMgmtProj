# All necessary imports for creating models.
from django.db import models
import random

# Importing all necessary components from this app.
from .constants import *
from manufacturer.models import ManufacturerModel

#-----------------------------------------------------------------------------------------------------------------------

class CarModel(models.Model):
    brand = models.ForeignKey(ManufacturerModel, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Brand')
    model = models.CharField(max_length=25, verbose_name="Model")
    color = models.CharField(max_length=5, choices=CHOICES_COLOR, verbose_name="Color")
    vin_number = models.CharField(max_length=25, unique=True, null=False, blank=False, verbose_name="VIN Number")
    registration_number = models.CharField(max_length=10, null=False, blank=False, verbose_name='Registration Number')
    tuv_expire_date = models.DateField(null=False, blank=False, verbose_name="Tuv Expire Date")

    def related_wo_history(self):
        return self.workordersmodel_set.filter(car=self)
    # It will return only the work orders related to this car. Don't do circular import.

    def __str__(self):
        return f"{self.model} - {self.vin_number} - {self.registration_number} - {self.tuv_expire_date}"

#-----------------------------------------------------------------------------------------------------------------------
