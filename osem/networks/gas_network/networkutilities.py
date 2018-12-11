
# this script contains helper function for the pandansgas network
import pandas as pd
import numpy as np
import os
import networkx as nx
import operator
import fluids
from thermo.chemical import Chemical


class UtilitiesNetwork:

    def __init__(self, net):

        self.net = net

    def erase_results(self):
        """
        erases the result of a simulation. Automatically done at a start of a new simulation.

        """
        self.net.res_bus.drop(self.net.res_bus.index, inplace=True)
        self.net.res_pipe.drop(self.net.res_pipe.index, inplace=True)
        self.net.res_feeder.drop(self.net.res_feeder.index, inplace=True)
        self.net.res_station.drop(self.net.res_station.index, inplace=True)

    def create_nxgraph_all_level(self, only_in_service=True):
        """
        create the networkx graphic linked to the current gas network
        :return:
        """

        self.net.netnx_all['all'] = self.create_nxgraph(None, only_in_service, directed=False)
        for level in self.net.levels.keys():
            self.net.netnx_all[level] = self.create_nxgraph(level, only_in_service, directed=True)

    def create_nxgraph(self, level=None, only_in_service=True, directed=True):
        """
        Convert a given network into a NetworkX MultiGraph for particular level or for all level if level is set to None.

        :param level: the name of pressure level of interest (string)
        :param only_in_service: if True, convert only the pipes that are in service (default: True)
        :param directed: If true, create a directed graph, otherwise undirected
        :return: a MultiGraph
        """

        if directed:
            g = nx.MultiDiGraph()
        else:
            g = nx.Graph()

        # create node
        if level is None:
            for idx, row in self.net.bus.iterrows():
                    g.add_node(row.name)
        else:
            for idx, row in self.net.bus.iterrows():
                if row[0] == level:
                    g.add_node(row.name)

        # create edge
        pipes = self.net.pipe
        if only_in_service:
            pipes = pipes.loc[pipes["in_service"]]
        for idx, row in pipes.iterrows():
            if row[0] in g.nodes() or row[1] in g.nodes():
                g.add_edge(row[0], row[1], name=row.name, type="PIPE", L_m=row[2], D_m=row[3], mat=row[4])

        # create edge at station if multi-level network
        if level is None:
            for idx, row in self.net.station.iterrows():
                g.add_edge(row[0], row[1], name=row.name, type="STATION")

        return g

    def create_empty_result(self):
        """
        creates a list of dataframe with all result value set to zeros

        :param net:
        :return: a net with res_bus, res_pipe, res_feeder and res_station at a value of zeros
        """

        self.net.res_bus = pd.DataFrame(0, index=self.net.bus.index, columns=self.net.res_bus.columns)
        self.net.res_pipe = pd.DataFrame(0, index=self.net.pipe.index, columns=self.net.res_pipe.columns)
        self.net.res_feeder = pd.DataFrame(0, index=self.net.feeder.index, columns=self.net.res_feeder.columns)
        self.net.res_station = pd.DataFrame(0, index=self.net.station.index, columns=self.net.res_station.columns)

    def save_gas_network(self, netname, pathdir=None, save_result=False):
        """
        saves a pandangaz network to csv files (one csv by dataframe in a folder)

        :param netname: the name under which the network should be saved (string)
        :param pathdir: the path where to save the file (by default current path)
        :param save_result: If True, save also the simulation results
        """

        # get path and save directory
        if pathdir is None:
            pathdir = os.path.join(os.getcwd(), netname)
        else:
            pathdir = os.path.join(pathdir, netname)
        if not os.path.isdir(pathdir):
            os.makedirs(pathdir)

        # save data
        dataframe_name = ['pipe.csv', 'bus.csv', 'load.csv', 'feeder.csv', 'station.csv']
        dataframe_val = [self.net.pipe, self.net.bus, self.net.load, self.net.feeder, self.net.station]
        for id, d in enumerate(dataframe_name):
            dataframe_val[id].to_csv(os.path.join(pathdir, d))

        # save result
        if save_result:
            dataframe_name = ['pipe_res.csv', 'bus_res.csv', 'feeder_res.csv', 'station_res.csv']
            dataframe_val = [self.net.res_pipe, self.net.res_bus, self.net.res_feeder, self.net.res_station]
            for id, d in enumerate(dataframe_name):
                dataframe_val[id].to_csv(os.path.join(pathdir, d))

    def load_gas_network(self, pathdir, get_result=False):
        """
        Load a pandangas network which was created though the save_pandangas_net() function.

        :param pathdir: the path to the folder
        :param get_result: If True also load the result of an old simulation
        """

        self.net.pipe = pd.read_csv(os.path.join(pathdir, 'pipe.csv'), index_col=0)
        self.net.bus = pd.read_csv(os.path.join(pathdir, 'bus.csv'), index_col=0)
        self.net.load = pd.read_csv(os.path.join(pathdir, 'load.csv'), index_col=0)
        self.net.feeder = pd.read_csv(os.path.join(pathdir, 'feeder.csv'), index_col=0)
        self.net.station = pd.read_csv(os.path.join(pathdir, 'station.csv'), index_col=0)

        if get_result:
            self.net.res_pipe = pd.read_csv(os.path.join(pathdir, 'pipe_res.csv'), index_col=0)
            self.net.res_bus = pd.read_csv(os.path.join(pathdir, 'bus_res.csv'), index_col=0)
            self.net.res_feeder = pd.read_csv(os.path.join(pathdir, 'feeder_res.csv'), index_col=0)
            self.net.res_station = pd.read_csv(os.path.join(pathdir, 'station_res.csv'), index_col=0)


# this function is commented as it would need two additional library which is a lot for OSEF
# import geopandas as gpd
# from shapely.geometry import Point, LineString
#
# def save_panandgas_as_shp(net, pos, netname, pathdir=None, crs=None):
#     """
#     This function save a pandagas as a shapefile
#     :param net: the pandas gas .net
#     :param pos: A dict with bus name as key and coordinate as value
#     :param netname: the name of the netpwork
#     :param path_dir: the path where to save the file (by default current path)
#     :param crs: the coordinate system of the file to save
#     """
#
#     # get path and save directory
#     if pathdir is None:
#         pathdir = os.path.join(os.getcwd(), netname)
#     else:
#         pathdir = os.path.join(pathdir, netname)
#     if not os.path.isdir(pathdir):
#         os.makedirs(pathdir)
#
#     # get the geometry for the bus
#     net.res_bus['geometry'] = None
#     for n in net.res_bus.index:
#         net.res_bus.loc[n, 'geometry'] = Point(pos[n])
#
#     # get the geometry for pipe
#     net.res_pipe['geometry'] = None
#     for n in net.res_pipe.index:
#         bus1 = net.pipe.loc[n, 'from_bus']
#         bus2 = net.pipe.loc[n, 'to_bus']
#         net.res_pipe.loc[n, 'geometry'] = LineString([pos[bus1], pos[bus2]])
#
#     # save bus
#     filebus = os.path.join(pathdir, netname + '_bus.shp')
#     net.res_bus = gpd.GeoDataFrame(net.res_bus, geometry='geometry')
#     if crs is not None:
#         net.res_bus.crs = crs
#     net.res_bus.to_file(filebus, driver='ESRI Shapefile')
#
#     # save pipes
#     filepipe = os.path.join(pathdir, netname + '_pipe.shp')
#     net.res_pipe = gpd.GeoDataFrame(net.res_pipe, geometry='geometry')
#     if crs is not None:
#         net.res_pipe.crs = crs
#     net.res_pipe.to_file(filepipe, driver='ESRI Shapefile')








