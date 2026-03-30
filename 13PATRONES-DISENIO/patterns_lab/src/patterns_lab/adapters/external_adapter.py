class ExternalProvider:
    def get_price(self):
        return {"total_price": 100}


class Price:
    def __init__(self, amount: float):
        self.amount = amount


class ExternalPriceAdapter:
    def __init__(self, provider: ExternalProvider):
        self.provider = provider

    def get_price(self) -> Price:
        data = self.provider.get_price()
        return Price(amount=data["total_price"])