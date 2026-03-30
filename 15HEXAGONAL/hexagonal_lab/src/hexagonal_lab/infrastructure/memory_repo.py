from hexagonal_lab.domain.order import Order


class MemoryOrderRepository:
    def __init__(self):
        self.storage: dict[int, Order] = {}

    def save(self, order: Order) -> None:
        self.storage[order.id] = order

    def get(self, order_id: int) -> Order | None:
        return self.storage.get(order_id)