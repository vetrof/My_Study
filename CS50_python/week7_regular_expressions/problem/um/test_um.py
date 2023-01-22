# test um.py
# Harvard / cs50p / python
# problem set week 7  https://cs50.harvard.edu/python/2022/psets/7
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

from um import count


def  test_count1():
    assert count("um") == 1
    assert count("uma") == 0


def  test_count2():
    assert count("um?") == 1


def  test_count3():
    assert count("Um, thanks for the album.") == 1


def  test_count3():
    assert count("Um, thanks, um") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
    assert count("Um, thanks, um, regular expressions make sense now.") == 2
    assert count("Um... what are regular expressions?") == 1
    assert count("This is, um... CS50.") == 1
    assert count("Hello, um, world") == 1

