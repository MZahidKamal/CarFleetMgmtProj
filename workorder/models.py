# All necessary imports for creating models.
from django.db import models
import random

# Importing all necessary components from this app.
from .constants import *
from vehiclecondition.models import CarReceivingVCModel, CarGivingVCModel

#-----------------------------------------------------------------------------------------------------------------------

class CarExpensesModel(models.Model):
    expense_type = models.CharField(max_length=14, choices=CHOICES_CE, verbose_name="Expense Type")
    amount = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Amount")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created on")
    payment_method = models.CharField(max_length=14, choices=CHOICES_PM, verbose_name="Payment Method")
    receipt_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name="Receipt Image")

    def __str__(self):
        return f"{self.expense_type} - {self.amount} - {self.payment_method} - {self.created_on}"

#-----------------------------------------------------------------------------------------------------------------------

class OverheadExpensesModel(models.Model):
    expense_type = models.CharField(max_length=17, choices=CHOICES_OE, verbose_name="Expense Type")
    amount = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Amount")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created on")
    payment_method = models.CharField(max_length=14, choices=CHOICES_PM, verbose_name="Payment Method")
    receipt_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name="Receipt Image")

    def __str__(self):
        return f"{self.expense_type} - {self.amount} - {self.payment_method} - {self.created_on}"

#-----------------------------------------------------------------------------------------------------------------------

class WorkOrdersModel(models.Model):
    wo_number = models.CharField(max_length=25, unique=True, editable=False, verbose_name="Work Order Number")
    type = models.CharField(max_length=12, choices=CHOICES_WOT, default='CAR DELIVERY', verbose_name="Work Order Type")
    car = models.CharField(max_length=50, verbose_name="Car")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created On")

    status = models.CharField(max_length=21, choices=CHOICES_ST, default='PENDING', verbose_name="Work Order Status")
    delivery_date = models.DateField(verbose_name="Delivery Date", null=True, blank=True)

    car_dealer = models.CharField(max_length=50, verbose_name="Car Dealer")
    customer = models.CharField(max_length=100, verbose_name="Customer")
    delivery_agent = models.CharField(max_length=50, verbose_name="Delivery Agent")

    car_receiving_vc = models.ForeignKey(CarReceivingVCModel, on_delete=models.CASCADE, verbose_name="Car Receiving VC", null=True, blank=True)
    car_giving_vc = models.ForeignKey(CarGivingVCModel, on_delete=models.CASCADE, verbose_name="Car Giving VC", null=True, blank=True)

    car_expenses = models.ForeignKey(CarExpensesModel, on_delete=models.CASCADE, verbose_name="Car Expenses", null=True, blank=True)
    overhead_expenses = models.ForeignKey(OverheadExpensesModel, on_delete=models.CASCADE, verbose_name="Overhead Expenses", null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.wo_number:
            self.wo_number = f"WO{random.randint(100000, 999999)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.wo_number} - {self.type} - {self.car} - {self.created_on}"

#-----------------------------------------------------------------------------------------------------------------------
