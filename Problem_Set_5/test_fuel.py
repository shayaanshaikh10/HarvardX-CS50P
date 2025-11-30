from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("3/4")==75
    assert convert ("2/4")==50

def test_value_error():
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("-1/2")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("9/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"


