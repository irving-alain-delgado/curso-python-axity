from typing import Protocol
from clean_lab.interfaces.repository import OrderRepository


class UnitOfWork(Protocol):
    orders: OrderRepository

    def __enter__(self): ...
    def __exit__(self, *args): ...
    def commit(self): ...