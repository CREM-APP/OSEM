import pytest
from osef.access_data import Kbob


def test_kbob():
    kbob = Kbob()
    # test loading the data
    assert kbob.data.index[0] == "Oil EL"
    assert kbob.data.index[-1] == "Cogeneration (CHP) plant - small gas"
    assert kbob.data.columns[0] == "LCA_UB"
    # test the functions
    assert kbob.get_units("EP_Renew") == "kWh_oil_eq"
    assert kbob.get_value("Oil", "EP_Renew") == 0.00902
    assert kbob.get_value("Oil", "EP_Renew_si") == 0.0
    assert kbob.get_value_french("Mazout", "EP_Renew") == 0.00902

