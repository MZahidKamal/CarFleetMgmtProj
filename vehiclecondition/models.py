# All necessary imports for creating models.
from django.db import models
from datetime import datetime

# Importing all necessary components from this app.
from .constants import *

#-----------------------------------------------------------------------------------------------------------------------

# Creating a proofimages model, so that it can be inherited from the vehicle condition models.
class ProofImagesModel(models.Model):
    vin_number_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='VIN Image', null=True, blank=True)
    license_plate_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='License Plate Image', null=True, blank=True)
    emission_sticker_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='Emission Sticker Image', null=True, blank=True)
    registration_certificate_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='Registration Certificate Image', null=True, blank=True)
    dashboard_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='Dashboard Image', null=True, blank=True)
    front_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='Front Image', null=True, blank=True)
    left_front_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='Left Front Image', null=True, blank=True)
    left_rear_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='Left Rear Image', null=True, blank=True)
    rear_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='Rear Image', null=True, blank=True)
    right_rear_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='Right Rear Image', null=True, blank=True)
    right_front_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='Right Front Image', null=True, blank=True)
    key_set_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='Key Set Image', null=True, blank=True)
    boot_accessories_image = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='Boot Accessories Image', null=True, blank=True)

    def __str__(self):
        return f"General Images : Vehicle Condition : ID-{self.id}"

#-----------------------------------------------------------------------------------------------------------------------

# Creating a vehicle condition model, so that it can be inherited from the car receiving/delivering VC models.
class VehicleConditionModel(models.Model):
    vin_number = models.CharField(max_length=25, verbose_name='VIN')
    registration_number = models.CharField(max_length=25, verbose_name='Registration Number')
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
    proof_images = models.ForeignKey(ProofImagesModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.vin_number}, {self.registration_number}, {self.mileage}'

#-----------------------------------------------------------------------------------------------------------------------

# Creating a car receiving VC model, so that it can be created along with the workorder model from workorder app.
class CarReceivingVCModel(models.Model):
    vehicle_condition = models.ForeignKey(VehicleConditionModel, on_delete=models.SET_NULL, null=True, blank=True)
    receiving_from = models.CharField(max_length=50, verbose_name='Receiving From', null=True, blank=True)
    created_on = models.DateField(auto_now_add=True, verbose_name='Date and Time', null=True, blank=True)
    location = models.CharField(max_length=50, verbose_name='Location', null=True, blank=True)
    # e_signature = models.CharField(max_length=50, verbose_name='Signature', null=True, blank=True)
    e_signature = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='E-Signature', null=True, blank=True)

    def __str__(self):
        return f'{self.receiving_from}, {self.created_on}'

#-----------------------------------------------------------------------------------------------------------------------

# Creating a car receiving VC model, so that it can be created along with the workorder model from workorder app.
class CarGivingVCModel(models.Model):
    vehicle_condition = models.ForeignKey(VehicleConditionModel, on_delete=models.SET_NULL, null=True, blank=True)
    giving_to = models.CharField(max_length=50, verbose_name='Giving To', null=True, blank=True)
    created_on = models.DateField(auto_now_add=True, verbose_name='Date and Time', null=True, blank=True)
    location = models.CharField(max_length=50, verbose_name='Location', null=True, blank=True)
    e_signature = models.ImageField(upload_to='workorder/%Y-%m-%d-%H-%M-%S/', verbose_name='E-Signature', null=True, blank=True)

    def __str__(self):
        return f'{self.giving_to}, {self.created_on}'

#-----------------------------------------------------------------------------------------------------------------------
