# fuel unit test
# Harvard / cs50p / python
# problem set week 5  https://cs50.harvard.edu/python/2022/psets/5/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('3/4') == 75
    assert convert('1/4') == 25
    assert convert('4/4') == 100
    assert convert('0/4') == 0


def test_error():
    with pytest.raises(ZeroDivisionError):
        convert('4/0')

    with pytest.raises(ValueError):
        convert('1.5/3')

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'
