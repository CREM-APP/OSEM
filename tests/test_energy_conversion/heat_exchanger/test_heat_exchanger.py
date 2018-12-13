

from osem.energy_conversion.heat_exchanger.heat_Exchanger import HeatExchanger




class TestHeatExchanger():


    def test_the_estimation_should_be_correct_case0(self):
        args = {"u": 25, "area": 15,
                "flow_hot": [0, 0.001], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0], "t_in_cold": [20, 20]}

        expected = {"t_out_hot": [100, 100], "t_out_cold": [20, 20]}

        actual = HeatExchanger(args).calculate()

        for (th_exp, tc_exp, th_act, tc_act) in zip(expected["t_out_hot"], expected["t_out_cold"],
                                                    actual["t_out_hot"], actual["t_out_cold"]):
            assert th_exp == th_act
            assert tc_exp == tc_act


    def test_the_estimation_should_be_correct_case1(self):
        args = {"u": 25, "area": 15,
                "flow_hot": [0.0005, 0.001], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0.0005], "t_in_cold": [20, 20]}

        expected = {"t_out_hot": [87.37, 93.68], "t_out_cold": [26.32, 32.63]}

        actual = HeatExchanger(args).calculate()

        for (th_exp, tc_exp, th_act, tc_act) in zip(expected["t_out_hot"], expected["t_out_cold"],
                                                    actual["t_out_hot"], actual["t_out_cold"]):
            assert th_exp == th_act
            assert tc_exp == tc_act


    def test_the_estimation_should_be_correct_case2(self):
        args = {"u": 25, "area": 15,
                "flow_hot": [0.0005, 0.001], "t_in_hot": [100, 100],
                "flow_cold": [0.0005, 0.001], "t_in_cold": [20, 20]}

        expected = {"t_out_hot": [87.83, 93.42], "t_out_cold": [32.17, 26.58]}

        actual = HeatExchanger(args).calculate()

        for (th_exp, tc_exp, th_act, tc_act) in zip(expected["t_out_hot"], expected["t_out_cold"],
                                                    actual["t_out_hot"], actual["t_out_cold"]):
            assert th_exp == th_act
            assert tc_exp == tc_act

