import matplotlib.pyplot as plt
import numpy as np
import pytest
from osef.access_data import Price
from osef.general.helper import func_logarithm


def test_get_info_price():

    price = Price()
    assert price.get_technology_available() == ['BoilerPellet', 'BoilerGas', 'BoilerOil', 'HeatPumpAirWater',
                                                'HeatPumpWaterWater', 'HeatPumpWaterSoil', 'SeasonalStorage',
                                                'DailyStorageHt', 'DailyStorageLt', 'PipeStreet', 'PipeFields', 'PV',
                                                'CHP','SolarThermalPanel', 'IsolationRoof', 'IsolationWindows',
                                                'IsolationWall']

    assert price.get_type_of_price_available(techno_choice="seasonalstorage") == ['cost_machine', 'cost_installation','CAPEX',
                                                                    'maintenance']
    # obtain the bibliographical reference of the price
    assert price.get_reference_for_price(techno_choice="DailyStorageHt", price_choice="cost_machine"
                                         ).values[0] == 'viessmann catalogue, 2018'
    assert price.get_units(techno_choice="BoilerGas") == 'kW'
    with pytest.raises(Exception):
        price.get_type_of_price_available(techno_choice="lililalal")


def test_price():
    price = Price()
    assert price.get_price(techno_choice="HeatPumpWaterSoil", price_choice="cost_machine", unit_size=50,
                           interp_choice=1) == 91111.111111111124
    # could not compute the spline by hands
    assert isinstance(price.get_price("PipeStreet", "CAPEX", 32, 'spline'), float)
    assert price.get_price(techno_choice="BoilerOil", price_choice="Maintenance", unit_size=20,
                           interp_choice='logarithm') - 371.503932 < 1e-5
    assert price.get_price(techno_choice="BoilerOil", price_choice="Maintenance", unit_size=20,
                           interp_choice=func_logarithm, bounds=([-np.inf, 0, -np.inf], np.inf)) - 371.503932 < 1e-5
    assert price.get_price_for_many_units(techno_choice="HeatPumpWaterSoil", price_choice="cost_machine",
                                          unit_size=[14, 11, 12], interp_choice=1) \
                                          == [30711.111111111135, 25677.777777777803, 27355.55555555558]
    with pytest.raises(Exception):
        price.get_price(techno_choice="BoilerOil", price_choice="xkcd", unit_size=20, interp_choice=func_logarithm)


def test_fig_price():
    # only test if the figure exists, not its quality
    price = Price()
    fig1 = price.create_fig_interpolation(techno_choice="BoilerOil", price_choice="maintenance",
                                          interp_choice=1, show=False)
    assert isinstance(fig1, plt.Figure)
    fig2 = price.create_fig_price(techno_choice="BoilerOil", price_choice="maintenance", show=False)
    assert isinstance(fig2, plt.Figure)
