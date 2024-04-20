# All necessary imports for creating test cases.
from django.test import TestCase

# Importing all necessary components from this app.
from .models import ManufacturerModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a class to test everything related to DeliveryAgentModel.
class ManufacturerModelTestCases(TestCase):

    # Creating an object of ManufacturerModel.
    def setUp(self):
        pass
        # company_info='',
        # CompanyModel has already been tested previously. So we are not creating it again and testing again.

    def test_manufacturer_creation(self):
        pass

    def test_manufacturer_model_str_method(self):
        pass

#-----------------------------------------------------------------------------------------------------------------------
