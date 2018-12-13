

import osem.networks.pandangas.run_simulation as pg_run
import osem.networks.pandangas.network_for_test as network_for_test
import osem.networks.pandangas.utilities as pg_uti

def test_runpg():
    net = network_for_test.model_gas_test()
    pg_run.runpg(net)
    assert len(net.res_bus.index) == 5
    assert pg_uti.check_network_result(net, lim_mass=1, lim_pres=2) == True


def test_runpg2():
    net = network_for_test.model_gas_test2()
    pg_run.runpg(net)
    assert len(net.res_bus.index) == 3
    assert pg_uti.check_network_result(net, lim_mass=1, lim_pres=2) == True
    assert net.res_bus.at["BUS2", "p_Pa"] == 2487.08901


def test_runpg3():
    net = network_for_test.model_with_two_feeder()
    pg_run.runpg(net)
    assert len(net.res_bus.index) == 3
    assert pg_uti.check_network_result(net, lim_mass=1, lim_pres=2) == True


def test_len_of_created_df():
    net = network_for_test.model_gas_test()
    pg_run.runpg(net)
    assert len(net.res_bus.index) == 5
    assert len(net.res_pipe.index) == 4
    assert len(net.res_feeder.index) == 1
    assert len(net.res_station.index) == 1


def test_columns_of_created_df():
    net = network_for_test.model_gas_test()
    pg_run.runpg(net)
    assert set(net.res_bus.columns) == {"p_Pa", "p_bar", "m_dot_kg/s","p_kW"}
    assert set(net.res_pipe.columns) == {"m_dot_kg/s","v_m/s","p_kW","loading_%"}
    assert set(net.res_feeder.columns) == {"m_dot_kg/s", "p_kW", "loading_%"}
    assert set(net.res_station.columns) == {"m_dot_kg/s", "p_kW", "loading_%"}
