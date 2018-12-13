import pytest

import osem.networks.pandangas.network_for_test as network_for_test
import osem.networks.pandangas.network_creation as pg


def test_len_of_created_df():
    net = network_for_test.model_gas_test()
    assert len(net.bus.index) == 5
    assert len(net.pipe.index) == 4
    assert len(net.load.index) == 3
    assert len(net.feeder.index) == 1
    assert len(net.station.index) == 1


def test_columns_of_created_df():
    net = network_for_test.model_gas_test()
    assert set(net.bus.columns) == {"level", "zone", "type"}
    assert set(net.pipe.columns) == {"from_bus","to_bus","length_m", "diameter_m","material","in_service"}
    assert set(net.load.columns) == {"bus", "p_kW", "min_p_Pa", "scaling"}
    assert set(net.feeder.columns) == {"bus", "p_lim_kW", "p_Pa"}
    assert set(net.station.columns) == {"bus_high","bus_low","p_lim_kW","p_Pa"}


def test_bus_creation_bad_bus_level_raise_exception():
    net = network_for_test.model_gas_test()
    with pytest.raises(ValueError) as e_info:
        pg.create_bus(net, level="XX", name="BUSX")
        msg = "The pressure level of the bus BUSX is not in {}".format(
            ["HP", "MP", "BP+", "BP"]
        )
        assert e_info.value.message == msg
    assert len(net.bus.index) == 5


def test_pipe_creation_non_existing_bus_raise_exception():
    net =  network_for_test.model_gas_test()
    with pytest.raises(ValueError) as e_info:
        pg.create_pipe(net, "BUS1", "BUSX", length_m=100, diameter_m=0.05, name="PIPEX")
        msg = "The bus {} does not exist !".format("BUSX")
        assert e_info.value.message == msg
    assert len(net.pipe.index) == 4


def test_pipe_creation_different_levels_raise_exception():
    net = network_for_test.model_gas_test()
    with pytest.raises(ValueError) as e_info:
        pg.create_pipe(net, "BUS0", "BUS1", length_m=100, diameter_m=0.05, name="PIPEX")
        msg = "The buses BUS0 and BUS1 have a different pressure level !"
        assert e_info.value.message == msg
    assert len(net.pipe.index) == 4


def test_station_creation_same_level_raise_exception():
    net =  network_for_test.model_gas_test()
    with pytest.raises(ValueError) as e_info:
        pg.create_station(
            net, "BUS2", "BUS3", p_lim_kW=50, p_Pa=0.025E5, name="STATION"
        )
        msg = "The buses BUS2 and BUS3 have the same pressure level !"
        assert e_info.value.message == msg
    assert len(net.station.index) == 1


def test_network_repr():
    net =  network_for_test.model_gas_test()
    assert "This pandangas network includes the following parameter tables:" in repr(
        net
    )
    assert "- bus (5 elements)" in repr(net)
    assert "and the following results tables:" not in repr(net)
