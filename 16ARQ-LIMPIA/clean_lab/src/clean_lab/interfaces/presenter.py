from typing import Protocol
from clean_lab.entities.order import Order


class OrderPresenter(Protocol):
    def present(self, order: Order) -> dict: ...