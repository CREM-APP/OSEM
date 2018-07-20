import os
import pandas as pd

from osef.access_data.helper_func import find_string


class Kbob:
    """
    This class loads and manipulate the kbob data
    """

    LANG = ["ENG", "FRA", "GER"]

    def __init__(self, year_id=None):

        # default parameter
        self.data_folder = "data"
        self.version_default = 2016
        self.basename_unit = "kbob_unit"
        self.basename_kbob = "kbob_data"
        self.cutoff = 0.3

        #  kbob creation
        if year_id:
            self.version = year_id
        else:
            self.version = self.version_default
        self.data, self.unit = self._load_kbob()

    def get_value(self, techno, indicator, language="ENG"):
        """
        This function load one value of the kbob as a function of the user choice

        :param techno: string - the technology chosen
        :param indicator: string - the requested indicator
        :param language:
        :return:
        """
        self._check_language(language)

        tech_found = find_string(techno, self.data[language].values.tolist(), self.cutoff)
        indi_found = find_string(indicator, self.available_indicators, self.cutoff)

        if not tech_found:
            raise ValueError("The requested technology {} does not match any entry.".format(techno))

        if not indi_found:
            raise ValueError("The requested indicator {} does not match any entry.".format(indicator))

        print(tech_found)
        print(self.data.loc[self.data[language] == tech_found, indi_found].values[0])
        return self.data.loc[self.data[language] == tech_found, indi_found].values[0]

    def get_units(self, choice_col):
        """
        This function return the units of the different data type
        :return: the unit as string
        """
        name_found = find_string(choice_col, self.data.columns, self.cutoff)
        if not name_found:
            raise ValueError("The requested data {} does not match any entry.".format(choice_col))

        return self.unit[name_found].values[0]

    def get_available_technologies(self, language="ENG"):
        self._check_language(language)
        return list(self.data[language].values)

    @property
    def available_indicators(self):
        """
        Give access to indicator availables names
        :return: a list of available indicators
        """
        return [c for c in self.data.columns if c not in self.LANG]

    @property
    def year_version(self):
        """
        Return the version (year) of the kbob used
        """
        return self.version

    # TODO: add tests
    def restore_to_default_version(self):
        """
        Restore the loaded kbob to the default version
        """
        self.version = self.version_default
        self.data, self.unit = self._load_kbob()

    # TODO: add tests
    def change_version(self, version_new):
        """
        Change the loaded kbob to the version chosen
        """
        self.version = version_new
        self.data, self.unit = self._load_kbob()

    # TODO: add tests
    def _load_kbob(self):
        """
        This function loads the kbob data and the units related to it
        """
        filename_kbob = os.path.join(self.data_folder, "{}{}.csv".format(self.basename_kbob, self.version))
        filename_unit = os.path.join(self.data_folder, "{}{}.json".format(self.basename_unit, self.version))

        kbob = pd.read_csv(filename_kbob, index_col=0)
        kbob["EP_Percent_Renew"] = 100 * (kbob["EP_Renew"] / kbob["EP_Global"])
        unit = pd.read_json(filename_unit, lines=True)

        return kbob, unit

    def _check_language(self, language):
        if language not in self.LANG:
            raise ValueError("The requested language {} is not supported.".format(language))
