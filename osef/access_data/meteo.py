# this script loads and manage meteo data
import os
import pandas as pd

import osef.general.conf as conf

class Meteo:

    def __init__(self, year_id=None):

        # load data
        self._data_folder = conf.data_folder_meteo
        self._filenames = conf.filenames
        self._nbline_header = conf.nbline_header
        self._meteo_data = self._load_meteo_data()

    # find meteo station from coordinate

    def get_meteo_parameter(self):
        """

        :return: A list of string with the name of the parameter
        """

    def get_meteo_station(self, self_met_param):
        """
        This function get the meteorological station available for a particular meteorological parameter
        :param parameter:
        :return:
        """

    # list available parameter

    # get parameter for a year

    # get parameter for a month


    def _load_meteo_data(self):
        """
        This function loads the climatological data
        :return: A dictionary of Dataframe, one Dataframe by type of meteorological data
        """

        meteo_data = {}
        for f in self._filenames:
            key = os.path.splitext(f)[0]
            values = pd.read_csv(os.path.join(self._data_folder, f), header=self._nbline_header, sep='\t')
            meteo_data[key] = values

        return meteo_data

a = Meteo()
a._load_meteo_data()