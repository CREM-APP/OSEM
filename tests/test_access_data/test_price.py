# TODO: remove unused statement
import pytest
from osef.access_data import Price


def test_price():
    price = Price()
    assert price._get_poly(1, "heat_pump_air_water") == [2000.0, 18000.0]
    assert price.get_units("heat_pump") == "kW"
    assert price.get_units("haet_pump_air") == "kW"      # test typo
    assert price.price_total('heat_pump', 10) == 38000
    assert price.price_total("electricity", 10) == 1.6
    assert price.price_by_unit("heat_pump") == 'Cost[CHF]=2000.0x +18000.0'
    assert price.get_available_technology()[0] == 'roof_isol'
    assert len(price.get_available_technology()) == 41
