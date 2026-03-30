from typing import Protocol
from hexagonal_lab.domain.order import Order


class OrderRepository(Protocol):
    def save(self, order: Order) -> None: ...
    def get(self, order_id: int) -> Order | None: ...


class Notifier(Protocol):
    def notify(self, message: str) -> None: ...