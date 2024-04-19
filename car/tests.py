# All necessary imports for creating test cases.
from django.test import TestCase
from datetime import date

# Importing all necessary components from this app.
from .models import CarModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a class to test everything related to CarModel.
class CarModelTestCases(TestCase):

    # Creating an object of CarModel.
    def setUp(self):
        self.car = CarModel.objects.create(
            brand='Lynk & Co',
            model='01',
            vin_number='L6TCX2E77NE016623',
            registration_number='WI-L5763E',
            color='BLUE',
            tuv_expire_date=date(2026, 10, 11),
        )

    def test_car_creation(self):
        self.assertIsInstance(self.car, CarModel)
        self.assertTrue(self.car.id)
        self.assertEqual(self.car.brand, 'Lynk & Co')
        self.assertEqual(self.car.model, '01')
        self.assertEqual(self.car.vin_number, 'L6TCX2E77NE016623')
        self.assertEqual(self.car.registration_number, 'WI-L5763E')
        self.assertEqual(self.car.color, 'BLUE')
        self.assertEqual(self.car.tuv_expire_date, date(2026, 10, 11))

    def test_car_model_str_method(self):
        expected_str = f'Lynk & Co - 01 - L6TCX2E77NE016623 - WI-L5763E - 2026-10-11'
        self.assertEqual(str(self.car), expected_str)

#-----------------------------------------------------------------------------------------------------------------------
