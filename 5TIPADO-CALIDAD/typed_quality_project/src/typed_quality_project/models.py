from dataclasses import dataclass
from typing import Literal, Protocol, TypedDict


# ==============================
# 1️⃣ Type alias con Literal
# ==============================

OrderStatus = Literal["pending", "paid", "cancelled"]


# ==============================
# 2️⃣ TypedDict
# ==============================


class OrderData(TypedDict):
    id: int
    amount: float
    status: OrderStatus


# ==============================
# 3️⃣ Protocol
# ==============================


class SupportsSave(Protocol):
    def save(self) -> None: ...


# ==============================
# 4️⃣ Entidad principal
# ==============================


@dataclass
class Order:
    id: int
    amount: float
    status: OrderStatus

    def pay(self) -> None:
        if self.status != "pending":
            raise ValueError("Solo órdenes pendientes pueden pagarse")

        self.status = "paid"

    def cancel(self) -> None:
        if self.status == "paid":
            raise ValueError("No se puede cancelar una orden pagada")

        self.status = "cancelled"

    def to_dict(self) -> OrderData:
        return {
            "id": self.id,
            "amount": self.amount,
            "status": self.status,
        }
