# All necessary imports for creating test cases.
from django.test import TestCase
from datetime import date, datetime

# Importing all necessary components from this app.
from .models import CarExpensesModel, OverheadExpensesModel, WorkOrdersModel

#-----------------------------------------------------------------------------------------------------------------------

# Creating a class to test everything related to CarExpensesModel.
class CarExpensesModelTestCases(TestCase):

    # Creating an object of CarExpensesModel.
    def setUp(self):
        self.car_expenses = CarExpensesModel.objects.create(
            expense_type='REFUELING COST',
            amount='55.90',
            created_on=datetime.now(),
            payment_method='MASTER CARD',
            receipt_image='workorder/test_images/15. refueling_receipt',
        )

    def test_car_expenses_creation(self):
        self.assertIsInstance(self.car_expenses, CarExpensesModel)
        self.assertTrue(self.car_expenses.id)
        self.assertEqual(self.car_expenses.expense_type, 'REFUELING COST')
        self.assertEqual(self.car_expenses.amount, '55.90')
        self.assertTrue(self.car_expenses.created_on)
        self.assertEqual(self.car_expenses.payment_method, 'MASTER CARD')
        self.assertEqual(self.car_expenses.receipt_image, 'workorder/test_images/15. refueling_receipt')

    def test_car_expenses_model_str_method(self):
        expected_str = f'REFUELING COST - 55.90 - MASTER CARD - {self.car_expenses.created_on}'
        self.assertEqual(str(self.car_expenses), expected_str)

#-----------------------------------------------------------------------------------------------------------------------

class OverheadExpensesModelTestCases(TestCase):

    # Creating an object of OverheadExpensesModel.
    def setUp(self):
        self.overhead_expenses = OverheadExpensesModel.objects.create(
            expense_type='TAXI COST',
            amount='23.80',
            created_on=datetime.now(),
            payment_method='MASTER CARD',
            receipt_image='workorder/test_images/16. taxi_receipt',
        )

    def test_overhead_expenses_creation(self):
        self.assertIsInstance(self.overhead_expenses, OverheadExpensesModel)
        self.assertTrue(self.overhead_expenses.id)
        self.assertEqual(self.overhead_expenses.expense_type, 'TAXI COST')
        self.assertEqual(self.overhead_expenses.amount, '23.80')
        self.assertTrue(self.overhead_expenses.created_on)
        self.assertEqual(self.overhead_expenses.payment_method, 'MASTER CARD')
        self.assertEqual(self.overhead_expenses.receipt_image, 'workorder/test_images/16. taxi_receipt')

    def test_overhead_expenses_model_str_method(self):
        expected_str = f'TAXI COST - 23.80 - MASTER CARD - {self.overhead_expenses.created_on}'
        self.assertEqual(str(self.overhead_expenses), expected_str)

#-----------------------------------------------------------------------------------------------------------------------

class WorkOrdersModelTestCases(TestCase):

    # Creating an object of WorkOrderModel.
    def setUp(self):
        self.work_order = WorkOrdersModel.objects.create(
            # wo_number='WO195673',
            type='CAR RETURN',
            car_vin='L6TCX2E78NE034774',
            created_on=datetime.now(),
            status='IN PROCESS',
            delivery_date=date(2016, 10, 11),
            car_dealer='Haas GmbH',
            customer='Paul Lauterbach',
            delivery_agent='Juan Manuel',
            # car_receiving_vc='',
            # CarReceivingVCModel has already been tested previously. So we are not creating it again and testing again.
            # car_giving_vc='',
            # CarGivingVCModel has already been tested previously. So we are not creating it again and testing again.
            # car_expenses='',
            # CarExpensesModel has already been tested previously. So we are not creating it again and testing again.
            # overhead_expenses='',
            # OverheadExpensesModel has already been tested previously. So we are not creating it again and testing again.
        )

    def test_work_order_creation(self):
        self.assertIsInstance(self.work_order, WorkOrdersModel)
        self.assertTrue(self.work_order.id)
        self.assertTrue(self.work_order.wo_number)
        self.assertEqual(self.work_order.type, 'CAR RETURN')
        self.assertEqual(self.work_order.car_vin, 'L6TCX2E78NE034774')
        self.assertTrue(self.work_order.created_on)
        self.assertEqual(self.work_order.status, 'IN PROCESS')
        self.assertEqual(self.work_order.delivery_date, date(2016, 10, 11))
        self.assertEqual(self.work_order.car_dealer, 'Haas GmbH')
        self.assertEqual(self.work_order.customer, 'Paul Lauterbach')
        self.assertEqual(self.work_order.delivery_agent, 'Juan Manuel')

    def test_work_order_model_str_method(self):
        expected_str = f'{self.work_order.wo_number} - CAR RETURN - L6TCX2E78NE034774 - {self.work_order.created_on}'
        self.assertEqual(str(self.work_order), expected_str)

#-----------------------------------------------------------------------------------------------------------------------
