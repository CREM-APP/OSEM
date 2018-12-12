# this list of function provide an interface to the class GasNetwork which ressembles the interface from pandaspower.
# So we can have a gas model with an API similair to a model for electricity network, which is useful for the
#  co-simulation

import osem.networks.gas_network.networkbase as networkbase
import osem.general.conf as conf


def create_empty_network():
    """
    Creates an empty network.

    Here is an example of usage to fill in this empty network:

    .. highlight:: python
    .. code-block:: python

        import osef.network.gas_network as pg

        net = pg.create_empty_network()

        busf = pg.create_bus(net, level="MP", name="BUSF")
        bus0 = pg.create_bus(net, level="MP", name="BUS0")

        bus1 = pg.create_bus(net, level="BP", name="BUS1")
        bus2 = pg.create_bus(net, level="BP", name="BUS2")
        bus3 = pg.create_bus(net, level="BP", name="BUS3")

        pg.create_load(net, bus2, p_kW=10.0, name="LOAD2")
        pg.create_load(net, bus3, p_kW=13.0, name="LOAD3")

        pg.create_pipe(net, busf, bus0, length_m=100, diameter_m=0.05, name="PIPE0")
        pg.create_pipe(net, bus1, bus2, length_m=400, diameter_m=0.05, name="PIPE1")
        pg.create_pipe(net, bus1, bus3, length_m=500, diameter_m=0.05, name="PIPE2")
        pg.create_pipe(net, bus2, bus3, length_m=500, diameter_m=0.05, name="PIPE3")

        pg.create_station(net, bus0, bus1, p_lim_kW=50, p_Pa=0.025E5, name="STATION")
        pg.create_feeder(net, busf, p_lim_kW=50, p_Pa=0.9E5, name="FEEDER")

    :return: a Network object that will later contain all the buses, pipes, etc.

    """

    net = networkbase.GasNetwork()

    return net


def simulate_network_all_pressure_level(net):
    """
    used to run a pandangas simulation. In other word, this is the main function to call to use this module
    after having created a natural gas network.
    """

    net.simulate_network_all_pressure_level()

    return net


def create_bus(net, level, name, zone=None, check=True):
    """
    Creates a bus on a given network

    :param net: the given network
    :param level: nominal pressure level of the bus
    :param name: name of the bus
    :param zone: zone of the bus (default: None)
    :param check: If True, check the integrity of the input
    :return: name of the bus

    """

    name = net.create_bus(level, name, zone, check)
    return name


