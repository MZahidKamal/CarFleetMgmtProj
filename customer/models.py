# All necessary imports for creating models.
import uuid
import os

from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

# Importing all necessary components from this app.
from .constants import *
from stationery.models import PersonModel

#-----------------------------------------------------------------------------------------------------------------------

def this_cr_folder_path(instance, filename):
    safe_filename = os.path.basename(filename)
    return os.path.join('customer', instance.customer.cr_number, 'personal_documents', safe_filename)
    # File will be uploaded to MEDIA_ROOT/customer/<cr_number>/personal_documents/<filename>

class PersonalDocumentsModel(models.Model):
    customer = models.OneToOneField('CustomerModel', on_delete=models.CASCADE)
    passport_pdf = models.FileField(upload_to=this_cr_folder_path, validators=[FileExtensionValidator(['pdf'])], verbose_name='Passport Copy')
    residence_permit_pdf = models.FileField(upload_to=this_cr_folder_path, validators=[FileExtensionValidator(['pdf'])], verbose_name='Residence Permit Copy')
    schufa_score_pdf = models.FileField(upload_to=this_cr_folder_path, validators=[FileExtensionValidator(['pdf'])], verbose_name='Schufa Score Copy')
    driving_license_pdf = models.FileField(upload_to=this_cr_folder_path, validators=[FileExtensionValidator(['pdf'])], verbose_name='Driving License Copy')
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    def __str__(self):
        return f"{self.customer.cr_number} -- {self.customer.personal_info.first_name} {self.customer.personal_info.last_name} -- {self.last_updated.strftime("%d %B %Y")}"

    class Meta:
        verbose_name = 'Personal Document'
        verbose_name_plural = 'Personal Documents'

#-----------------------------------------------------------------------------------------------------------------------

class CustomerModel(models.Model):
    cr_number = models.CharField(max_length=8, unique=True, editable=False, verbose_name="Customer Number")
    personal_info = models.ForeignKey(PersonModel, on_delete=models.CASCADE, verbose_name="Personal Info")
    personal_documents = models.OneToOneField(PersonalDocumentsModel, on_delete=models.CASCADE, verbose_name="Personal Documents", related_name='personal_documents', null=True, blank=True)
    eligibility_check = models.CharField(max_length=7, choices=CHOICES_EC, default='PENDING', verbose_name="Eligibility Check")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Customer Created On")

    # Overriding the model's 'save' method.
    def save(self, *args, **kwargs):

        # Dynamically creating a CR number and saving it in this model's instance.
        if not self.cr_number:
            self.cr_number = f"CR{str(uuid.uuid4().int)[:6]}"

            # Creating a folder with the CR number to save all relevant media files.
            path = os.path.join(settings.MEDIA_ROOT, 'customer', self.cr_number)
            if not os.path.exists(path):
                os.makedirs(path)

        super().save(*args, **kwargs)

    def related_wo_history(self):
        return self.workordersmodel_set.filter(customer=self)
    # It will return only the work orders related to this customer. Don't do circular import.

    def __str__(self):
        if self.personal_info:
            return f"{self.cr_number} -- {self.personal_info.first_name} {self.personal_info.last_name} -- {self.created_on.strftime("%d %B %Y")}"
        else:
            return f"{self.cr_number} -- {self.created_on.strftime("%d %B %Y")}"

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

#-----------------------------------------------------------------------------------------------------------------------
