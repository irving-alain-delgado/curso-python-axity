from unittest.mock import Mock

from orders_service.application.use_cases.create_order import CreateOrderUseCase
from orders_service.domain.entities import Order


def test_create_order_use_case_success():
    # Arrange
    mock_repo = Mock()
    mock_publisher = Mock()

    use_case = CreateOrderUseCase(
        repo=mock_repo,
        publisher=mock_publisher,
    )

    # Act
    order = use_case.execute(
        user_id="user1",
        product="Laptop",
        quantity=1,
    )

    # Assert
    assert isinstance(order, Order)
    assert order.user_id == "user1"

    mock_repo.save.assert_called_once_with(order)
    mock_publisher.publish_order_created.assert_called_once_with(order)