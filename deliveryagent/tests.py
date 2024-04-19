# All necessary imports for creating test cases.
from django.test import TestCase

# Importing all necessary components from this app.
from .models import DeliveryAgentModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a class to test everything related to DeliveryAgentModel.
class DeliveryAgentModelTestCases(TestCase):

    # Creating an object of CarModel.
    def setUp(self):
        pass
        # personal_info='',
        # PersonModel has already been tested previously. So we are not creating it again and testing again.

    def test_delivery_agent_creation(self):
        pass

    def test_delivery_agent_model_str_method(self):
        pass

#-----------------------------------------------------------------------------------------------------------------------
