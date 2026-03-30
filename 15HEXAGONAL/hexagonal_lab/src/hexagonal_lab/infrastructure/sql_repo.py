from sqlalchemy.orm import Session

from hexagonal_lab.domain.order import Order
from hexagonal_lab.infrastructure.sql_models import OrderModel


class SqlOrderRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, order: Order) -> None:
        model = OrderModel(id=order.id, amount=order.amount)
        self.session.add(model)
        self.session.commit()

    def get(self, order_id: int) -> Order | None:
        model = self.session.get(OrderModel, order_id)

        if model is None:
            return None

        return Order(id=model.id, amount=model.amount)