import project
import pytest


def test_check_input():
    with pytest.raises(ValueError):
        project.check_input('')

    with pytest.raises(ValueError):
        project.check_input('123')


def test_m_index_now():
    w = {'temp_c': 7.0,
         'feelslike_c': 1.8, 'wind_kph': 33.1,
         'gust_kph': 49.3,
         'pressure_mmHg': 765}
    k = {'kp_index': 2}

    assert project.m_index_now(w, k) == {'m_index': 79.5}


def test_print_current():
    assert project.print_m_now({'m_index': 7}) == 'm_index                          7'






