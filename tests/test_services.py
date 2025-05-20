from datetime import date

import pytest

from services import (
    calculate,
    convert_length,
    convert_weight,
    convert_temperature,
    calculate_bmi,
    date_difference,
)


def test_calculate_add():
    assert calculate(1, '+', 2) == 3


def test_calculate_div_zero():
    with pytest.raises(ValueError):
        calculate(1, '/', 0)


def test_convert_length():
    result = convert_length(1)
    assert result['公分'] == 100
    assert result['英吋'] == pytest.approx(39.3701)


def test_bmi():
    bmi = calculate_bmi(170, 60)
    assert round(bmi, 2) == 20.76


def test_date_difference():
    d1 = date(2024, 1, 1)
    d2 = date(2024, 1, 5)
    assert date_difference(d1, d2) == 4
