import pytest
from orders_service.domain.entities import Order
from orders_service.domain.exceptions import InvalidQuantityError

def test_create_order_success():
    order = Order.create("user1", "Laptop", 2)

    assert order.user_id == "user1"
    assert order.product == "Laptop"
    assert order.quantity == 2
    assert order.id is not None


def test_create_order_invalid_quantity():
    with pytest.raises(InvalidQuantityError):
        Order.create("user1", "Laptop", 0)