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
        self.version_default = '2016'
        self.basename_unit = "kbob_unit"
        self.basename_kbob = "kbob_data"
        self.filename_trans_ind = "kbob_translation_indicator.csv"
        self.cutoff = 0.55

        #  kbob creation
        if year_id:
            self.version = year_id
        else:
            self.version = self.version_default
        self.data, self.unit, self.index_translation = self._load_kbob()

    def get_value(self, techno, indicator, language="ENG"):
        """
        This function load one value of the kbob as a function of the user choice

        :param techno: string - the technology chosen
        :param indicator: string - the requested indicator
        :param language: string - the requested language
        :return: float - the value of the indicator
        """
        self._check_language(language)

        tech_found = find_string(techno, self.data[language].values.tolist(), self.cutoff)
        indi_found_lang = find_string(indicator, self.index_translation[language], self.cutoff)

        indi_found = self.index_translation.loc[self.index_translation[language] == indi_found_lang, 'ENG'].values[0]
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
        """
        The function return the available technology
        :param language: string - the requested language
        :return a list of available technology
        """
        self._check_language(language)
        return list(self.data[language].values)

    def get_available_indicators(self, language="ENG"):
        """
        Give access to the names of the available indicators in different language
        :return: a list of available indicators
        """
        self._check_language(language)
        return list(self.index_translation[language])

    @property
    def kbob_version(self):
        """
        Return the version (year) of the kbob used
        """

        return self.version

    def change_to_default_version(self):
        """
        Restore the loaded kbob to the default version
        """
        self.version = self.version_default
        self.data, self.unit, self.index_translation = self._load_kbob()

    def change_version(self, version_new):
        """
        Change the loaded kbob to the version chosen
        """
        self.version = str(version_new)
        self.data, self.unit, self.index_translation = self._load_kbob()

    def _load_kbob(self):
        """
        This function loads the kbob data and the units related to it
        """
        filename_kbob = os.path.join(self.data_folder, self.basename_kbob+self.version+'.csv')
        filename_trans = os.path.join(self.data_folder, self.filename_trans_ind)
        filename_unit = os.path.join(self.data_folder, self.basename_unit+self.version+'.json')

        kbob = pd.read_csv(filename_kbob, index_col=0)
        unit = pd.read_json(filename_unit, lines=True)
        index_translation = pd.read_csv(filename_trans, header=0)

        return kbob, unit, index_translation

    def _check_language(self, language):
        if language not in self.LANG:
            raise ValueError("The requested language {} is not supported.".format(language))
