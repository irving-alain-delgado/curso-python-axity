from tdd_lab.pricing import calculate_total
from hypothesis import given
from hypothesis import strategies as st


def test_no_discount():
    assert calculate_total(500) == 500


def test_discount_applied():
    assert calculate_total(1000) == 900


def test_negative_amount_raises():
    import pytest
    with pytest.raises(ValueError):
        calculate_total(-10)

@given(st.floats(min_value=0, max_value=10000))
def test_total_never_negative(amount):
    result = calculate_total(amount)
    assert result >= 0