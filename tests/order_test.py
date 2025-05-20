import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def test_order_associations(self):
        customer = Customer("Allan")
        coffee = Coffee("Mocha")
        order = Order(customer, coffee, 3.5)
        
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 3.5)

    def test_invalid_price(self):
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        with self.assertRaises(ValueError):
            Order(customer, coffee, 20.0)  

    def test_invalid_customer_type(self):
        with self.assertRaises(TypeError):
            Order("NotACustomer", Coffee("Espresso"), 2.5)