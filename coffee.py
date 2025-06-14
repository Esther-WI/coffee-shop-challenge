from order import Order

class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string and have at least 3 characters")
        self._name = name

    @property
    def name (self):
        return self._name 
    
    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)

    