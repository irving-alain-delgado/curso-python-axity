from dataclasses import dataclass
from datetime import datetime, UTC
from uuid import uuid4


@dataclass
class Order:
    id: str
    user_id: str
    product: str
    quantity: int
    created_at: datetime

    @staticmethod
    def create(user_id: str, product: str, quantity: int) -> "Order":
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        return Order(
            id=str(uuid4()),
            user_id=user_id,
            product=product,
            quantity=quantity,
            created_at=datetime.now(UTC),
        )