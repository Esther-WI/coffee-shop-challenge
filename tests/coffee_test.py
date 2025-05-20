import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def test_coffee_name_getter(self):
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("L")

    def test_num_orders_and_avg_price(self):
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        Order(customer, coffee, 5.0)
        Order(customer, coffee, 4.0)

        self.assertEqual(coffee.num_orders(), 2)
        self.assertEqual(coffee.avg_price(), 4.5)