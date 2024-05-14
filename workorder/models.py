# All necessary imports for creating models.
import uuid
import os
from django.db import models
from django.conf import settings
from datetime import datetime

# Importing all necessary components from this app.
from .constants import *
from manufacturer.models import ManufacturerModel
from car.models import CarModel
from cardealer.models import CarDealerModel
from customer.models import CustomerModel
from deliveryagent.models import DeliveryAgentModel

#-----------------------------------------------------------------------------------------------------------------------

def this_wo_vc_folder_path(instance, filename):
    safe_filename = os.path.basename(filename)
    if not instance.workorder.car_receiving_vc and not instance.workorder.car_giving_vc:
        return os.path.join('workorder', instance.workorder.wo_number, 'car_receiving_vc', safe_filename)
    elif instance.workorder.car_receiving_vc and not instance.workorder.car_giving_vc:
        return os.path.join('workorder', instance.workorder.wo_number, 'car_giving_vc', safe_filename)
    # File will be uploaded to MEDIA_ROOT/workorder/<wo_number>/<respective_vc>/e_signature/<filename>

class ProofImagesModel(models.Model):
    workorder = models.ForeignKey('WorkOrdersModel', on_delete=models.CASCADE, null=True, blank=True)
    vin_number_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='VIN Image')
    license_plate_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='License Plate Image')
    emission_sticker_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='Emission Sticker Image')
    registration_certificate_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='Registration Certificate Image')
    dashboard_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='Dashboard Image')
    front_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='Front Image')
    left_front_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='Left Front Image')
    left_rear_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='Left Rear Image')
    rear_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='Rear Image')
    right_rear_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='Right Rear Image')
    right_front_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='Right Front Image')
    key_set_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='Key Set Image')
    boot_accessories_image = models.ImageField(upload_to=this_wo_vc_folder_path, verbose_name='Boot Accessories Image')

    def __str__(self):
        return f'{self.workorder.wo_number} - {self.workorder.created_on.strftime("%d %B %Y")}'

    # TODO: Convert images to binary and then save into database (without folder structure) in order to save space.

    class Meta:
        verbose_name = 'Proof Image'
        verbose_name_plural = 'Proof Images'

#-----------------------------------------------------------------------------------------------------------------------

# Creating a vehicle condition model, so that it can be inherited from the car receiving/delivering VC models.
class VehicleConditionModel(models.Model):
    workorder = models.ForeignKey('WorkOrdersModel', on_delete=models.CASCADE, null=True, blank=True)
    vin_number = models.CharField(max_length=25, verbose_name='VIN')
    registration_number = models.CharField(max_length=10, verbose_name='Registration Number')
    mileage = models.IntegerField(verbose_name='Mileage')
    fuel_level = models.CharField(max_length=5, choices=CHOICES_FL, default='0/10', verbose_name='Fuel Level')
    main_keys = models.CharField(max_length=1, choices=CHOICES_MK, default='0', verbose_name='Main Keys')
    transponder_keys = models.CharField(max_length=1, choices=CHOICES_TK, default='0', verbose_name='Transponder Keys')
    registration_certificate = models.CharField(max_length=10, choices=CHOICES_RC, default='NO', verbose_name='Registration Certificate')
    first_aid_kit = models.CharField(max_length=3, choices=CHOICES_FAK, default='NO', verbose_name='First Aid Kit')
    high_visibility_waistcoat = models.CharField(max_length=3, choices=CHOICES_HVWC, default='NO', verbose_name='High Visibility Waistcoat')
    warning_triangle = models.CharField(max_length=3, choices=CHOICES_WT, default='NO', verbose_name='Warning Triangles')
    luggage_net = models.CharField(max_length=3, choices=CHOICES_LN, default='NO', verbose_name='Luggage Net')
    floor_mats = models.CharField(max_length=3, choices=CHOICES_FM, default='NO', verbose_name='Floor Mats')
    rear_boot_rubber_mat = models.CharField(max_length=3, choices=CHOICES_RBRM, default='NO', verbose_name='Rear Boot Rubber Mat')
    charging_cable_type2 = models.CharField(max_length=3, choices=CHOICES_CCT2, default='NO', verbose_name='Charging Cable Type2')
    charging_cable_schuko = models.CharField(max_length=3, choices=CHOICES_CCS, default='NO', verbose_name='Charging Cable Schuko')
    tyre_set = models.CharField(max_length=6, choices=CHOICES_TS, default='SUMMER', verbose_name='Tyre Set')
    tow_bar = models.CharField(max_length=3, choices=CHOICES_TB, default='NO', verbose_name='Tow Bar')
    proof_images = models.OneToOneField(ProofImagesModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.vin_number}, {self.registration_number}, {self.mileage}'

    class Meta:
        verbose_name = 'Vehicle Condition'
        verbose_name_plural = 'Vehicle Conditions'

