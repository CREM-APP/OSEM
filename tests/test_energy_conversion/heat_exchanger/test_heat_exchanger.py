import unittest

from osem.energy_conversion.heat_exchanger.heat_Exchanger import HeatExchanger

from osem.general.enerapi.common import DomainException


class TestHeatExchanger(unittest.TestCase):

    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        args = {"u": 25, "area": 15,
                "flow_hot": [0.0005], "t_in_hot": [100],
                "flow_cold": [0.001], "t_in_cold": [20]}
        HeatExchanger(args)

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        args = {"area": 15,
                "flow_hot": [0.0005], "t_in_hot": [100],
                "flow_cold": [0.001], "t_in_cold": [20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

        args = {"u": 25,
                "flow_hot": [0.0005], "t_in_hot": [100],
                "flow_cold": [0.001], "t_in_cold": [20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

        args = {"u": 25, "area": 15,
                "t_in_hot": [100],
                "flow_cold": [0.001], "t_in_cold": [20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

        args = {"u": 25, "area": 15,
                "flow_hot": [0.0005],
                "flow_cold": [0.001], "t_in_cold": [20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

        args = {"u": 25, "area": 15,
                "flow_hot": [0.0005], "t_in_hot": [100],
                "t_in_cold": [20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

        args = {"u": 25, "area": 15,
                "flow_hot": [0.0005], "t_in_hot": [100],
                "flow_cold": [0.001]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

    def test_if_a_list_argument_has_an_incorrect_length_an_exception_should_be_raised(self):
        args = {"u": 25, "area": 15,
                "flow_hot": [0.0005, 0.0005], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0.001], "t_in_cold": [20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):
        args = {"u": 25, "area": 15,
                "flow_hot": [0.0005, 0.0005], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0.001], "t_in_cold": [20, 150]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

        args = {"u": 25, "area": 15,
                "flow_hot": [0.0005, -0.0005], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0.001], "t_in_cold": [20, 20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

        args = {"u": -25, "area": 15,
                "flow_hot": [0.0005, 0.0005], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0.001], "t_in_cold": [20, 20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

        args = {"u": 25, "area": -15,
                "flow_hot": [0.0005, 0.0005], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0.001], "t_in_cold": [20, 20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

        args = {"u": 25, "area": 15, "rho": -10,
                "flow_hot": [0.0005, 0.0005], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0.001], "t_in_cold": [20, 20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

        args = {"u": 25, "area": 15, "cp": -10,
                "flow_hot": [0.0005, 0.0005], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0.001], "t_in_cold": [20, 20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

        args = {"u": 25, "area": 15, "type": "test",
                "flow_hot": [0.0005, 0.0005], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0.001], "t_in_cold": [20, 20]}
        with self.assertRaises(DomainException):
            HeatExchanger(args)

    def test_the_estimation_should_be_correct_case0(self):
        args = {"u": 25, "area": 15,
                "flow_hot": [0, 0.001], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0], "t_in_cold": [20, 20]}

        expected = {"t_out_hot": [100, 100], "t_out_cold": [20, 20]}

        actual = HeatExchanger(args).calculate()

        for (th_exp, tc_exp, th_act, tc_act) in zip(expected["t_out_hot"], expected["t_out_cold"],
                                                    actual["t_out_hot"], actual["t_out_cold"]):
            self.assertAlmostEqual(th_exp, th_act, places=2, msg=None, delta=None)
            self.assertAlmostEqual(tc_exp, tc_act, places=2, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case1(self):
        args = {"u": 25, "area": 15,
                "flow_hot": [0.0005, 0.001], "t_in_hot": [100, 100],
                "flow_cold": [0.001, 0.0005], "t_in_cold": [20, 20]}

        expected = {"t_out_hot": [87.37, 93.68], "t_out_cold": [26.32, 32.63]}

        actual = HeatExchanger(args).calculate()

        for (th_exp, tc_exp, th_act, tc_act) in zip(expected["t_out_hot"], expected["t_out_cold"],
                                                    actual["t_out_hot"], actual["t_out_cold"]):
            self.assertAlmostEqual(th_exp, th_act, places=2, msg=None, delta=None)
            self.assertAlmostEqual(tc_exp, tc_act, places=2, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case2(self):
        args = {"u": 25, "area": 15,
                "flow_hot": [0.0005, 0.001], "t_in_hot": [100, 100],
                "flow_cold": [0.0005, 0.001], "t_in_cold": [20, 20]}

        expected = {"t_out_hot": [87.83, 93.42], "t_out_cold": [32.17, 26.58]}

        actual = HeatExchanger(args).calculate()

        for (th_exp, tc_exp, th_act, tc_act) in zip(expected["t_out_hot"], expected["t_out_cold"],
                                                    actual["t_out_hot"], actual["t_out_cold"]):
            self.assertAlmostEqual(th_exp, th_act, places=2, msg=None, delta=None)
            self.assertAlmostEqual(tc_exp, tc_act, places=2, msg=None, delta=None)

