import pytest
from calculate import calculate_total


def test_total_without_discount():
    assert calculate_total(100) == 105.00


def test_discount_boundary():
    assert calculate_total(300) == 315.00


def test_total_with_discount():
    # Intentionally incorrect for the first CI run
    assert calculate_total(400) == 380.00


def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_total(-100)
