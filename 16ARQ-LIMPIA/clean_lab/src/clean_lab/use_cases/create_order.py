from clean_lab.entities.order import Order
from clean_lab.interfaces.uow import UnitOfWork
from clean_lab.interfaces.presenter import OrderPresenter


class CreateOrder:
    def __init__(self, uow: UnitOfWork, presenter: OrderPresenter):
        self.uow = uow
        self.presenter = presenter

    def execute(self, order_id: int, amount: float):
        with self.uow:
            order = Order(order_id, amount)
            order.validate()
            order.mark_created()

            self.uow.orders.save(order)
            self.uow.commit()

        return self.presenter.present(order)