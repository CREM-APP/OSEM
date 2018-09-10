import pytest
import os
from osef.access_data import Kbob


def test_check_language():
    kbob = Kbob()
    kbob._check_language(language="FRA")
    with pytest.raises(Exception):
        kbob._check_language(language="BRA")


def test_get_value():
    kbob = Kbob()
    # test of the function
    assert kbob.get_value(techno="Oil", indicator="EP renew") == 0.00902
    assert kbob.get_value(techno="Mazout", indicator="EP renouv", language="FRA") == 0.00902
    assert kbob.get_value(techno="Photovoltaik", indicator="CO2", language="GER") == 0.0964

    with pytest.raises(Exception):
        kbob.get_value(techno="XXX", indicator="EP renew")

    with pytest.raises(Exception):
        kbob.get_value(techno="Mazout", indicator="BTU/square.inch")


def test_get_units():
    kbob = Kbob()
    assert kbob.get_units(choice_col="EP renew") == "kWh_oil_eq"

    with pytest.raises(Exception):
        kbob.get_units(choice_col="nabila")


def test_get_available_technologies():
    kbob = Kbob()
    assert len(kbob.get_available_technologies()) == 108
    assert "Gaz naturel" in kbob.get_available_technologies(language="FRA")


def test_available_indicators():
    kbob = Kbob()
    assert kbob.get_available_indicators() == ['LCA_UB','EP_Global','EP_Renew', 'EP_Nonrenew','EP_Renew_Onsite',
                                               'EP_Percent_Renew','CO2']
    assert "FRA" not in kbob.get_available_indicators()


def test_filename():
    kbob = Kbob()
    assert kbob.get_filenames() == {'kbob': os.path.join("data", "data_kbob", "kbob_data2016.csv"),
                                    'unit':  os.path.join("data", "data_kbob", "kbob_unit2016.json"),
                                    'translation':  os.path.join("data", "data_kbob", "kbob_translation_indicator.csv")}


def test_kbob_version():
    kbob = Kbob()
    kbob.change_version(version_new=2222)
    assert kbob.get_kbob_version() == '2222'
    kbob.change_to_default_version()
    assert kbob.get_kbob_version() == '2016'
