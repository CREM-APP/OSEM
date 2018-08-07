import os
import pandas as pd
import numpy as np
from osef.general.helper import find_string
import osef.general.conf as conf


class Price:
    """
    This class loads and manipulate the price data
    """

    def __init__(self):

        # parameter
        self._data_folder = conf.data_folder
        self._cutoff = conf.cutoff
        self._precision = conf.precision_price
        self._basename_price = conf.basename_price

        # load data
        self.db_price = pd.read_csv(os.path.join(self._data_folder, self._basename_price), sep=";")
        self.db_price.set_index("technology", inplace=True)

    def price_total(self, tech_choice, size_unit):
        """
        This function calculate the price of the technology chosen by the user for the size of unit given
        :param tech_choice: string - the technology chosen
        :param size_unit: float - the number of unit or the power of the installation
        """
        # get the chosen technology
        tech_found = find_string(tech_choice, self.db_price.index, self._cutoff)

        if size_unit < self.db_price.loc[tech_found, "lim_min"] or size_unit > self.db_price.loc[tech_found, "lim_max"]:
            raise Warning("the size given is out of the chosen range")

        # compute the polynomial function of order func_type which represent the cost
        func_type = self.db_price.loc[tech_found, "order_formula"]
        ppar = self._get_poly(func_type, tech_found)

        # compute the cost
        return np.polyval(ppar, size_unit)

    def price_by_unit(self, tech_choice):
        """
        This function return the price by unit of the technology
        :param tech_choice: string - the technology chosen
        """
        # get the chosen technology
        tech_found = find_string(tech_choice, self.db_price.index, self._cutoff)

        # compute the polynomial function which represent the cost
        func_type = self.db_price.loc[tech_found, "order_formula"]
        ppar = self._get_poly(func_type, tech_found)

        # print the cost by unit
        poly_str = "Cost[CHF]="
        for i in range(func_type):
            if str(func_type - i):
                poly_str += str(ppar[i]) + "x +"
            else:
                poly_str += str(ppar[i]) + "x^" + str(func_type - i) + "+"
        poly_str += str(ppar[-1])

        return poly_str

    def get_units(self, choice_col):
        """
        This function get the units for the price of the different heating technology
        :return: string- the unit
        """
        name_found = find_string(choice_col, self.db_price.index, self._cutoff)
        return self.db_price.loc[name_found, "unit"]

    def get_available_technology(self):
        """
        get the names of the available heating technology and fuels
        """
        return list(self.db_price.index)

    def _get_poly(self, func_type, tech_found):
        """
        This function return the terms of the cost function which is a polynomial
        :param func_type: int - the order of the polynomial
        :param tech_found: string - the chosen technology
        :return: a list with the parameter of each term of the polynomial
        """
        try:
            func_type = int(func_type)
        except ValueError:
            raise ValueError("The function {} is not recognized".format(func_type))
        ppar = np.zeros(func_type + 1)
        for i in range(func_type + 1):
            ppar[i] = round(self.db_price.loc[tech_found, "price_chf_" + str(i)], self._precision)
        return ppar.tolist()
