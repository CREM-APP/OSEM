import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np
import networkx as nx

class DrawNetwork():

    def __init__(self, net):
        self.net = net

    def draw_network_gas(self, pos=None, show=True):
        """
        plots a gas network before the simulation.

        :param pos: The coordinates of the node (optional)
        :param show: If True, it will show the figure now
        """
        # prepare a network for plotting
        net_draw = self.net.netnx_all['all']
        bus_load = self.net.bus.loc[self.net.bus['type'] == 'SINK', :].index.tolist()
        bus_feeder = self.net.bus.loc[self.net.bus['type'] == 'SRCE', :].index.tolist()
        name_feeder_sta = {k:v for (k,v) in zip(bus_feeder, bus_feeder)}

        # position of the nodes
        if not pos:
            pos = nx.spring_layout(net_draw)

        # plot
        plt.figure()
        try:
            nx.draw(net_draw, pos, node_size=2, node_color='black', label='Node', with_labels=False, font_size=12)
        except ValueError:
            print('ValueError: you might have pipes with NULL position.')
        nx.draw_networkx_nodes(net_draw, pos,
                               nodelist=bus_load,
                               node_color='r',
                               node_size=10,
                               label='Load')
        nx.draw_networkx_nodes(net_draw, pos,
                               nodelist=bus_feeder,
                               node_color='g',
                               node_size=10,
                               label='Feeders and Stations')
        nx.draw_networkx_labels(net_draw, pos, labels=name_feeder_sta)
        plt.legend()

        if show:
            plt.show()

    def draw_results(self, pos=None, show=True, maxloading=300):
        """
        plot the outputs from a pandangaz model.

        :param pos: The coordinates of the node (optional)
        :param show: If True, the result are shown
        :param maxloading: for the colorbar, the max of the load (sometimes there are short pipe with high load)
        """
        # prepare a network for plotting
        net_draw = self.net.netnx_all['all']

        # order output
        res_bus_ordered = self.net.res_bus
        res_bus_ordered = res_bus_ordered.reindex(net_draw.nodes())
        order_edge = [data['name'] for (u, v, data) in net_draw.edges(data=True)]
        res_pipe_ordered = self.net.res_pipe
        res_pipe_ordered = res_pipe_ordered.reindex(order_edge)

        # get the result for mass and pressure
        mass_res = res_pipe_ordered['m_dot_kg/s'].values
        loading = res_pipe_ordered['loading_%'].values
        pressure_nodes = res_bus_ordered['p_Pa'].values
        mass_nodes = np.abs(res_bus_ordered["m_dot_kg/s"].values)

        # position of the nodes
        if not pos:
            pos = nx.spring_layout(net_draw)
        cmap = plt.cm.get_cmap('jet')

        # plot the loads
        plt.figure()
        vmin = min(loading)
        vmax = maxloading
        plt.title('Pipe Loading')
        try:
            nx.draw(net_draw, pos, node_size=1, node_color='black', edge_color=loading,
                        edge_cmap=cmap, width=3, with_labels=False, font_size=12,edge_vmin=vmin,edge_vmax=vmax)
        except ValueError:
            print('ValueError: you might have pipes with NULL position.')
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
        sm.set_array([])
        cbar = plt.colorbar(sm, shrink=.6)
        cbar.set_label('Load [%]', rotation=270, labelpad=15)
        plt.legend()

        # plot the mass in the pipe
        plt.figure()
        vmin = min(mass_res)
        vmax = max(mass_res)
        plt.title('Mass in pipe')
        try:
            nx.draw(net_draw, pos, node_size=1, node_color='black', edge_color=mass_res,
                    edge_cmap=cmap, width=3, with_labels=False, font_size=12, edge_vmin=vmin, edge_vmax=vmax)
        except ValueError:
            print('ValueError: you might have pipes with NULL position.')
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
        sm.set_array([])
        cbar = plt.colorbar(sm, shrink=.6)
        cbar.set_label('Discharge mass [kg/sec]', rotation=270, labelpad=15)
        plt.legend()

        # plot the pressure in the nodes
        plt.figure()
        vmin = min(pressure_nodes)
        vmax = max(pressure_nodes)+1
        plt.title('Pressure - Gas Nodes')
        nx.draw_networkx(net_draw, pos, node_size=30, node_color=pressure_nodes, cmap=cmap, with_labels=False, font_size=12,
                vmin=vmin, vmax=vmax)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
        sm.set_array([])
        cbar = plt.colorbar(sm, shrink=.6)
        cbar.set_label('Pressure [Pa]', rotation=270, labelpad=15)
        plt.legend()

        # plot the mass in the nodes
        vmin = min(mass_nodes)
        vmax = max(mass_nodes)
        cmap = plt.cm.get_cmap('bwr')
        plt.figure()
        plt.title('Discharge Mass Nodes')
        nx.draw_networkx(net_draw, pos, node_size=10, node_color=mass_nodes, cmap=cmap, with_labels=False, font_size=12,
                         vmin=vmin, vmax=vmax)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
        sm.set_array([])
        cbar = plt.colorbar(sm, shrink=.6)
        cbar.set_label('Discharge mass [kg/sec]', rotation=270, labelpad=15)
        plt.legend()

        if show:
            plt.show()

    def _draw_separate_network(self, sub_graphs, pos=None):
        """
        Draw each connected sub-networkk in a different colors. Useful for the metho check_connectivity.
        """

        net_nx = self.net.netnx_all['all']
        if not pos:
            pos = nx.spring_layout(net_nx)
        colors = list(mcolors.cnames)[9:] * 100  # avoid very light color at the start
        plt.figure()
        plt.title('Sub-networks')
        for iss, s in enumerate(sub_graphs):
            nx.draw(s, pos, node_size=1)
            if s.number_of_nodes() > 200:
                label = 'Number of nodes: ' + str(s.number_of_nodes())
                nx.draw_networkx_nodes(s, pos, node_size=10, node_color=colors[iss], label=label)
            else:
                nx.draw_networkx_nodes(s, pos, node_size=10, node_color=colors[iss])
        plt.xlabel('x-coordinate [m]')
        plt.ylabel('y-coordinate [m]')
        plt.show()



