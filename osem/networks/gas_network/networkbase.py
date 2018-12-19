import osem.general.conf as conf
import osem.networks.gas_network.networkcreate as networkcreate
import osem.networks.gas_network.networksimulation as networksimulation
import osem.networks.gas_network.networkcheck as networkcheck
import osem.networks.gas_network.networkdraw as networkdraw
import osem.networks.gas_network.networkutilities as networkutilities
import osem.networks.gas_network.solveroption as solveroption

import operator
import numpy as np


class GasNetwork:
    """
    A class which defines a gas network. It contains the class definition of a gas network and the methods used
    to create this network and its components.

    """

    def __init__(self):

        # data
        self._data_folder = conf.data_folder

        # default value
        self.levels = conf.default_levels  # Pa
        self.lhv = conf.lhv
        self.v_max = conf.v_max
        self.temperature = conf.temperature  # K
        self.p_atm = conf.p_atm  # Pa
        self.corr_pnom = conf.corr_pnom  # Pa

        # netowrkx graph for each pressure level
        self.netnx_all = {}

        # helper class
        self.net_create = networkcreate.CreateNetwork(self)
        self.net_uti = networkutilities.UtilitiesNetwork(self)
        self.net_check = networkcheck.CheckNetwork(self)
        self.net_plot = networkdraw.DrawNetwork(self)
        self.net_sim = networksimulation.SimulationNetwork(self)
        self.solver_option = solveroption.SolverOption()

    def simulate_network_all_pressure_level(self):
        """
        used to run a pandangas simulation. In other word, this is the main function to call to use this module
        after having created a natural gas network.
        """

        # prepare simulation
        self.net_uti.erase_results()
        self.net_uti.create_empty_result()
        self.net_check.check_duplicates()

        # order level
        sorted_levels = sorted(self.levels.items(), key=operator.itemgetter(1))

        # create nx graph for all level
        self.net_uti.create_nxgraph_all_level()

        # pass through each level
        for level, value in sorted_levels:
            if level in self.bus["level"].unique():
                # run simulation for one pressure level
                print("Compute level {}".format(level))
                self.net_sim.run_sim_by_level(level)

    def create_bus(self, *args,**kwargs):
        """
        call create_bus function from the CreateNetowrk class
        :param args:
        """
        name = self.net_create.create_bus(*args, **kwargs)
        return name

    def create_pipe(self, *args,**kwargs):
        """
        call create_pipe function from the CreateNetwork class
        """
        name = self.net_create.create_pipe(*args,**kwargs)
        return name

    def create_station(self, *args,**kwargs):
        """
        call create_station function from the CreateNetwork class
        """
        name = self.net_create.create_station(*args,**kwargs)
        return name

    def create_feeder(self, *args,**kwargs):
        """
        call create_feeder from the CreateNetwork class
        """
        name = self.net_create.create_feeder(*args,**kwargs)
        return name

    def create_load(self, *args, **kwargs):
        """
        call create_load from the CreateNetwork class
        """
        name = self.net_create.create_load(*args, **kwargs)
        return name

    def change_load(self, *args, **kwargs):
        """
        call change_load from the CreateNetwork class
        """
        name = self.net_create.change_load(*args, **kwargs)
        return name

    def set_pressure_level(self,levels):
        """
        sets the pressure levels of pandangas network. The pressure levels are in Pascal.

        :param net: a pandangas network
        :param levels: a dictionnary where the keys are the name of the pressure level and the keys the value.
        """

        self.levels = levels

    def set_temperature(self, temp, celsius=False):
        """
        sets the exterior temperature of the network

        :param net: a pandangas network
        :param temp: the temperature in Celsius or Kelvin
        :param celsius: if True, the temperature is in Celsius,  otherwise it is in Kelvin
        """
        if celsius:
            self.temperature = temp + 273.15
        else:
            self.temperature = temp

    def set_exterior_pressure(self, p_atm):
        """
        sets the exterior pressure of the network in Pascal

        :param net: a pandangas network
        :param p_atm: the exterio pression (Pa)
        """
        self.p_atm = p_atm

    def set_solver_option(self, solver_option=None):
        """
        sets the solver option used to solve the equations.

        :param solver_option: the dict given by the user with custom options, no need to give all options.
        """

        self.solver_option.set_solver_option(solver_option)

    def get_solver_info(self):
        """
         prints the information related to the solver options.
        """
        print(self.solver_option)

    def check_network(self, type_of_check, *args,**kwargs):
        """
        This method can be used to check the quality of the network. The check needed is given in argument.
        Currently the accepted value are: 'unique_name', 'connectivity', 'result', and 'all_load_full'.

        :param type_of_check: a string which indicates the check needed
        :return: True if the check is ok, False other wise
        """

        if len(self.pipe) > 1:
            self.net_uti.create_nxgraph_all_level()
        self.net_check.execute_check(type_of_check,*args,**kwargs)

        return self.net_check.pass_check

    def draw_network(self, pos=None, show=True):
        """
        plots a gas network before the simulation.

        :param pos: The coordinates of the node (optional)
        :param show: If True, it will show the figure now
        """
        if len(self.pipe) > 1:
            self.net_uti.create_nxgraph_all_level()
        self.net_plot.draw_network_gas(pos, show)

    def draw_network_result(self, pos=None, show=True, maxloading=300):
        """
       plot the outputs from a gas nework simulation.

       :param pos: The coordinates of the node (optional)
       :param show: If True, the result are shown
       :param maxloading: for the colorbar, the max of the load (sometimes there are short pipe with high load)
       """

        if len(self.pipe) > 1:
            self.net_uti.create_nxgraph_all_level()

        if len(self.res_bus) > 1:
            self.net_plot.draw_results(pos, show, maxloading)
        else:
            self.net_plot.draw_network_gas(pos, show)

    def save_network(self,netname, pathdir=None, save_result=False):
        """
        saves a pandangaz network to csv files (one csv by dataframe in a folder)

        :param netname: the name under which the network should be saved (string)
        :param pathdir: the path where to save the file (by default current path)
        :param save_result: If True, save also the simulation results
        """

        self.net.net_uti.save_gas_network(netname, pathdir, save_result)

    def load_network(self, pathdir, get_result=False):
        """
        Load a pandangas network which was created though the save_pandangas_net() function.

        :param pathdir: the path to the folder
        :param get_result: If True also load the result of an old simulation
        """

        self.net.net_uti.load_gas_network(pathdir, get_result)

    def get_data_by_edge(self, level, data_type):
        """
        returns the data ordered as the edge of the network for particular pressure level, for a particular data_type

        :param netnx: the graph
        :param data_type: the type of data need
        :return: an np.array with the data ordered as in the edge
        """
        data_by_edge = np.array([data[data_type] for _, _, data in self.netnx_all[level].edges(data=True)])

        return data_by_edge

    def __repr__(self):
        """
        implementation of the print function
        """
        r = "This pandangas network includes the following parameter tables:"
        par = []
        res = []
        for tb in self.net_element_name:
            if len(getattr(self, tb)) > 0:
                if "res_" in tb:
                    res.append(tb)
                else:
                    par.append(tb)
        for tb in par:
            length = len(getattr(self, tb))
            r += "\n   - %s (%s %s)" % (
                tb,
                length,
                "elements" if length > 1 else "element",
            )
        if res:
            r += "\n and the following results tables:"
            for tb in res:
                length = len(getattr(self, tb))
                r += "\n   - %s (%s %s)" % (
                    tb,
                    length,
                    "elements" if length > 1 else "element",
                )

        return r

if __name__ == "__main__":
    # execute only if run as a script
    model_gas_test2()

