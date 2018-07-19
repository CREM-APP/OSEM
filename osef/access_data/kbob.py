import pandas as pd
import os
from osef.access_data.helper_func import find_string


class Kbob:
    """
    This class loads and manipulate the kbob data
    """

    def __init__(self, year_id=None):

        # default parameter
        self.data_folder = "data"
        self.version_default = str(2016)
        self.basename_unit = "kbob_unit"
        self.basename_kbob = "kbob_data"
        self.cutoff = 0.3

        #  kbob creation
        if year_id:
            self.version = year_id
        else:
            self.version = self.version_default
        self.data, self.unit = self._load_kbob()

    # TODO: change variable name: choice_type is ambiguous
    def get_value(self, choice_tech, choice_type):
        """
        This function load one value of the kbob as a function of the user choice
        :param choice_tech: string - the technology chosen
        :param choice_type: string - the data type
        :return:
        """
        tech_found = find_string(choice_tech, self.data.index, self.cutoff)
        type_found = find_string(choice_type, self.data.columns, self.cutoff)
        # TODO: create else adding warning to logs
        if tech_found and type_found:
            val_kbob = self.data.loc[tech_found, type_found]
            return val_kbob

    # TODO: switch to one method with language as option (+ german ?)
    # TODO: change variable name: choice_type is ambiguous
    def get_value_french(self, choice_tech, choice_type):
        """
        This function load one value of the kbob as a function of the user choice with french technology.
        :param choice_tech: string - the technology chosen in French
        :param choice_type: string - the data type
        :return:
        """
        tech_found = find_string(choice_tech, self.data["French_Name"], self.cutoff)
        type_found = find_string(choice_type, self.data.columns, self.cutoff)
        # TODO: create else adding warning to logs
        if tech_found and type_found:
            val_kbob = self.data.loc[self.data["French_Name"] == tech_found, type_found][0]
            return val_kbob

    def get_units(self, choice_col):
        """
        This function return the units of the different data type
        :return: the unit as string
        """
        name_found = find_string(choice_col, self.data.columns, self.cutoff)
        # TODO: create else adding warning to logs
        if name_found:
            # print("Unit for " + name_found + " is " + self.unit[name_found].values[0] + '.')
            return self.unit[name_found].values[0]

    # TODO: delete redundant method
    def print_units(self, choice_col):
        """
        This function return the units of the different data type
        """
        name_found = find_string(choice_col, self.data.columns, self.cutoff)
        # TODO: create else adding warning to logs
        if name_found:
            print("Unit for " + name_found + " is " + self.unit[name_found].values[0] + '.')

    # TODO: switch to property
    # TODO: remove print
    # TODO: add tests
    def print_available_technology(self):
        """
        print the names of the available heating technology and fuels
        """
        with pd.option_context('display.max_rows', None):
            print('The available technology are:')
            print(list(self.data.index))

    # TODO: switch to property
    # TODO: remove print
    # TODO: add tests
    def print_available_datatype(self):
        """
        print the name of the available datatype (primary energy, Co2, etc.)
        """
        with pd.option_context('display.max_rows', None):
            print('The available data type are :')
            print(list(self.data.columns)[:-1])

    # TODO: switch to property
    # TODO: remove print
    # TODO: add tests
    def print_version(self):
        """
        Return the version (year) of the kbob used
        """
        print("The current kbob version is " + self.version)

    # TODO: add tests
    def change_to_default_version(self):
        """
        change the loaded kbob to the default version
        """
        self.version = self.version_default
        self.data, self.unit = self._load_kbob()

    # TODO: add tests
    def change_version(self, version_new):
        """
        change the loaded kbob to the version chosen
        """
        self.version = version_new
        self.data, self.unit = self._load_kbob()

    # TODO: add tests
    def _load_kbob(self):
        """
        This function loads the kbob data and the units related to it
        """
        filename_kbob = os.path.join(self.data_folder, self.basename_kbob + self.version + ".csv")
        filename_unit = os.path.join(self.data_folder, self.basename_unit + self.version + ".json")

        kbob = pd.read_csv(filename_kbob)
        kbob.set_index("English_Name", inplace=True)
        kbob["EP_Percent_Renew"] = 100 * (kbob["EP_Renew"] / kbob["EP_Global"])
        unit = pd.read_json(filename_unit, lines=True)

        return kbob, unit

