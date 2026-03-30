def calculate_total(amount: float) -> float:
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if amount >= 1000:
        return amount * 0.9

    return amount