import pandas as pd
import os
import json
import osem.general.conf as conf


class CreateNetwork:
    """
    A class which defines a gas network. It contains the class definition of a gas network and the methods used
    to create this network and its components.

    """

    def __init__(self, net):

        self.net = net

        # list of network component
        self.net.net_element_name = ["bus", "pipe", "load", "feeder", "station", "res_bus", "res_pipe",
                                 "res_feeder", "res_station"]

        # component of the network
        self.net.bus = pd.DataFrame(columns=["level", "zone", "type"])
        self.net.pipe = pd.DataFrame(columns=["from_bus", "to_bus", "length_m", "diameter_m", "material", "in_service"])
        self.net.load = pd.DataFrame(columns=["bus", "p_kW", "min_p_Pa", "scaling"])
        self.net.feeder = pd.DataFrame(columns=["bus", "p_lim_kW", "p_Pa"])
        self.net.station = pd.DataFrame(columns=["bus_high", "bus_low", "p_lim_kW", "p_Pa"])

        # resultat of the simulation by components
        self.net.res_bus = pd.DataFrame(columns=["p_Pa", "p_bar", "m_dot_kg/s", "p_kW"])
        self.net.res_pipe = pd.DataFrame(columns=["m_dot_kg/s", "v_m/s", "p_kW", "loading_%"])
        self.net.res_feeder = pd.DataFrame(columns=["m_dot_kg/s", "p_kW", "loading_%"])
        self.net.res_station = pd.DataFrame(columns=["m_dot_kg/s", "p_kW", "loading_%"])

    def _change_bus_type(self, bus, bus_type):
        """
        Bus can have three type: NODE, SRCE and LOAD. This function allows to change between these different type.

        :param bus: the bus of the network whoses type should be changed
        :param bus_type: the bus type

        """

        old_type = self.net.bus.loc[bus, "type"]
        try:
            assert old_type == "NODE"
        except AssertionError:
            msg = "The buses {} is already a {} !".format(bus, old_type)
            raise ValueError(msg)

        self.net.bus.loc[bus, "type"] = bus_type

    def _try_existing_bus(self, bus):
        """
        Checks if a bus exist on a given network, raise ValueError and log an error if not

        :param bus: the bus whose existence should be checked
        :return:
        """
        try:
            assert bus in self.net.bus.index
        except AssertionError:
            msg = "The bus {} does not exist !".format(bus)
            raise ValueError(msg)

    def _check_level(self, bus_a, bus_b, same=True):
        """
        Check the pressure level of two buses on a given network, raise ValueError and log an error depending on parameter

        :param net: the given network
        :param bus_a: the first bus
        :param bus_b: the second bus
        :param same: if True, the method will check if the node have the same pressure level
        if False, the method will check if the node have different pressure levels (default: True)
        :return:
        """
        lev_a = self.net.bus.loc[bus_a, "level"]
        lev_b = self.net.bus.loc[bus_b, "level"]

        if same:
            try:
                assert lev_a == lev_b
            except AssertionError:
                msg = "The buses {} and {} have a different pressure level !".format(bus_a, bus_b)
                raise ValueError(msg)
        else:
            try:
                assert lev_a != lev_b
            except AssertionError:
                msg = "The buses {} and {} have the same pressure level !".format(bus_a, bus_b)
                raise ValueError(msg)

    def create_bus(self, level, name, zone=None, check=True):
        """
        Creates a bus on a given network

        :param level: nominal pressure level of the bus
        :param name: name of the bus
        :param zone: zone of the bus (default: None)
        :param check: If True, check the integrity of the input
        :return: name of the bus
        """
        if check:
            if level not in self.net.levels:
                msg = "The pressure level of the bus {} is not in {}".format(name, self.net.levels)
                raise ValueError(msg)
            if name in self.net.bus.index:
                msg = "The bus {} already exists".format(name)
                raise ValueError(msg)

        self.net.bus.loc[name] = [level, zone, "NODE"]
        return name

    def create_pipe(self, from_bus, to_bus, length_m, diameter_m, name, material=conf.mat_default, in_service=True,
                    check=True):
        """
        Creates a pipe between two existing buses on a given network

        :param from_bus: the name of the already existing bus where the pipe starts
        :param to_bus: the name of the already existing bus where the pipe ends
        :param length_m: length of the pipe (in [m])
        :param diameter_m: inner diameter of the pipe (in [m])
        :param name: name of the pipe
        :param material: material of the pipe
        :param in_service: if False, the simulation will not take this pipe into account (default: True)
        :param check: If True, check the integrity of the input
        :return: name of the pipe
        """
        if check:
            self._try_existing_bus(from_bus)
            self._try_existing_bus(to_bus)
            self._check_level(from_bus, to_bus)
            if name in self.net.pipe.index:
                msg = "The pipe {} already exists".format(name)
                raise ValueError(msg)

        self.net.pipe.loc[name] = [from_bus, to_bus, length_m, diameter_m, material, in_service]
        return name

    def create_load(self, bus, p_kW, name, min_p_pa=conf.min_p_pa, scaling=conf.scaling):
        """
        Creates a load attached to an existing bus in a given network

        :param bus: the existing bus
        :param p_kW: power consumed by the load (in [kW])
        :param name: name of the load
        :param min_p_pa: minimum acceptable pressure
        :param scaling: scaling factor for the load (default: 1.0)
        :return: name of the load
        """

        self._try_existing_bus(bus)
        self.net.load.loc[name] = [bus, p_kW, min_p_pa, scaling]
        self._change_bus_type( bus, "SINK")
        return name

    def change_load(self, name_load_bus, p_kW, add=False, bybusname=False):
        """
        adds a load to an existing load. For example, it
        can be used if more than one house is connected to a network end.
        If add is True, the load is added to the old load and not directly changed.

        :param name_load_bus: the name of the bus or the load
        :param p_kW: float - power consumed by the load (in [kW])
        :param add: a boolean indicating if the new load is added to the old one (add=True) or directly changed (add=False)
        :param bybusname: If True, the load is identified by its bus name, not the name of the load
        :return: name of the load
        """
        if bybusname:
            self._try_existing_bus(name_load_bus)
            name_load = self.net.load.loc[self.load["bus"] == name_load_bus].index[0]
        else:
            name_load = name_load_bus

        if add:
            self.net.load.loc[name_load, 'p_kW'] += p_kW
        else:
            self.net.load.loc[name_load, 'p_kW'] = p_kW

        return name_load_bus

    def create_feeder(self, bus, p_lim_kW, p_Pa, name):
        """
        Creates a feeder attached to an existing bus in a given selfwork

        :param bus: the existing bus
        :param p_lim_kW: maximum power flowing through the feeder
        :param p_Pa: operating pressure level at the output of the feeder
        :param name: name of the feeder
        :return: name of the feeder
        """
        self._try_existing_bus(bus)

        self.net.feeder.loc[name] = [bus, p_lim_kW, p_Pa]
        self._change_bus_type(bus, "SRCE")
        return name

    def create_station(self, bus_high, bus_low, p_lim_kW, p_Pa, name):
        """
        Creates a pressure station between two existing buses on different pressure level in a given network

        :param bus_high: the existing bus with higher nominal pressure
        :param bus_low: the existing bus with lower nominal pressure
        :param p_lim_kW: maximum power flowing through the feeder
        :param p_Pa: operating pressure level at the output of the feeder
        :param name: name of the station
        :return: name of the station
        """

        self._try_existing_bus(bus_high)
        self._try_existing_bus( bus_low)
        self._check_level(bus_high, bus_low, same=False)

        self.net.station.loc[name] = [bus_high, bus_low, p_lim_kW, p_Pa]
        self.create_load(bus_high, 0, "STALOAD" + str(name))
        self._change_bus_type(bus_low, "SRCE")

        return name





