
# test Cookie Jar
# Harvard / cs50p / python
# problem set week 8  https://cs50.harvard.edu/python/2022/psets/8
# Vetrof / vetrof@gmail.com  / vetrof.com
import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.cookies == 0

    with pytest.raises(ValueError):
        jar = Jar(-10)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.cookies == 10

    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.cookies == 5

    with pytest.raises(ValueError):
        jar.withdraw(10)




