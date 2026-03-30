from dataclasses import dataclass, field


@dataclass(order=True)
class Order:
    id: int
    price: float
    quantity: int
    total: float = field(init=False)

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        if self.quantity <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")

        self.total = self.price * self.quantity

    def __str__(self) -> str:
        return f"Order(id={self.id}, total={self.total})"