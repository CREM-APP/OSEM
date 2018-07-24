import os
import pandas as pd
from osef.access_data.helper_func import find_string


class PoliticalObj:
    """
    This class load the political objectives
    """

    def __init__(self):

        # parameter
        self.data_folder = "data"
        self.cutoff = 0.55
        self.basename = "political_obj.csv"
        self.column_not_print = ['reference_year', 'objective_year' , 'note' , 'reference']

        # load data
        self.db_obj = pd.read_csv(os.path.join(self.data_folder, self.basename), sep=";")
        self.db_obj.set_index("political_framework", inplace=True)
        self.name_objective = [c for c in self.db_obj.columns if c not in self.column_not_print]

    def get_objective(self, politic_type, obj_type, return_year=True):

        """
        This function return the political objective
        :param obj_type: string - the type of objective (C02 emisson, primary energy, etc.)
        :param politic_type: string - the name of the political frame work
        :param return_year: bool- if True return the reference and ojective year
        """

        # match the strings proposed by the user
        objective_found = find_string(obj_type, self.name_objective, self.cutoff)
        politic_found = find_string(politic_type, self.db_obj.index, self.cutoff)

        # get the objective
        objective_value = self.db_obj.loc[politic_found, objective_found]

        # year
        if return_year:
            year_ref = self.db_obj.loc[politic_found, "reference_year"]
            year_obj = self.db_obj.loc[politic_found, "objective_year"]
            objective_dict = {'value': objective_value, 'year_ref':year_ref, 'year_obj': year_obj}
            return objective_dict
        else:
            return objective_value

    def get_politic_framework(self):
        """
        This function get the available political framework
        """
        return list(self.db_obj.index.values)

    def get_all_objectives(self):
        """
        This function get the type of objective available
        """
        return list(self.name_objective)
