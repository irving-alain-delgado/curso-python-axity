from clean_lab.entities.order import Order

class SqlOrderRepository:
    def __init__(self, session):
        self.session = session

    def save(self, order):
        self.session.add(order)

    def get(self, order_id):
        return self.session.get(Order, order_id)