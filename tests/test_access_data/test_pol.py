import pytest
from osef.access_data import PoliticalObjective


def test_pol():
    pol = PoliticalObjective()
    assert pol.get_objective("2000 W 2050", "renewable", False) == 65
    assert pol.get_objective("Paris agreement", "CO2_reduction", False) == 30
    assert pol.get_objective("2000 W 2050", "renewable") == {'value': 65, 'year_ref': 2005, 'year_obj': 2050}
    assert pol.get_politic_framework() == ['Paris agreement', '3x20_2020', '3x20_2030', 'societe_2000_W_2020',
                                           'societe_2000_W_2035', 'societe_2000_W_2050']
