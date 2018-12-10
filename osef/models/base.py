import pandas as pd
import numpy as np

#TODO DevMaster: base is not so clear need a definition
#TODO DevMaster: for calculation helper keep it in an helper directory
def tau_model(y, t, io, tau, p_nom):
    """
    Define ODE for a simplified dynamic model using time constant.
    It computes the derivatives describing the model.
    """
    dydt = (p_nom * io - y) / tau
    return dydt


def normalize(v, y_min=0.0, y_max=1.0, x_min=0, x_max=1):
    """
    Normalize values and apply max and min limits to input values

    :param v: numpy.array - values to normalize
    :param y_min: float - minimal value to normalize with
    :param y_max: float - maximal value to normalize with
    :param x_min: float - lower bound for input values
    :param x_max: float - upper bound for input values
    :return numpy.array - normalized values
    """
    v = np.array([min(vx, x_max) for vx in v])
    v = np.array([max(vx, x_min) for vx in v])
    return (y_max - y_min) / (x_max - x_min) * (v - x_min)


class Model:
    """
    This class is used a a common bloc to build other models upon.
    """
    #TODO DevMaster: What is the purpose of this class missing documentation
    UNIT = {"seconds": 1, "minutes": 60, "hours": 3600}

    def __init__(self, start):
        """
        This method instantiate the model.

        :param start: pandas.Timestamp - start time for simulation results
        """
        self.time = pd.to_datetime(start)

    def step(self, step, unit):
        """
        This method makes the model go one step in time.

        :param step: float - time step to simulate
        :param unit: string - unit of the time step
        """
        self.time += pd.DateOffset(**{unit: step})
