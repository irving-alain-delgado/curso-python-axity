from solid_lab.domain import Order


class MemoryOrderRepository:
    def __init__(self):
        self.storage: dict[int, Order] = {}

    def add(self, order: Order) -> None:
        self.storage[order.id] = order

    def get(self, order_id: int) -> Order | None:
        return self.storage.get(order_id)