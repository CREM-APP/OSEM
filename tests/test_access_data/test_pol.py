# TODO: remove unused statement
import pytest
from osef.access_data import PoliticalObj


def test_pol():
    pol = PoliticalObj()
    assert pol.get_obj("2000 W 2050", "Renew", False) == 65
    assert pol.get_obj("Paris", "CO2", False) == 30
    assert pol.get_obj("2000 W 2050", "Renew") == (65, 2005, 2050)
