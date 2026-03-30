from sqlalchemy.orm import Session

from orders_service.domain.entities import Order
from orders_service.application.ports.repository import OrderRepository
from orders_service.infrastructure.db.models import OrderModel


class SQLAlchemyOrderRepository(OrderRepository):

    def __init__(self, session: Session):
        self.session = session

    def save(self, order: Order) -> None:
        db_order = OrderModel(
            id=order.id,
            user_id=order.user_id,
            product=order.product,
            quantity=order.quantity,
            created_at=order.created_at,
        )

        self.session.add(db_order)
        self.session.commit()