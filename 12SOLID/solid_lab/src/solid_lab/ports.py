from typing import Protocol
from solid_lab.domain import Order


class OrderRepository(Protocol):
    def add(self, order: Order) -> None: ...
    def get(self, order_id: int) -> Order | None: ...