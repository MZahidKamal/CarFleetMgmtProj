# All necessary imports for models.
from django.db import models

# All database models import from the stationery app.
from stationery.models import *

#-----------------------------------------------------------------------------------------------------------------------

# Create your models here.
# class Manufacturer(models.Model):
#     company_info = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, related_name='manufacturer')
#     car_collections = models.ManyToManyField()
