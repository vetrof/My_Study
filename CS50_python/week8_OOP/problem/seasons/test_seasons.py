import sys

import seasons
import datetime
import pytest

def test_get_date():
    seasons.get_date('2023-01-02') == datetime.date(2023, 1, 2)

    with pytest.raises(SystemExit):
        seasons.get_date('qweqwe')

    with pytest.raises(SystemExit):
        seasons.get_date('2345 43 09')


def test_minutes_to_text():
    seasons.minutes_to_text('123') == '000'
