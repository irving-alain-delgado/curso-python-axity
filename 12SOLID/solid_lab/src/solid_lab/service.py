from solid_lab.domain import Order
from solid_lab.ports import OrderRepository


class OrderService:
    def __init__(self, repo: OrderRepository):
        self.repo = repo

    def create_order(self, order_id: int, amount: float) -> Order:
        if amount <= 0:
            raise ValueError("Amount must be positive")

        order = Order(id=order_id, amount=amount)
        self.repo.add(order)
        return order

    def get_order(self, order_id: int) -> Order | None:
        return self.repo.get(order_id)