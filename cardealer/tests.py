# All necessary imports for creating test cases.
from django.test import TestCase

# Importing all necessary components from this app.
from .models import CarDealerModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a class to test everything related to DeliveryAgentModel.
class CarDealerModelTestCases(TestCase):

    # Creating an object of CarModel.
    def setUp(self):
        pass
        # company_info='',
        # CompanyModel has already been tested previously. So we are not creating it again and testing again.

    def test_car_dealer_creation(self):
        pass

    def test_car_dealer_model_str_method(self):
        pass

#-----------------------------------------------------------------------------------------------------------------------
