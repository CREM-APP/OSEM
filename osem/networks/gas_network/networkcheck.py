import numpy as np
import networkx as nx
import operator
from thermo.chemical import Chemical
import fluids


class CheckNetwork():
    """
    This class performs different check on the quality of the network
    """

    def __init__(self, net):
        self.net = net
        self.pass_check = False

    def execute_check(self, type_of_check, *args, **kwargs):
        """
        This function distribute the different type of check to be done
        :param type_of_check: a string which indicates which check should be done
        """
        if type_of_check == 'unique_name':
            self.check_duplicates()
        elif type_of_check == 'connectivity':
            self.check_for_connectivity(*args, **kwargs)
        elif type_of_check == 'result':
            self.check_network_result(*args, **kwargs)
        elif type_of_check == 'all_load_full':
            self.check_for_empty_load(*args, **kwargs)
        else:
            raise ValueError("The type of the check to be done is not recognized.")

    def check_for_connectivity(self, pos=None, show=True):
        """
        This function checks if all the nodes of a pandangaz network are connected. No check for pressure.

        :param net: A pandangas network
        :param show: If True, show an image with the different network when more than one network.
        :return: True if all connectec, False otherwise
        """
        net_nx = self.net.netnx_all['all']
        sub_graphs = list(nx.connected_component_subgraphs(net_nx))
        nb_net = len(sub_graphs)
        if nb_net > 1:

            # plot the different network(optional)
            if show:
                self.net.net_plot._draw_separate_network(sub_graphs, pos)
            self.pass_check = False

        elif nb_net == 1:
           self.pass_check = True

        else:
            self.pass_check = False

    def check_network_result(self, lim_mass=1e-3, lim_pres=2):
        """
        checks if the result of a simulation makes sense. To this end, mass conservation and
        pressure conservation are computed. Self.net.res_bus must exists. It calls functions from
        the NetworkSimulation class.

        For the pressure, small error are accepted because the rounding error is summed on all nodes, all pipes
        so lim_pres should not be too small. To lower this error, lower net.solver_option['round_num']

        :param lim_mass: An acceptable error on the mass
        :param lim_pres: An acceptable error on the mass
        :return: True if network satisfy the conditions of mass and pressure conservation , False otherwise
        """

        # check conservation of mass
        if abs(self.net.res_bus["m_dot_kg/s"].sum()) > lim_mass:
            self.pass_check = False
        else:
            self.net.net_sim.multiply_pressure_matrix_to_check()
            res = self.net.net_sim.res_check

            if abs(res) > lim_pres:
                self.pass_check = False
            else:
                self.pass_check =True

    def check_for_empty_load(self, default_load=0):
        """
        Checks if there are pipes which are at the network ends without a load. If not, it changes these end pipes to a
        load of the default_load values. It can be useful to stabilize the solver.

        :param default_load: the load to add to end pipes without a load
        """
        # get all pipe at the end of the network
        once_in_to_bus = self.net.pipe.loc[self.net.pipe.groupby('to_bus').to_bus.transform(len) == 1, :]
        load_all = once_in_to_bus.loc[~once_in_to_bus.to_bus.isin(self.net.pipe['from_bus']), 'to_bus']

        # get what type is the end nodes
        type_bus_end = self.net.bus.loc[self.net.bus.index.isin(load_all), 'type']
        if 'NODE' in type_bus_end.values:
            load_to_be_corrected = type_bus_end.loc[type_bus_end.values == 'NODE']

            # correct load
            for i, li in enumerate(load_to_be_corrected.index):
                self.net.net_create.create_load(li, p_kW=default_load, name='ADDED_LOAD' + str(i))

            self.pass_check = False

        else:
            self.pass_check = True

    def check_duplicates(self):
        """
        checks for duplicate names in the network. Duplicate name results in unrealistic simulations.

        :return:
        """

        self.pass_check = True
        if np.any(self.net.bus.index.duplicated()):
            self.pass_check = False
        if np.any(self.net.bus.index.duplicated()):
            self.pass_check = False
        if np.any(self.net.bus.index.duplicated()):
            self.pass_check =False
        if np.any(self.net.bus.index.duplicated()):
            self.pass_check = False



