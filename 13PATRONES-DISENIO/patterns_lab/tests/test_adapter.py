from patterns_lab.adapters.external_adapter import (
    ExternalProvider,
    ExternalPriceAdapter,
)


def test_adapter():
    provider = ExternalProvider()
    adapter = ExternalPriceAdapter(provider)

    price = adapter.get_price()

    assert price.amount == 100