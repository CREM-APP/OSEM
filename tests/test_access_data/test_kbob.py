import pytest
from osef.access_data import Kbob


def test_check_language():
    kbob = Kbob()
    kbob._check_language("FRA")
    with pytest.raises(Exception):
        kbob._check_language("BRA")


def test_get_value():
    kbob = Kbob()
    assert kbob.get_value("Oil", "EP renew") == 0.00902
    assert kbob.get_value("Mazout", "EP renew", language="FRA") == 0.00902
    assert kbob.get_value("Photovoltaik", "CO2", language="GER") == 0.0964

    with pytest.raises(Exception):
        kbob.get_value("XXX", "EP renew")

    with pytest.raises(Exception):
        kbob.get_value("Mazout", "BTU/square.inch")


def test_get_units():
    kbob = Kbob()
    assert kbob.get_units("EP renew") == "kWh_oil_eq"

    with pytest.raises(Exception):
        kbob.get_units("nabila")


def test_get_available_technologies():
    kbob = Kbob()
    assert len(kbob.get_available_technologies()) == 108
    assert "Gaz naturel" in kbob.get_available_technologies(language="FRA")


def test_available_indicators():
    kbob = Kbob()
    assert len(kbob.available_indicators) == 7
    assert "FRA" not in kbob.available_indicators


def test_kbob_version():
    kbob = Kbob()
    assert kbob.year_version == 2016
