# Testing bank
# Harvard / cs50p / python
# problem set week 5  https://cs50.harvard.edu/python/2022/psets/5/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

from bank import value

def test_value():
    assert value('Hello') == 0
    assert value('Hi') == 20
    assert value('Alloha') == 100
