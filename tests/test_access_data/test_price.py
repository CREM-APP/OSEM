import pytest
from osef.access_data import Price


def test_price():
    price = Price()
    assert price.get_units("heat_pump") == "kW"
    assert price.get_units("haet_pump") == "kW"      # test typo
    assert price.price_total('heat_pump', 10) == 38000
    assert price.price_total("electricity", 10) == 1.6
    assert price.price_by_unit("heat_pump") == 'Cost[CHF]=2000.0x +18000.0'