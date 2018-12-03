import unittest

from osem.energy_conversion.heat_pump.heat_pump import HeatPump

from osem.general.enerapi.common import DomainException


class TestHeatPump(unittest.TestCase):
    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        args = {"t_hot": [55.5, 60], "t_cold": [10, 12]}
        HeatPump(args)

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        args = {"t_cold": [10]}
        with self.assertRaises(DomainException):
            HeatPump(args)

        args = {"t_hot": [55]}
        with self.assertRaises(DomainException):
            HeatPump(args)

    def test_if_a_list_argument_has_an_incorrect_length_an_exception_should_be_raised(self):
        args = {"t_hot": [55], "t_cold": [10, 20]}
        with self.assertRaises(DomainException):
            HeatPump(args)

        args = {"t_hot": [55], "t_cold": []}
        with self.assertRaises(DomainException):
            HeatPump(args)

        args = {"t_hot": [55], "t_cold": [10], "reversible": [False, True]}
        with self.assertRaises(DomainException):
            HeatPump(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):
        args = {"t_hot": [-2], "t_cold": [-10]}
        with self.assertRaises(DomainException):
            HeatPump(args)

        args = {"t_hot": [55], "t_cold": [60]}
        with self.assertRaises(DomainException):
            HeatPump(args)

        args = {"t_hot": [55], "t_cold": [10], "reversible": ["test"]}
        with self.assertRaises(DomainException):
            HeatPump(args)

        args = {"t_hot": [55], "t_cold": [10], "n": 0}
        with self.assertRaises(DomainException):
            HeatPump(args)

        args = {"t_hot": [55], "t_cold": [10], "r": 10}
        with self.assertRaises(DomainException):
            HeatPump(args)

    def test_the_estimation_should_be_correct_case1(self):
        args = {"t_hot": [55, 50, 45], "t_cold": [0, 5, 10]}

        expected = {"cop_carnot": [5.97, 7.18, 9.09], "cop_real": [2.57, 3.09, 3.91]}

        actual = HeatPump(args).calculate()

        for c, r, ac, ar in zip(expected["cop_carnot"], expected["cop_real"], actual["cop_carnot"], actual["cop_real"]):

            self.assertAlmostEqual(c, ac, places=2, msg=None, delta=None)
            self.assertAlmostEqual(r, ar, places=2, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case2(self):
        args = {"t_hot": [55, 50, 45], "t_cold": [0, 5, 10], "reversible": [False]}

        expected = {"cop_carnot": [5.97, 7.18, 9.09], "cop_real": [2.57, 3.09, 3.91]}

        actual = HeatPump(args).calculate()

        for c, r, ac, ar in zip(expected["cop_carnot"], expected["cop_real"], actual["cop_carnot"], actual["cop_real"]):

            self.assertAlmostEqual(c, ac, places=2, msg=None, delta=None)
            self.assertAlmostEqual(r, ar, places=2, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case3(self):
        args = {"t_hot": [55, 50, 45], "t_cold": [0, 5, 10], "reversible": [False, False, True]}

        expected = {"cop_carnot": [5.97, 7.18, 8.09], "cop_real": [2.57, 3.09, 2.78]}

        actual = HeatPump(args).calculate()

        for c, r, ac, ar in zip(expected["cop_carnot"], expected["cop_real"], actual["cop_carnot"], actual["cop_real"]):

            self.assertAlmostEqual(c, ac, places=2, msg=None, delta=None)
            self.assertAlmostEqual(r, ar, places=2, msg=None, delta=None)