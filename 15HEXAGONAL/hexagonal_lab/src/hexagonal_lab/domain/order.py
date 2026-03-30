from dataclasses import dataclass


@dataclass
class Order:
    id: int
    amount: float

    def validate(self):
        if self.amount <= 0:
            raise ValueError("Amount must be positive")