#-----------------------------------------------------------------------------------------------------------------------

def this_wo_car_receiving_vc_folder_path(instance, filename):
    safe_filename = os.path.basename(filename)
    return os.path.join('workorder', instance.workorder.wo_number, 'car_receiving_vc/e_signature', safe_filename)
    # File will be uploaded to MEDIA_ROOT/workorder/<wo_number>/car_receiving_vc/e_signature/<filename>

class CarReceivingVCModel(models.Model):
    workorder = models.OneToOneField('WorkOrdersModel', on_delete=models.CASCADE, null=True, blank=True)
    vehicle_condition = models.OneToOneField(VehicleConditionModel, on_delete=models.SET_NULL, null=True, blank=True)
    receiving_from = models.CharField(max_length=50, verbose_name='Receiving From', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Date and Time', null=True, blank=True)
    location = models.CharField(max_length=50, verbose_name='Location', null=True, blank=True)
    e_signature = models.ImageField(upload_to=this_wo_car_receiving_vc_folder_path, verbose_name='E-Signature', null=True, blank=True)
    # TODO: Real e-signature feature need to be implemented.

    def __str__(self):
        return f'{self.receiving_from} -- {self.created_on.strftime("%d %B %Y")} -- {self.workorder.wo_number}'

    class Meta:
        verbose_name = 'CarReceiving VC'
        verbose_name_plural = 'CarReceiving VCs'

#-----------------------------------------------------------------------------------------------------------------------

def this_wo_car_giving_vc_folder_path(instance, filename):
    safe_filename = os.path.basename(filename)
    return os.path.join('workorder', instance.workorder.wo_number, 'car_giving_vc/e_signature', safe_filename)
    # File will be uploaded to MEDIA_ROOT/workorder/<wo_number>/car_giving_vc/e_signature/<filename>

class CarGivingVCModel(models.Model):
    workorder = models.OneToOneField('WorkOrdersModel', on_delete=models.CASCADE, null=True, blank=True)
    vehicle_condition = models.OneToOneField(VehicleConditionModel, on_delete=models.SET_NULL, null=True, blank=True)
    giving_to = models.CharField(max_length=50, verbose_name='Giving To', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Date and Time', null=True, blank=True)
    location = models.CharField(max_length=50, verbose_name='Location', null=True, blank=True)
    e_signature = models.ImageField(upload_to=this_wo_car_giving_vc_folder_path, verbose_name='E-Signature', null=True, blank=True)
    # TODO: Real e-signature feature need to be implemented.

    def __str__(self):
        return f'{self.giving_to} -- {self.created_on.strftime("%d %B %Y")} -- {self.workorder.wo_number}'

    class Meta:
        verbose_name = 'CarGiving VC'
        verbose_name_plural = 'CarGiving VCs'

#-----------------------------------------------------------------------------------------------------------------------

def this_wo_ce_folder_path(instance, filename):
    safe_filename = os.path.basename(filename)
    return os.path.join('workorder', instance.workorder.wo_number, 'car_expenses', safe_filename)
    # File will be uploaded to MEDIA_ROOT/workorder/<wo_number>/car_expenses/<filename>

class CarExpensesModel(models.Model):
    workorder = models.ForeignKey('WorkOrdersModel', on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=14, choices=CHOICES_CE, verbose_name="Expense Type")
    amount = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Amount")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created on")
    payment_method = models.CharField(max_length=14, choices=CHOICES_PM, verbose_name="Payment Method")
    receipt_image = models.ImageField(upload_to=this_wo_ce_folder_path, verbose_name="Receipt Image")
    # Car expenses documents need to be uploaded into the respective <wo_number> folder.

    def __str__(self):
        return f"{self.expense_type} -- {self.amount}€ -- {self.payment_method} -- {self.created_on.strftime("%d %B %Y")}"

    class Meta:
        verbose_name = 'CarExpenses'
        verbose_name_plural = 'CarExpenses'

#-----------------------------------------------------------------------------------------------------------------------

def this_wo_oe_folder_path(instance, filename):
    safe_filename = os.path.basename(filename)
    return os.path.join('workorder', instance.workorder.wo_number, 'overhead_expenses', safe_filename)
    # File will be uploaded to MEDIA_ROOT/workorder/<wo_number>/overhead_expenses/<filename>

class OverheadExpensesModel(models.Model):
    workorder = models.ForeignKey('WorkOrdersModel', on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=17, choices=CHOICES_OE, verbose_name="Expense Type")
    amount = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Amount")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Created on")
    payment_method = models.CharField(max_length=14, choices=CHOICES_PM, verbose_name="Payment Method")
    receipt_image = models.ImageField(upload_to=this_wo_oe_folder_path, verbose_name="Receipt Image")
    # Overhead expenses documents/images need to be uploaded into the respective <wo_number> folder.

    def __str__(self):
        return f"{self.expense_type} -- {self.amount}€ -- {self.payment_method} -- {self.created_on.strftime("%d %B %Y")}"

    class Meta:
        verbose_name = 'Overhead Expenses'
        verbose_name_plural = 'Overhead Expenses'

