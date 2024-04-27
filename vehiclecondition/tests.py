"""# All necessary imports for creating test cases.
from django.test import TestCase
from datetime import date, datetime

# Importing all database models from this app.
from .models import ProofImagesModel, VehicleConditionModel, CarReceivingVCModel, CarGivingVCModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a class to test everything related to ProofImagesModel.
class ProofImagesModelTestCases(TestCase):

    # Creating an object of ProofImagesModel.
    def setUp(self):
        self.proof_image = ProofImagesModel.objects.create(
            vin_number_image='workorder/test_images/01. vin_number',
            license_plate_image='workorder/test_images/02. license_plate',
            emission_sticker_image='workorder/test_images/03. emission_sticker',
            registration_certificate_image='workorder/test_images/04. registration_certificate',
            dashboard_image='workorder/test_images/05. dashboard',
            front_image='workorder/test_images/06. front',
            left_front_image='workorder/test_images/07. left_front',
            left_rear_image='workorder/test_images/08. left_rear',
            rear_image='workorder/test_images/09. rear',
            right_rear_image='workorder/test_images/10. right_rear',
            right_front_image='workorder/test_images/11. right_front',
            key_set_image='workorder/test_images/12. key_set',
            boot_accessories_image='workorder/test_images/13. boot_accessories'
        )

    def test_proof_images_model_str_method(self):
        self.assertIsInstance(self.proof_image, ProofImagesModel)
        self.assertTrue(self.proof_image.id)
        self.assertEqual(str(self.proof_image), f"General Images : Vehicle Condition : ID-{self.proof_image.id}")

    def test_image_fields(self):
        self.assertIsNotNone(self.proof_image.vin_number_image)
        self.assertIsNotNone(self.proof_image.license_plate_image)
        self.assertIsNotNone(self.proof_image.emission_sticker_image)
        self.assertIsNotNone(self.proof_image.registration_certificate_image)
        self.assertIsNotNone(self.proof_image.dashboard_image)
        self.assertIsNotNone(self.proof_image.front_image)
        self.assertIsNotNone(self.proof_image.left_front_image)
        self.assertIsNotNone(self.proof_image.left_rear_image)
        self.assertIsNotNone(self.proof_image.rear_image)
        self.assertIsNotNone(self.proof_image.right_rear_image)
        self.assertIsNotNone(self.proof_image.right_front_image)
        self.assertIsNotNone(self.proof_image.key_set_image)
        self.assertIsNotNone(self.proof_image.boot_accessories_image)

#-----------------------------------------------------------------------------------------------------------------------

class VehicleConditionModelTestCases(TestCase):

    # Creating an object of VehicleConditionModel.
    def setUp(self):
        self.vehicle_condition = VehicleConditionModel.objects.create(
            vin_number='L6TCX2E78NE034774',
            registration_number='WI-L7475E',
            mileage='7838',
            fuel_level='6/10',
            main_keys='2',
            transponder_keys='1',
            registration_certificate='ORIGINAL',
            first_aid_kit='YES',
            high_visibility_waistcoat='YES',
            warning_triangle='YES',
            luggage_net='YES',
            floor_mats='YES',
            rear_boot_rubber_mat='YES',
            charging_cable_type2='YES',
            charging_cable_schuko='YES',
            tyre_set='WINTER',
            tow_bar='YES',
            # ProofImages has already been tested previously. So we are not creating it again and testing again.
        )

    def test_vehicle_condition_creation(self):
        self.assertIsInstance(self.vehicle_condition, VehicleConditionModel)
        self.assertTrue(self.vehicle_condition.id)
        self.assertEqual(self.vehicle_condition.vin_number, 'L6TCX2E78NE034774')
        self.assertEqual(self.vehicle_condition.registration_number, 'WI-L7475E')
        self.assertEqual(self.vehicle_condition.mileage, '7838')
        self.assertEqual(self.vehicle_condition.fuel_level, '6/10')
        self.assertEqual(self.vehicle_condition.main_keys, '2')
        self.assertEqual(self.vehicle_condition.transponder_keys, '1')
        self.assertEqual(self.vehicle_condition.registration_certificate, 'ORIGINAL')
        self.assertEqual(self.vehicle_condition.first_aid_kit, 'YES')
        self.assertEqual(self.vehicle_condition.high_visibility_waistcoat, 'YES')
        self.assertEqual(self.vehicle_condition.warning_triangle, 'YES')
        self.assertEqual(self.vehicle_condition.luggage_net, 'YES')
        self.assertEqual(self.vehicle_condition.floor_mats, 'YES')
        self.assertEqual(self.vehicle_condition.rear_boot_rubber_mat, 'YES')
        self.assertEqual(self.vehicle_condition.charging_cable_type2, 'YES')
        self.assertEqual(self.vehicle_condition.charging_cable_schuko, 'YES')
        self.assertEqual(self.vehicle_condition.tyre_set, 'WINTER')
        self.assertEqual(self.vehicle_condition.tow_bar, 'YES')
        # ProofImages has already been tested previously. So we are not creating it again and testing again.
        # self.assertTrue(self.vehicle_condition.created_on)

    def test_vehicle_condition_model_str_method(self):
        expected_str = f'L6TCX2E78NE034774, WI-L7475E, 7838'
        self.assertEqual(str(self.vehicle_condition), expected_str)

#-----------------------------------------------------------------------------------------------------------------------

class CarReceivingVCModelTestCases(TestCase):

    # Creating an object of CarReceivingVCModel.
    def setUp(self):
        self.car_receiving_vc = CarReceivingVCModel.objects.create(
            # wo_number='',
            # VehicleCondition has already been tested previously. So we are not creating it again and testing again.
            receiving_from='Autohaus Hedtke GmbH',
            created_on=datetime.now(),
            location='Rudolf-Diesel-Straße 42, 64331 Weiterstadt',
            e_signature='workorder/test_images/14. e_signature',
        )

    def test_car_receiving_vc_creation(self):
        self.assertIsInstance(self.car_receiving_vc, CarReceivingVCModel)
        self.assertTrue(self.car_receiving_vc.id)
        # self.assertTrue(self.car_receiving_vc.wo_number)
        # VehicleCondition has already been tested previously. So we are not creating it again and testing again.
        self.assertTrue(self.car_receiving_vc.receiving_from)
        self.assertTrue(self.car_receiving_vc.created_on)
        self.assertTrue(self.car_receiving_vc.location)
        self.assertTrue(self.car_receiving_vc.e_signature)

    def test_car_receiving_vc_model_str_method(self):
        expected_str = f'Autohaus Hedtke GmbH, {self.car_receiving_vc.created_on}'
        self.assertEqual(str(self.car_receiving_vc), expected_str)

#-----------------------------------------------------------------------------------------------------------------------

class CarGivingVCModelTestCases(TestCase):

    # Creating an object of CarGivingVCModel.
    def setUp(self):
        self.car_giving_vc = CarGivingVCModel.objects.create(
            # VehicleCondition has already been tested previously. So we are not creating it again and testing again.
            giving_to='Autohaus Hedtke GmbH',
            created_on=datetime.now(),
            location='Rudolf-Diesel-Straße 42, 64331 Weiterstadt',
            e_signature='workorder/test_images/14. e_signature',
        )

    def test_car_giving_vc_creation(self):
        self.assertIsInstance(self.car_giving_vc, CarGivingVCModel)
        self.assertTrue(self.car_giving_vc.id)
        # VehicleCondition has already been tested previously. So we are not creating it again and testing again.
        self.assertTrue(self.car_giving_vc.giving_to)
        self.assertTrue(self.car_giving_vc.created_on)
        self.assertTrue(self.car_giving_vc.location)
        self.assertTrue(self.car_giving_vc.e_signature)

    def test_car_receiving_vc_model_str_method(self):
        expected_str = f'Autohaus Hedtke GmbH, {self.car_giving_vc.created_on}'
        self.assertEqual(str(self.car_giving_vc), expected_str)

#-----------------------------------------------------------------------------------------------------------------------
"""