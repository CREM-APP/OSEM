import osem.general.conf as conf
import json
import os


class SolverOption:
    """
    This class contains the option for the solver of the gas network model
    """

    def __init__(self):
        # data
        self._data_folder = conf.data_folder

        # values and key of the solver option
        self.solver_values = conf.default_solver_option
        self.solver_info = self._load_solver_info()

    def _load_solver_info(self):
        """
        load a json file which details the information related to the solver option
        :return: the info in a string
        """

        with open(os.path.join(self._data_folder, conf.filename_info_solver), 'r') as f:
            solver_explanation = json.load(f)
        return solver_explanation

    def set_solver_option(self, solver_option=None):
        """
        sets the solver option used to solve the equations.

        :param solver_option: the dict given by the user with custom options or none
        """

        if solver_option:
            for k in solver_option.keys():
                self.solver_values[k] = solver_option[k]

    def __repr__(self):
        """
        implementation of the print function
        """

        print('Here are the current solver options: ')
        print(self.solver_values)

        print('\nHere are definition of the current solver options: ')
        print(self.solver_info)

    def __getitem__(self, item):
        return self.solver_values[item]