from patterns_lab.pricing.strategy import PricingStrategy


class PriceCalculator:
    def __init__(self, strategy: PricingStrategy):
        self.strategy = strategy

    def calculate(self, amount: float) -> float:
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        return self.strategy.calculate(amount)