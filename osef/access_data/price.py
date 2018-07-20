import os
import pandas as pd
from osef.access_data.helper_func import find_string
import numpy as np


class Price:
    """
    This class loads and manipulate the price data
    """

    def __init__(self):

        # parameter
        self.data_folder = "data"
        self.cutoff = 0.3
        self.precision = 5
        self.basename_price = "price_liste.csv"

        # load data
        self.db_price = pd.read_csv(os.path.join(self.data_folder, self.basename_price), sep=";")
        self.db_price.set_index("technology", inplace=True)

    def price_total(self, tech_choice, size_unit):
        """
        This function calculate the price of the technology chosen by the user for the size of unit given
        :param tech_choice: string - the technology chosen
        :param size_unit: float - the number of unit or the power of the installation
        """
        # get the chosen technology
        tech_found = find_string(tech_choice, self.db_price.index, self.cutoff)
        if not tech_found:
            # TODO: add warning to logs
            return
        # TODO: remove print, add warning to logs
        if size_unit < self.db_price.loc[tech_found, "lim_min"] or size_unit > self.db_price.loc[tech_found, "lim_max"]:
            print("Warning: the size given is out of the chosen range")

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
        tech_found = find_string(tech_choice, self.db_price.index, self.cutoff)
        if not tech_found:
            # TODO: add warning to logs
            return

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

    # TODO: change print to return in docstring
    def get_units(self, choice_col):
        """
        This function print the units for the price of the different heating technology
        :return:
        """
        name_found = find_string(choice_col, self.db_price.index, self.cutoff)
        # TODO: create else adding warning to logs
        if name_found:
            return self.db_price.loc[name_found, "unit"]

    # TODO: delete redundant method
    def print_units(self, choice_col):
        """
        This function print the units for the price of the different heating technology
        :return:
        """
        name_found = find_string(choice_col, self.db_price.index, self.cutoff)
        if name_found:
            print("Unit for " + name_found + " is " + self.db_price.loc[name_found, "unit"] + ".")

    # TODO: switch to property
    # TODO: remove print
    # TODO: add tests
    def print_available_technology(self):
        """
        print the names of the available heating technology and fuels with a price
        """
        with pd.option_context("display.max_rows", None):
            print("The available technology are:")
            print(list(self.db_price.index))

    # TODO: add tests
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
            # TODO: remove print, add error to logs
            print("Error: Type of function not recognized")
            return
        ppar = np.zeros(func_type + 1)
        for i in range(func_type + 1):
            ppar[i] = round(self.db_price.loc[tech_found, "price_chf_" + str(i)], self.precision)
        return ppar


price = Price()
