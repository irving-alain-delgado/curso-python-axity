from hexagonal_lab.domain.order import Order
from hexagonal_lab.application.ports import OrderRepository, Notifier


class CreateOrder:
    def __init__(self, repo: OrderRepository, notifier: Notifier):
        self.repo = repo
        self.notifier = notifier

    def execute(self, order_id: int, amount: float) -> Order:
        order = Order(id=order_id, amount=amount)
        order.validate()

        self.repo.save(order)
        self.notifier.notify(f"Order {order_id} created")

        return order