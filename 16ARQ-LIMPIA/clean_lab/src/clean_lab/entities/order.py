from dataclasses import dataclass, field


@dataclass
class Order:
    id: int
    amount: float
    events: list = field(default_factory=list)

    def validate(self):
        if self.amount <= 0:
            raise ValueError("Amount must be positive")

    def mark_created(self):
        self.events.append("OrderCreated")