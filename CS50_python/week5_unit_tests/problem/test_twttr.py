# Testing my twttr
# Harvard / cs50p / python
# problem set week 5  https://cs50.harvard.edu/python/2022/psets/5/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

from twttr import shorten

def test_lower():
    assert shorten('twitter') == 'twttr'

def test_upper():
    assert shorten('TWITTER') == 'TWTTR'

def test_digit():
    assert shorten('121') == '121'

def test_coma():
    assert shorten('TWITTER, twitter') == 'TWTTR, twttr'

def test_abba():
    assert shorten('abba') == 'bb'
