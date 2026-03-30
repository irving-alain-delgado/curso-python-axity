from abc import ABC, abstractmethod
from orders_service.domain.entities import Order


class EventPublisher(ABC):

    @abstractmethod
    def publish_order_created(self, order: Order) -> None:
        pass