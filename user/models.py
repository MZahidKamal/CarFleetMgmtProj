from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Necessary imports for Token Authentication.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .constants import CHOICES_UR
from manufacturer.models import ManufacturerModel
from cardealer.models import CarDealerModel
from deliveryagent.models import DeliveryAgentModel
from customer.models import CustomerModel

#-----------------------------------------------------------------------------------------------------------------------
# Create your models here.
class CustomUserModel(AbstractUser):
    user_role = models.CharField(max_length=15, choices=CHOICES_UR, verbose_name='User Role')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

#-----------------------------------------------------------------------------------------------------------------------

class ManufacturerAccountModel(CustomUserModel):
    manufacturer_info = models.OneToOneField(ManufacturerModel, on_delete=models.CASCADE, verbose_name="Manufacturer Info")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Manufacturer Account'
        verbose_name_plural = 'Manufacturer Accounts'

@receiver(post_save, sender=ManufacturerAccountModel)
def create_manufacturer_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# As soon as an instance of ManufacturerAccountModel will be created, a Token will also be generated associating the instance and
# will be saved in the database.

#-----------------------------------------------------------------------------------------------------------------------
class CarDealerAccountModel(CustomUserModel):
    car_dealer_info = models.OneToOneField(CarDealerModel, on_delete=models.CASCADE, verbose_name="Car Dealer Info")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Car Dealer Account'
        verbose_name_plural = 'Car Dealers Accounts'

@receiver(post_save, sender=CarDealerAccountModel)
def create_car_dealer_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# As soon as an instance of CarDealerAccountModel will be created, a Token will also be generated associating the instance and
# will be saved in the database.

#-----------------------------------------------------------------------------------------------------------------------

class DeliveryAgentAccountModel(CustomUserModel):
    delivery_agent_info = models.OneToOneField(DeliveryAgentModel, on_delete=models.CASCADE, verbose_name="Delivery Agent Info")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Delivery Agent Account'
        verbose_name_plural = 'Delivery Agents Accounts'

@receiver(post_save, sender=DeliveryAgentAccountModel)
def create_delivery_agent_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# As soon as an instance of DeliveryAgentAccountModel will be created, a Token will also be generated associating the instance and
# will be saved in the database.

#-----------------------------------------------------------------------------------------------------------------------

class CustomerAccountModel(CustomUserModel):
    customer_info = models.OneToOneField(CustomerModel, on_delete=models.CASCADE, verbose_name="Customer Info")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Customer Account'
        verbose_name_plural = 'Customer Accounts'

@receiver(post_save, sender=CustomerAccountModel)
def create_customer_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# As soon as an instance of CustomerAccountModel will be created, a Token will also be generated associating the instance and
# will be saved in the database.

#-----------------------------------------------------------------------------------------------------------------------
