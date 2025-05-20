import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_customer_name_getter(self):
        customer = Customer("Alice")
        self.assertEqual(customer.name, "Alice")

    def test_customer_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("A")

    def test_create_order(self):
        customer = Customer("John")
        coffee = Coffee("Espresso")
        customer.create_order(coffee, 3.0)
        self.assertEqual(len(customer.orders()), 1)
        self.assertEqual(customer.orders()[0].price, 3.0)