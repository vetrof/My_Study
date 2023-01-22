
# test for Working.py
# am/pm converter time range to 24 hour format
# '9 AM to 5 PM'  >>>> '09:00 to 17:00'
# Harvard / cs50p / python
# problem set week 7  https://cs50.harvard.edu/python/2022/psets/7
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

from working import convert
import pytest


def test_convert_ampm():
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'


def test_convert_error():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')

    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')

    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')
