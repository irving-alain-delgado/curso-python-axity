from clean_lab.use_cases.create_order import CreateOrder
from clean_lab.entities.order import Order


class FakeRepo:
    def __init__(self):
        self.storage = {}

    def save(self, order):
        self.storage[order.id] = order

    def get(self, order_id):
        return self.storage.get(order_id)


class FakeUoW:
    def __enter__(self):
        self.orders = FakeRepo()
        return self

    def __exit__(self, *args):
        pass

    def commit(self):
        pass


class FakePresenter:
    def present(self, order):
        return {
            "id": order.id,
            "amount": order.amount,
            "events": order.events,
        }


def test_create_order():
    uow = FakeUoW()
    presenter = FakePresenter()

    use_case = CreateOrder(uow, presenter)

    result = use_case.execute(1, 100)

    assert result["amount"] == 100
    assert "OrderCreated" in result["events"]