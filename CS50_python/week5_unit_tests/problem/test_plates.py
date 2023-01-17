# vanity plate validator unit test
# Harvard / cs50p / python
# problem set week 5  https://cs50.harvard.edu/python/2022/psets/5/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

from plates import is_valid

def test_valid():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False
    assert is_valid('CS50P') == False
    assert is_valid('PI3.14') == False
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False
    assert is_valid('123456') == False