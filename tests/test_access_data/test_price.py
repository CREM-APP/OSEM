import matplotlib.pyplot as plt
import numpy as np
import pytest
from osef.access_data import Price
from osef.general.helper import func_log


def test_get_info_price():

    price = Price()
    assert price.get_technology_available() == ['BoilerPellet', 'BoilerGas', 'BoilerOil', 'HeatPumpAirWater',
                                                'HeatPumpWaterWater', 'HeatPumpWaterSoil', 'SeasonalStorage',
                                                'DailyStorageHt', 'DailyStorageLt', 'PipeStreet', 'PipeFields', 'PV',
                                                'CHP','SolarThermalPanel', 'IsolationRoof', 'IsolationWindows',
                                                'IsolationWall']

    assert price.get_type_of_price_available("seasonalstorage") == ['cost_machine', 'cost_installation','CAPEX',
                                                                    'maintenance']

    print(price.get_reference_for_price("DailyStorageHt", "cost_machine").values)
    assert price.get_reference_for_price("DailyStorageHt", "cost_machine").values[0] == 'viessmann catalogue, 2018'
    assert price.get_units("BoilerGas") == 'kW'
    with pytest.raises(Exception):
        price.get_type_of_price_available("lililalal")


def test_price():
    price = Price()
    assert price.get_price("HeatPumpWaterSoil", "cost_machine", 50, 1) == 91111.111111111124
    # could not compute the spline by hands
    assert isinstance(price.get_price("PipeStreet", "CAPEX", 32, 'spline'), float)
    assert price.get_price("BoilerOil", "Maintenance", 20, 'log') == 371.5027404869461
    assert price.get_price("BoilerOil", "Maintenance", 20, func_log, bounds=([-np.inf, 0, -np.inf], np.inf)) \
           == 371.5027404869461
    assert price.get_price_for_many_units("HeatPumpWaterSoil", "cost_machine", [14, 11, 12], 1) == [30711.111111111142,
                                                                                                    25677.77777777781,
                                                                                                    27355.555555555587]
    with pytest.raises(Exception):
        price.get_price("BoilerOil", "xkcd", 20, func_log)


def test_fig_price():
    # only test if the figure exists, not its quality
    price = Price()
    fig1 = price.create_fig_interpolation("BoilerOil", "maintenance", 1, show=False)
    assert isinstance(fig1, plt.Figure)
    fig2 = price.create_fig_price("BoilerOil", "maintenance", show=False)
    assert isinstance(fig2, plt.Figure)
