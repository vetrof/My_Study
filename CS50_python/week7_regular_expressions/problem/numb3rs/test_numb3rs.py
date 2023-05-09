# create tests for numb3rs.py file
# Harvard / cs50p / python
# problem set week 7  https://cs50.harvard.edu/python/2022/psets/7
# Vitaly aka Vetrof / vetrof@gmail.com  / vetrof.com

from numb3rs import validate


def test_validate_digit():
    assert validate("255.0.0.255") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("12.33.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.21000") == False
    assert validate("121000") == False


def test_validate_char():
    assert validate("cat") == False
    assert validate("CAT") == False
    assert validate("a.a.a.a") == False
    assert validate("") == False
    assert validate(" ") == False
