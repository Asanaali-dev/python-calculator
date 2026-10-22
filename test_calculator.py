import pytest
from calculator import calculate
def test_add():
    assert calculate(2, 3, "+") == 5
def test_power():
    assert calculate(2, 3, "**") == 8
def test_divide():
    assert calculate(10, 4, "/") == 2.5
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(5, 0, "/")
