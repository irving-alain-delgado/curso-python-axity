from orders_service.domain.entities import Order
from orders_service.application.ports.repository import OrderRepository
from orders_service.application.ports.event_publisher import EventPublisher


class CreateOrderUseCase:

    def __init__(self, repo: OrderRepository, publisher: EventPublisher):
        self.repo = repo
        self.publisher = publisher

    def execute(self, user_id: str, product: str, quantity: int) -> Order:
        order = Order.create(user_id, product, quantity)
        self.repo.save(order)
        self.publisher.publish_order_created(order)
        return order