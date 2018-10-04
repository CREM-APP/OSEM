import pandas as pd
import numpy as np
import os

import osef.general.conf as conf
from osef.access_data.kbob import Kbob
from osef.access_data.price import Price
from osef.general.helper import find_string

class Kpi:
    """
    Ths class compute different kpi
    """

    def __init__(self):

        # link to external data
        self._data_folder = conf.data_folder
        self._kbob = Kbob()
        self._price = Price()

        # efficiency
        self._filename_eff = conf.filename_eff
        self._data_efficiency = self._load_efficiency_data
        self._cutoff = conf.cutoff

        # heating temperature of buildings
        self.temp_building = conf.temp_building  # might be more than one temperature
        self._temp_ext = conf.temp_ext

    def _load_efficiency_data(self):
        """
        This function load the efficiency data
        """

        filename_eff = os.path.join(self._data_folder, self._filename_eff)
        data_efficiency = pd.read_csv(filename_eff, index_col=0)

        return data_efficiency

    def _get_efficiency(self, tech_name,temp_build=None):
        """
        This function return the efficiency of a technology, to pass from final to primary. For an heat pump,
        the efficiency account for the building temperature through Carnot.
        :param tech_name: the name of the technology
        :param temp_build:
        :return:
        """
        # temperature of the building
        if temp_build is not None:
            self.temp_build = temp_build
        self.temp_build = np.array(self.temp_build)

        # get correct name
        tech_name = find_string(tech_name, tech_name.index, cutoff=self._cutoff)

        # get efficiency, account for Carnot for the heat pumps
        eff = self._data_efficiency.loc[tech_name, "efficiency"]
        if 'heat' in tech_name and 'pump' in tech_name:
            carnot = (self.temp_build[:,1] + 273.15) / np.abs(self.temp_build[:,1] - self._temp_ext)
            eff = eff * np.sum(carnot * self.temp_build[:,0]/100)

        return eff

    def get_co2_emission(self, data_heating):
        """
        This function compute c02 emission of different heating technology based on useful energy
        :param data_heating: A dataframe with the following columns: scenario, year, <technology 1>, <technology 2>,...
        :return: a Dataframe with the c02 emission by technology by year by scenarios in kg
        """

        # compute co2
        co2_emi = _create_empty_output(data_heating)
        for tech_name in co2_emi.columns[2:]:
            co2_rate = self._kbob.get_value(tech_name, 'CO2', language="ENG", ener_type='useful')
            co2_emi[tech_name] = co2_rate * data_heating[tech_name]

        return co2_emi

    def get_renewable_part(self, data_heating):
        """
        The function computes the part of renewable energy from different technology based on useful energy.
        :param data_heating: A dataframe with the following columns: scenario, year, <technology 1>, <technology 2>,...
        :return: a Dataframe with the renewable energy by technology by year by scenarios in kWh
        """

        # create the output dataframe
        renewable =  _create_empty_output(data_heating)
        # compute renewable
        for tech_name in renewable.columns[2:]:
            renew_per = self._kbob.get_value(tech_name, 'EP_Renew', language="ENG", ener_type='useful')
            renewable[tech_name] = (renew_per/100) * data_heating[tech_name]

        return renewable


    def get_energy_final(self, ):
        pass

    def get_energy_primary(self, data_heating):
        """
       The function computes the primary energy from different technology based on useful energy.
       :param data_heating: A dataframe with the following columns: scenario, year, <technology 1>, <technology 2>,...
       :return: a Dataframe with the primary energy by technology by year by scenarios in kWh
       """

        # create the output dataframe
        primary_ener = _create_empty_output(data_heating)
        # compute renewable
        for tech_name in primary_ener .columns[2:]:
            primary_coeff = self._kbob.get_value(tech_name, 'EP_Global', language="ENG", ener_type='useful')
            primary_ener[tech_name] = primary_coeff * data_heating[tech_name]

        return primary_ener

    def set_ext_temp(self, temp_ext):
        """
        To set the exterior temperature for the efficiency of the heat pumps
        :param temp_ext: the exteriot temperature in Celsius
        """
        self._temp_ext = temp_ext

    def get_opex(self,):
        pass

    def get_capex(self,):
        pass

    def get_time_investement_return(self):
        pass


 def _create_empty_output(self,data_heating):
        """
        This function create an empty dataframe with years and scenario which is used to return kpi data after the
        commutation
        :param data_heating: A dataframe with the following columns: scenario, year, <technology 1>, <technology 2>,...
        :return: a Dataframe with empty column and one column with the year and one column with the scenarios
        """

        # create the output dataframe
        empty_output = pd.DataFrame(0, index=data_heating.index, columns=data_heating.columns)
        empty_output['years'] = data_heating['years']
        empty_output['scenarios'] = data_heating['scenarios']

        return empty_output

