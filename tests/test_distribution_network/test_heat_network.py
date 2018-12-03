import unittest

from osem.distribution_network.heat_network import HeatNetwork

from osem.general.enerapi.common import DomainException


class TestHeatNetwork(unittest.TestCase):
    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        args = {"len_tot": 1000, "t_cons_max": 90, "p_cons_tot": 500, "t_return_fixed": 60}
        HeatNetwork(args)

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        args = {"t_cons_max": 90, "p_cons_tot": 500, "t_return_fixed": 60}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

        args = {"len_tot": 1000, "p_cons_tot": 500, "t_return_fixed": 60}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

        args = {"len_tot": 1000, "t_cons_max": 90, "t_return_fixed": 60}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

        args = {"len_tot": 1000, "t_cons_max": 90, "p_cons_tot": 500}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):
        args = {"len_tot": -10, "t_cons_max": 90, "p_cons_tot": 500, "t_return_fixed": 60}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

        args = {"len_tot": 1000, "t_cons_max": -10, "p_cons_tot": 500, "t_return_fixed": 60}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

        args = {"len_tot": 1000, "t_cons_max": 90, "p_cons_tot": -10, "t_return_fixed": 60}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

        args = {"len_tot": 1000, "t_cons_max": 90, "p_cons_tot": 500, "t_return_fixed": -10}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

        args = {"len_tot": 1000, "t_cons_max": 90, "p_cons_tot": 500, "t_return_fixed": 60, "th_loss_coef": 0}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

        args = {"len_tot": 1000, "t_cons_max": 90, "p_cons_tot": 500, "t_return_fixed": 60, "rho_fluid": 0}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

        args = {"len_tot": 1000, "t_cons_max": 90, "p_cons_tot": 500, "t_return_fixed": 60, "cp_mass_fluid": 0}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

        args = {"len_tot": 1000, "t_cons_max": 90, "p_cons_tot": 500, "t_return_fixed": 60, "v_max": 0}
        with self.assertRaises(DomainException):
            HeatNetwork(args)

    def test_the_estimation_should_be_correct_case1(self):
        args = {"len_tot": 10000, "t_cons_max": 90, "p_cons_tot": 5000, "t_return_fixed": 60}

        expected = {"ratio_th_loss": 0.05, "p_supply": 5265, "t_reject": 60.6, "fluid_flow": 146}

        actual = HeatNetwork(args).calculate()

        self.assertAlmostEqual(expected["ratio_th_loss"], actual["ratio_th_loss"], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_supply"], actual["p_supply"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_reject"], actual["t_reject"], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["fluid_flow"], actual["fluid_flow"], places=0, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case2(self):
        args = {"len_tot": 10000, "t_cons_max": 40, "p_cons_tot": 10000, "t_return_fixed": 20, "ground_temp": 8}

        expected = {"ratio_th_loss": 0.009, "p_supply": 10090}

        actual = HeatNetwork(args).calculate()

        self.assertAlmostEqual(expected["ratio_th_loss"], actual["ratio_th_loss"], places=3, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_supply"], actual["p_supply"], places=0, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case3(self):
        args = {"len_tot": 10000, "t_cons_max": 40, "p_cons_tot": 10000, "t_return_fixed": 20, "th_loss_coef": 0.5}

        expected = {"ratio_th_loss": 0.02, "p_supply": 10201}

        actual = HeatNetwork(args).calculate()

        self.assertAlmostEqual(expected["ratio_th_loss"], actual["ratio_th_loss"], places=3, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_supply"], actual["p_supply"], places=0, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case4(self):
        args = {"len_tot": 10000, "t_cons_max": 40, "p_cons_tot": 10000, "t_return_fixed": 20, "rho_fluid": 2000}

        expected = {"ratio_th_loss": 0.008, "p_supply": 10081}

        actual = HeatNetwork(args).calculate()

        self.assertAlmostEqual(expected["ratio_th_loss"], actual["ratio_th_loss"], places=3, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_supply"], actual["p_supply"], places=0, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case5(self):
        args = {"len_tot": 10000, "t_cons_max": 90, "p_cons_tot": 10000, "t_return_fixed": 60, "cp_mass_fluid": 4000}

        expected = {"ratio_th_loss": 0.026, "p_supply": 10265, "fluid_flow": 303}

        actual = HeatNetwork(args).calculate()

        self.assertAlmostEqual(expected["ratio_th_loss"], actual["ratio_th_loss"], places=3, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_supply"], actual["p_supply"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["fluid_flow"], actual["fluid_flow"], places=0, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case6(self):
        args = {"len_tot": 10000, "t_cons_max": 90, "p_cons_tot": 10000, "t_return_fixed": 20, "v_max": 1.8}

        expected = {"ratio_th_loss": 0.018, "p_supply": 10184, "fluid_flow": 123, "inner_diameter_min": 0.155}

        actual = HeatNetwork(args).calculate()

        self.assertAlmostEqual(expected["ratio_th_loss"], actual["ratio_th_loss"], places=3, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_supply"], actual["p_supply"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["fluid_flow"], actual["fluid_flow"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["inner_diameter_min"], actual["inner_diameter_min"], places=2, msg=None,
                               delta=None)
