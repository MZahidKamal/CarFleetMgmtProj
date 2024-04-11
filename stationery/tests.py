# All necessary imports for creating test cases.
from django.test import TestCase
from datetime import date

# Importing all database models from this app.
from .models import AddressModel, PersonModel, EmployeeModel, CompanyModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a class to test everything related to AddressModel.
class AddressModelTestCase(TestCase):

    # Creating an object of AddressModel.
    def setUp(self):
        self.address = AddressModel.objects.create(
            street='Kaiserstraße',
            house='75',
            zip_code='60329',
            city='Frankfurt am Main',
            state='Hessen',
            country='Germany'
        )

    # Testing each property of the AddressModel.
    def test_address_creation(self):
        # Test the creation of AddressModel objects
        self.assertEqual(self.address.street, 'Kaiserstraße')
        self.assertEqual(self.address.house, '75')
        self.assertEqual(self.address.zip_code, '60329')
        self.assertEqual(self.address.city, 'Frankfurt am Main')
        self.assertEqual(self.address.state, 'Hessen')
        self.assertEqual(self.address.country, 'Germany')

    # Testing the method of the AddressModel.
    def test_address_str_method(self):
        # Test the __str__ method of AddressModel
        expected_str = 'Kaiserstraße 75, 60329 Frankfurt am Main, Hessen, Germany'
        self.assertEqual(str(self.address), expected_str)

#-----------------------------------------------------------------------------------------------------------------------

# Creating a class to test everything related to PersonModel.
class PersonModelTestCase(TestCase):

    # Creating an object of PersonModel.
    def setUp(self):
        self.person = PersonModel.objects.create(
            first_name='John',
            last_name='Doe',
            date_of_birth=date(1999, 12, 31),
            email_address='john_doe@email.com',
            phone_number='+4912345678910',
            # Address has already been tested previously. So we are not creating it again and testing again.
        )

    # Testing each property of the PersonModel.
    def test_person_creation(self):
        self.assertEqual(self.person.first_name, 'John')
        self.assertEqual(self.person.last_name, 'Doe')
        self.assertEqual(self.person.date_of_birth, date(1999, 12, 31))
        self.assertEqual(self.person.email_address, 'john_doe@email.com')
        self.assertEqual(self.person.phone_number, '+4912345678910')

        # Calculating the age dynamically, then asserting and testing.
        expected_age = (date.today() - self.person.date_of_birth).days // 365
        self.assertEqual(self.person.age, expected_age)

    # Testing the method of the PersonModel.
    def test_person_str_method(self):
        expected_str = 'John Doe'
        self.assertEqual(str(self.person), expected_str)

#-----------------------------------------------------------------------------------------------------------------------

# Creating a class to test everything related to EmployeeModel.
class EmployeeModelTestCase(TestCase):

    # Creating an object of EmployeeModel.
    def setUp(self):
        self.employee = EmployeeModel.objects.create(
            # Person has already been tested previously. So we are not creating it again and testing again.
            designation='Sales Executive',
        )

    # Testing each property of the EmployeeModel.
    def test_employee_creation(self):
        self.assertEqual(self.employee.designation, 'Sales Executive')

    # Testing the method of the EmployeeModel.
    def test_employee_str_method(self):
        # It's creating only the full name, which has already been tested previously.
        # So we are not creating it again and testing again.
        pass

#-----------------------------------------------------------------------------------------------------------------------

# Creating a class to test everything related to CompanyModel.
class CompanyModelTestCase(TestCase):

    # Creating an object of CompanyModel.
    def setUp(self):
        self.company = CompanyModel.objects.create(
            name='Zhejiang Geely Holding Group',
            # Address has already been tested previously. So we are not creating it again and testing again.
            registered_on=date(2016, 1, 1),
            registration_number='12345678910-ABCD-EF',
            # Employee has already been tested previously. So we are not creating it again and testing again.
        )

    def test_company_creation(self):
        self.assertEqual(self.company.name, 'Zhejiang Geely Holding Group')
        self.assertEqual(self.company.registered_on, date(2016, 1, 1))
        self.assertEqual(self.company.registration_number, '12345678910-ABCD-EF')

    def test_company_str_method(self):
        # It's creating only the company name, and the address, which has already been tested previously.
        # So we are not creating these again and testing again.
        pass

#-----------------------------------------------------------------------------------------------------------------------
