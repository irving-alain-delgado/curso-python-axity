from typing import Protocol


class PricingStrategy(Protocol):
    def calculate(self, amount: float) -> float:
        ...


class RegularPricing:
    def calculate(self, amount: float) -> float:
        return amount


class PremiumPricing:
    def calculate(self, amount: float) -> float:
        return amount * 0.9


class WholesalePricing:
    def calculate(self, amount: float) -> float:
        return amount * 0.8