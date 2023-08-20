from django.test import TestCase
from customer.models import *

class TestCustomerModel(TestCase):
    def setUp(self) -> None:
        self.customer1 = Customer.objects.create( phone_number = "09123456789", order = 0, point = 0)


    def test_customer_str(self):
        self.assertEquals(str(self.customer1.phone_number), '09123456789')

