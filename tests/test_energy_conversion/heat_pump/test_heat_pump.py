
from osem.energy_conversion.heat_pump.heat_pump import HeatPump




class TestHeatPump():

    def test_the_estimation_should_be_correct_case1(self):
        args = {"t_hot": [55, 50, 45], "t_cold": [0, 5, 10]}

        expected = {"cop_carnot": [5.97, 7.18, 9.09], "cop_real": [2.57, 3.09, 3.91]}

        actual = HeatPump(args).calculate()

        for c, r, ac, ar in zip(expected["cop_carnot"], expected["cop_real"], actual["cop_carnot"], actual["cop_real"]):

            assert c == ac
            assert r == ar
    def test_the_estimation_should_be_correct_case2(self):
        args = {"t_hot": [55, 50, 45], "t_cold": [0, 5, 10], "reversible": [False]}

        expected = {"cop_carnot": [5.97, 7.18, 9.09], "cop_real": [2.57, 3.09, 3.91]}

        actual = HeatPump(args).calculate()

        for c, r, ac, ar in zip(expected["cop_carnot"], expected["cop_real"], actual["cop_carnot"], actual["cop_real"]):
            assert c == ac
            assert r == ar

    def test_the_estimation_should_be_correct_case3(self):
        args = {"t_hot": [55, 50, 45], "t_cold": [0, 5, 10], "reversible": [False, False, True]}

        expected = {"cop_carnot": [5.97, 7.18, 8.09], "cop_real": [2.57, 3.09, 2.78]}

        actual = HeatPump(args).calculate()

        for c, r, ac, ar in zip(expected["cop_carnot"], expected["cop_real"], actual["cop_carnot"], actual["cop_real"]):

            assert c == ac
            assert r == ar