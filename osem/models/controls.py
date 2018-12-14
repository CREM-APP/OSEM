from osem.models.base import Model


class Hysteresis(Model):
    """
    Model class of a hysteresis controller

    >>> ctrl = Hysteresis()
    >>> ctrl.step(60)

    """
    #TODO DevMaster: What is the purpose of this class missing documentation

    def __init__(self, x_max=1.0, x_min=0.0, y_init=0, start="1/1/2000"):
        """
        This method instantiate the model for the hysteresis controller.

        :param x_max: float - maximal value accepted for sensor value
        :param x_min: float - minimal value accepted for sensor value
        :param y_init: int - initial value for the controller output, must be 0 or 1
        :param start: pandas.Timestamp - start time for simulation results
        """
        super().__init__(start)
        self.x_max = x_max
        self.x_min = x_min

        self.x = 0.0
        self.y = y_init

    def step(self, step, unit="seconds"):
        """
        This method makes the model go one step in time.

        :param step: float - time step to simulate
        :param unit: string - unit of the time step
        """
        super().step(step, unit)
        if self.y and self.x >= self.x_max:
            self.y = 0
        if not self.y and self.x <= self.x_min:
            self.y = 1
