from abc import ABC, abstractmethod
from orders_service.domain.entities import Order


class OrderRepository(ABC):

    @abstractmethod
    def save(self, order: Order) -> None:
        pass