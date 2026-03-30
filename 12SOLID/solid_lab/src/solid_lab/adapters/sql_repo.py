from solid_lab.domain import Order
from solid_lab.adapters.sql_models import OrderModel


class SqlOrderRepository:
    def __init__(self, session):
        self.session = session

    def add(self, order: Order) -> None:
        model = OrderModel(id=order.id, amount=order.amount)
        self.session.add(model)
        self.session.commit()

    def get(self, order_id: int) -> Order | None:
        model = self.session.get(OrderModel, order_id)
        if not model:
            return None
        return Order(id=model.id, amount=model.amount)