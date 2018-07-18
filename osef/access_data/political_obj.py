import os
import pandas as pd
from osef.access_data.helper_func import find_string


class PoliticalObj:
    """
    This class load the political objectives
    """

    def __init__(self):

        # parameter
        self.cutoff = 0.3
        self.basename = "data/political_obj.csv"
        path_osef = os.path.dirname(os.path.dirname(os.getcwd()))

        # load data
        self.db_obj = pd.read_csv(os.path.join(path_osef, self.basename), sep=';')
        self.db_obj.set_index("political_framework", inplace=True)

    def get_obj(self, politic_type, obj_type, return_year=True):
        """
        This function return the political objective
        :param obj_type: string - the type of objective (C02 emisson, primary energy, etc.)
        :param politic_type: string - the name of the political frame work
        :param return_year: bool- if True return the reference and ojective year
        """

        # match the strings proposed by the user
        obj_found = find_string(obj_type, self.db_obj.columns[:-4], self.cutoff)
        politic_found = find_string(politic_type, self.db_obj.index, self.cutoff)
        if not politic_found or not obj_found:
            return None, None, None

        # get the objective
        obj_value = self.db_obj.loc[politic_found, obj_found]

        # year
        if return_year:
            year_ref = self.db_obj.loc[politic_found, "reference_year"]
            year_obj = self.db_obj.loc[politic_found, "objective_year"]
            return obj_value, year_ref, year_obj
        else:
            return obj_value

    def print_politic_framework(self):
        """
        This function print the available political framework (what a suprise!)
        """
        print(self.db_obj.index.values)

    def print_obj_type(self):
        """
        This function types the type of objective available
        """
        print(self.db_obj.columns[:-4].values)

