import pytest
from osem.access_data import PoliticalObjective


def test_pol():
    pol = PoliticalObjective()
    assert pol.get_objective(politic_type="2000 W 2050", objective_type="renewable", return_year=False) == 65
    assert pol.get_objective(politic_type="Paris agreement", objective_type="CO2_reduction", return_year=False) == 30
    assert pol.get_objective(politic_type="2000 W 2050", objective_type="renewable") == {'value': 65, 'year_ref': 2005,
                                                                                         'year_obj': 2050}
    assert pol.get_politic_framework() == ['Paris agreement', '3x20_2020', '3x20_2030', 'societe_2000_W_2020',
                                           'societe_2000_W_2035', 'societe_2000_W_2050','strategie_energetique_2050',
                                           'strategie_energetique_2050']
