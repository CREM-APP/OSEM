import pytest
from osef.access_data import PoliticalObj


def test_pol():
    pol = PoliticalObj()
    assert pol.get_objective("2000 W 2050", "Renew", False) == 65
    assert pol.get_objective("Paris", "CO2", False) == 30
    assert pol.get_objective("2000 W 2050", "Renew") == {'value': 65, 'year_ref': 2005, 'year_obj': 2050}
