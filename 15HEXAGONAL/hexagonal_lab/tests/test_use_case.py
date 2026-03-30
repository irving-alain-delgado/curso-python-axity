from hexagonal_lab.application.use_cases import CreateOrder
from hexagonal_lab.infrastructure.memory_repo import MemoryOrderRepository


class FakeNotifier:
    def notify(self, message: str):
        self.message = message


def test_create_order_use_case():
    repo = MemoryOrderRepository()
    notifier = FakeNotifier()

    use_case = CreateOrder(repo, notifier)

    order = use_case.execute(1, 200)

    assert order.amount == 200
    assert repo.get(1) == order
    assert "Order 1 created" in notifier.message