def create_pipe(net, from_bus, to_bus, length_m, diameter_m, name, material=conf.mat_default,
                in_service=True, check=True):

    """
    Creates a pipe between two existing buses on a given network

    :param net: the given network
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
    name = net.create_pipe(from_bus, to_bus, length_m, diameter_m, name, material, in_service, check)
    return name


def create_station(net, bus_high, bus_low, p_lim_kW, p_Pa, name):
    """
    Creates a pressure station between two existing buses on different pressure level in a given network

    :param net: the given network
    :param bus_high: the existing bus with higher nominal pressure
    :param bus_low: the existing bus with lower nominal pressure
    :param p_lim_kW: maximum power flowing through the feeder
    :param p_Pa: operating pressure level at the output of the feeder
    :param name: name of the station
    :return: name of the station
    """
    name = net.create_station(bus_high, bus_low, p_lim_kW, p_Pa, name)
    return name


def create_feeder(net, bus, p_lim_kW, p_Pa, name):
    """
    Creates a feeder attached to an existing bus in a given network

    :param net: the given network
    :param bus: the existing bus
    :param p_lim_kW: maximum power flowing through the feeder
    :param p_Pa: operating pressure level at the output of the feeder
    :param name: name of the feeder
    :return: name of the feeder
    """
    name = net.create_feeder(bus, p_lim_kW, p_Pa, name)
    return name


def create_load(net, bus, p_kW, name, min_p_pa=conf.min_p_pa, scaling=conf.scaling):
    """
    Creates a load attached to an existing bus in a given network

    :param net: the given network
    :param bus: the existing bus
    :param p_kW: power consumed by the load (in [kW])
    :param name: name of the load
    :param min_p_pa: minimum acceptable pressure
    :param scaling: scaling factor for the load (default: 1.0)
    :return: name of the load
    """

    name = net.create_load(bus, p_kW, name, min_p_pa, scaling)
    return name


def change_load(net, name_load_bus, p_kW, add=False, bybusname=False):
    """
    adds a load to an existing load. For example, it
    can be used if more than one house is connected to a network end.
    If add is True, the load is added to the old load and not directly changed.

    :param net: the given pandangas network
    :param name_load_bus: the name of the bus or the load
    :param p_kW: float - power consumed by the load (in [kW])
    :param add: a boolean indicating if the new load is added to the old one (add=True) or directly changed (add=False)
    :param bybusname: If True, the load is identified by its bus name, not the name of the load
    :return: name of the load
    """
    name = net.change_load(name_load_bus, p_kW, add, bybusname)
    return name


def set_pressure_level(net,levels):
    """
    sets the pressure levels of pandangas network. The pressure levels are in Pascal.

    :param net: a pandangas network
    :param levels: a dictionnary where the keys are the name of the pressure level and the keys the value.
    """

    net.set_pressure_level(levels)

    return net


def set_temperature(net, temp, celsius=False):
    """
    sets the exterior temperature of the network

    :param net: a pandangas network
    :param temp: the temperature in Celsius or Kelvin
    :param celsius: if True, the temperature is in Celsius,  otherwise it is in Kelvin
    """
    net.set_temperature(temp, celsius)
    return net


def set_exterior_pressure(net, p_atm):
    """
    sets the exterior pressure of the network in Pascal

    :param net: a pandangas network
    :param p_atm: the exterior pression (Pa)
    """
    net.set_exterior_pressure(p_atm)
    return net


def set_solver_option(net, solver_option=None):
    """
    sets the solver option used to solve the equations.

    :param solver_option: the dict given by the user with custom options, no need to give all options.
    """

    net.set_solver_option(solver_option)
    return net


def get_solver_info(net):
    """
     prints the information related to the solver options.
    """
    print(net.solver_option)


def check_network(net, type_of_check, *args,**kwargs):
    """
    This method can be used to check the quality of the network. The check needed is given in argument.
    Currently the accepted value are: 'unique_name', 'connectivity', 'result', and 'all_load_full'.

    No additional argument are necessary, but optional argument are given in the class NetworkCheck for finer control.

    :param type_of_check: a string which indicates the check needed
    :return: True if the check is ok, False other wise
    """

    pass_check = net.check_network(type_of_check, *args, **kwargs)

    return pass_check


def draw_network(net, pos=None, show=True):
    """
    plots a gas network before the simulation.

    :param pos: The coordinates of the node (optional)
    :param show: If True, it will show the figure now
    """

    net.draw_network(pos, show)


def draw_network_result(net, pos=None, show=True, maxloading=300):
    """
   plot the outputs from a gas nework simulation.

   :param pos: The coordinates of the node (optional)
   :param show: If True, the result are shown
   :param maxloading: for the colorbar, the max of the load (sometimes there are short pipe with high load)
   """

    net.draw_network_result(pos, show, maxloading)


def save_network(net,netname, pathdir=None, save_result=False):
    """
    saves a pandangaz network to csv files (one csv by dataframe in a folder)

    :param netname: the name under which the network should be saved (string)
    :param pathdir: the path where to save the file (by default current path)
    :param save_result: If True, save also the simulation results
    """

    net.save_network(netname, pathdir, save_result)


def load_network(net, pathdir, get_result):
    """
    Load a pandangas network which was created though the save_pandangas_net() function.

    :param pathdir: the path to the folder
    :param get_result: If True also load the result of an old simulation
    """

    net.load_network(self, pathdir, get_result)


