import network_for_test
import osem.networks.gas_network.networkinterface as pg
import os


def test_runpg():
    net = network_for_test.model_gas_test()
    pg.simulate_network_all_pressure_level(net)
    assert len(net.res_bus.index) == 5
    assert pg.check_network(net, type_of_check='result', lim_mass=1, lim_pres=2) == True


def test_runpg2():
    net = network_for_test.model_gas_test2()
    pg.set_solver_option(net, solver_option={'round_num': 5})
    pg.simulate_network_all_pressure_level(net)
    assert len(net.res_bus.index) == 3
    assert pg.check_network(net, 'result', lim_mass=1, lim_pres=2) == True
    assert net.res_bus.at["BUS2", "p_Pa"] == 2487.08901


def test_runpg3():
    net = network_for_test.model_with_two_feeder()
    pg.simulate_network_all_pressure_level(net)
    assert len(net.res_bus.index) == 3
    assert pg.check_network(net, 'result', lim_mass=1, lim_pres=2) == True


def test_check_for_network():
    net = network_for_test. model_with_eight_bus(all_load_added=True)
    pg.simulate_network_all_pressure_level(net)
    assert pg.check_network(net, 'connectivity') == True
    assert pg.check_network(net, 'unique_name') == True
    assert pg.check_network(net, 'all_load_full') == True
    net2 = network_for_test.model_with_eight_bus(all_load_added=False)
    assert pg.check_network(net2, 'all_load_full') == False

def test_len_of_created_df():
    net = network_for_test.model_gas_test()
    pg.simulate_network_all_pressure_level(net)
    assert len(net.res_bus.index) == 5
    assert len(net.res_pipe.index) == 4
    assert len(net.res_feeder.index) == 1
    assert len(net.res_station.index) == 1

def test_figure():
    net = network_for_test.model_gas_test()
    pg.draw_network(net,show=False)
    pg.simulate_network_all_pressure_level(net)
    pg.draw_network_result(net, show=False)


def test_columns_of_created_df():
    net = network_for_test.model_gas_test()
    pg.simulate_network_all_pressure_level(net)
    assert set(net.res_bus.columns) == {"p_Pa", "p_bar", "m_dot_kg/s","p_kW"}
    assert set(net.res_pipe.columns) == {"m_dot_kg/s","v_m/s","p_kW","loading_%"}
    assert set(net.res_feeder.columns) == {"m_dot_kg/s", "p_kW", "loading_%"}
    assert set(net.res_station.columns) == {"m_dot_kg/s", "p_kW", "loading_%"}
