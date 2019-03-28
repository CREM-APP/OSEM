import unittest

from Ener.Storage.HotWaterTank.HotWaterTank import HotWaterTank

from Ener.common import DomainException


class TestHotWaterTank(unittest.TestCase):
    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65}
        HotWaterTank(args)

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        args = {"diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65}

        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "q_aux": [0, 150],
                "t_init": 65}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150]}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):
        args = {"height": -1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": -0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "u": -0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [-0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, -150],
                "t_init": 65}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65,
                "rho": -1}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65,
                "cp": -4184}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65,
                "t_step": 0}
        with self.assertRaises(DomainException):
            HotWaterTank(args)

        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65,
                "nbr_of_values_for_step": 0}

        with self.assertRaises(DomainException):
            HotWaterTank(args)

    def test_the_estimation_should_be_correct_case1(self):
        args = {"height": 1,
                "diameter": 0.5,
                "u": 0.05,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [22, 25],
                "q_aux": [0, 150],
                "t_init": 65}

        expected = {'t': [65.0, 48.94, 52.93]}

        actual = HotWaterTank(args).calculate()

        for t_exp, t_act in zip(expected["t"], actual["t"]):
            self.assertAlmostEqual(t_exp, t_act, places=2, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case2(self):
        args = {"height": 1,
                "diameter": 0.5,
                "u": 10,
                "t_cold": [12, 10.5],
                "flow_cons": [0.0001, 0.0001],
                "t_ext": [72, 75],
                "t_init": 65}

        expected = {'t': [65.0, 70.75, 73.65]}

        actual = HotWaterTank(args).calculate()

        for t_exp, t_act in zip(expected["t"], actual["t"]):
            self.assertAlmostEqual(t_exp, t_act, places=2, msg=None, delta=None)
