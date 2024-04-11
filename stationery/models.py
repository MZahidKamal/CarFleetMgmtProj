# All necessary imports for creating models.
from django.db import models
from datetime import date

#-----------------------------------------------------------------------------------------------------------------------

# Creating an address model, so that it can be inherited from anywhere of this project.
class AddressModel(models.Model):
    street = models.CharField(max_length=100, verbose_name="Street")
    house = models.CharField(max_length=15, verbose_name="House")
    zip_code = models.CharField(max_length=10, verbose_name="ZIP")
    city = models.CharField(max_length=200, verbose_name="City")
    state = models.CharField(max_length=25, verbose_name="State")
    country = models.CharField(max_length=25, verbose_name="Country")

    def __str__(self):
        return f"{self.street} {self.house}, {self.zip_code} {self.city}, {self.state}, {self.country}"
    # The __str__() method in a Django model is used to define the representation of the object information in the admin
    # interfaces or elsewhere in the application.

#-----------------------------------------------------------------------------------------------------------------------

# Creating a person model, so that it can be inherited from anywhere of this project.
class PersonModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth", null=True, blank=True)
    email_address = models.EmailField(max_length=100, unique=True, verbose_name="Email Address")
    phone_number = models.CharField(max_length=50, unique=True, verbose_name="Phone Number")
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def age(self):
        if self.date_of_birth:
            return (date.today() - self.date_of_birth).days // 365
        else:
            return None
    # The @property decorator in a Django model allows you to create a read-only attribute that behaves like a regular
    # property but is calculated dynamically based on other attributes or methods in the model.

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#-----------------------------------------------------------------------------------------------------------------------

# Creating an employee model, so that it can be inherited from anywhere of this project.
class EmployeeModel(models.Model):
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE, null=True, blank=True)
    designation = models.CharField(max_length=100, verbose_name="Designation")

    @property
    def full_name(self):
        return f"{self.person.first_name} {self.person.last_name}"

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name}"

#-----------------------------------------------------------------------------------------------------------------------

# Creating a company model, so that it can be inherited from anywhere of this project.
class CompanyModel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Company Name")
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, null=True, blank=True)
    registered_on = models.DateField(verbose_name="Registration Date")
    registration_number = models.CharField(max_length=100, unique=True, verbose_name="Registration Number")
    employees = models.ManyToManyField(EmployeeModel, verbose_name="Employees", blank=True)

    def __str__(self):
        return f"{self.name}, {self.address}"

#-----------------------------------------------------------------------------------------------------------------------
