from patterns_lab.pricing.strategy import (
    RegularPricing,
    PremiumPricing,
    WholesalePricing,
)
from patterns_lab.pricing.context import PriceCalculator


def test_regular_pricing():
    calculator = PriceCalculator(RegularPricing())
    assert calculator.calculate(100) == 100


def test_premium_pricing():
    calculator = PriceCalculator(PremiumPricing())
    assert calculator.calculate(100) == 90


def test_wholesale_pricing():
    calculator = PriceCalculator(WholesalePricing())
    assert calculator.calculate(100) == 80