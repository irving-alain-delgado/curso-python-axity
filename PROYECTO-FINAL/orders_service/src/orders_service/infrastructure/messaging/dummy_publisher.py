from orders_service.application.ports.event_publisher import EventPublisher
from orders_service.domain.entities import Order


class DummyEventPublisher(EventPublisher):

    def publish_order_created(self, order: Order) -> None:
        print(f"[EVENT] OrderCreated -> {order.id}")