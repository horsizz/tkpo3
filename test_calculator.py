import pytest
from calculator import calculate_monthly_payment


def test_standard_mortgage():
    # Кредит 1 000 000 под 10% на 10 лет -> ~13215.07
    assert calculate_monthly_payment(1_000_000, 10, 10) == 12215.07


def test_zero_interest_raises_error():
    with pytest.raises(ValueError):
        calculate_monthly_payment(500_000, 0, 5)


def test_negative_principal_raises_error():
    with pytest.raises(ValueError):
        calculate_monthly_payment(-100_000, 12, 5)


def test_zero_years_raises_error():
    with pytest.raises(ValueError):
        calculate_monthly_payment(500_000, 12, "")