#-----------------------------------------------------------------------------------------------------------------------

class WorkOrdersModel(models.Model):
    wo_number = models.CharField(max_length=10, unique=True, editable=False, verbose_name="Work Order Number")
    type = models.CharField(max_length=12, choices=CHOICES_WOT, default='CAR DELIVERY', verbose_name="Work Order Type")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Work Order Created On")
    status = models.CharField(max_length=21, choices=CHOICES_ST, default='PENDING', verbose_name="Work Order Status")

    manufacturer = models.ForeignKey(ManufacturerModel, on_delete=models.CASCADE, verbose_name="Manufacturer", null=True, blank=True,)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name="Car", null=True, blank=True,)

    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, verbose_name="Customer", null=True, blank=True,)
    car_dealer = models.ForeignKey(CarDealerModel, on_delete=models.CASCADE, verbose_name="Car Dealer", null=True, blank=True,)
    delivery_agent = models.ForeignKey(DeliveryAgentModel, on_delete=models.CASCADE, verbose_name="Delivery Agent", null=True, blank=True,)

    delivery_date = models.DateField(verbose_name="Delivery Date", null=True, blank=True)

    car_receiving_vc = models.OneToOneField(CarReceivingVCModel, on_delete=models.CASCADE, verbose_name="Car Receiving VC", related_name='workordersmodel', null=True, blank=True)
    car_giving_vc = models.OneToOneField(CarGivingVCModel, on_delete=models.CASCADE, verbose_name="Car Giving VC", null=True, blank=True)
    car_expenses = models.OneToOneField(CarExpensesModel, on_delete=models.CASCADE, verbose_name="Car Expenses", related_name='workordersmodel', null=True, blank=True)
    # Car expenses documents need to be uploaded into the respective <wo_number> folder.
    overhead_expenses = models.OneToOneField(OverheadExpensesModel, on_delete=models.CASCADE, verbose_name="Overhead Expenses", null=True, blank=True)
    # Overhead expenses documents need to be uploaded into the respective <wo_number> folder.

    # Overriding the model's 'save' method.
    def save(self, *args, **kwargs):

        # Dynamically creating a WO number and saving it in this model's instance.
        if not self.wo_number:
            self.wo_number = f"WO{str(uuid.uuid4().int)[:8]}"

            # Creating a folder with the WO number to save all relevant media files.
            path = os.path.join(settings.MEDIA_ROOT, 'workorder', self.wo_number)
            if not os.path.exists(path):
                os.makedirs(path)

        # TODO: Status will change automatically with the progress of field completion.

        # As soon as all fields will be completed, modification of this instance will no more be possible.
        if self.wo_number and self.type and self.created_on and self.status and self.manufacturer and self.car and self.customer and self.car_dealer and self.delivery_agent and self.delivery_date and self.car_receiving_vc and self.car_giving_vc:
            self.is_read_only = True

        super().save(*args, **kwargs)

    # Overriding the model's 'delete' method.
    def delete(self, *args, **kwargs):
        if self.is_read_only:
            raise PermissionError("This work order is read-only and cannot be deleted.")
        else:
            super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.wo_number} - {self.type.capitalize()}"

    class Meta:
        verbose_name = 'Work Order'
        verbose_name_plural = 'Work Orders'

#-----------------------------------------------------------------------------------------------------------------------
