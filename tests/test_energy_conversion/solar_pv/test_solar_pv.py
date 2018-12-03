import unittest

from osem.energy_conversion.solar_pv.solar_pv import SolarPV


class TestSolarPV(unittest.TestCase):
    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        # nothing to do, this test is complete
        args = {"Pmax": 0, "GtotalTiltedPlane": 0, "Gstc": 1, "TempCoef": 0, "Ta": 0, "NOCT": 0, "Tstc": 0}
        SolarPV(args)
        pass

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        # complete set of args. Use this and remove an arg for each test case

        args = {"GtotalTiltedPlane": 0, "Gstc": 1, "TempCoef": 0, "Ta": 0, "NOCT": 0, "Tstc": 0}
        with self.assertRaises(DomainException):
            SolarPV(args)

        args = {"Pmax": 0, "Gstc": 1, "TempCoef": 0, "Ta": 0, "NOCT": 0, "Tstc": 0}
        with self.assertRaises(DomainException):
            SolarPV(args)

        args = {"Pmax": 0, "GtotalTiltedPlane": 0, "Gstc": 1, "TempCoef": 0, "NOCT": 0, "Tstc": 0}
        with self.assertRaises(DomainException):
            SolarPV(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):

        args = {"Pmax": -1, "GtotalTiltedPlane": 0, "Gstc": 1, "TempCoef": 0, "Ta": 0, "NOCT": 0, "Tstc": 0}
        with self.assertRaises(DomainException):
            SolarPV(args)

        args = {"Pmax": 0, "GtotalTiltedPlane": -2, "Gstc": 1, "TempCoef": 0, "Ta": 0, "NOCT": 0, "Tstc": 0}
        with self.assertRaises(DomainException):
            SolarPV(args)

        args = {"Pmax": 0, "GtotalTiltedPlane": 0, "Gstc": 0, "TempCoef": 0, "Ta": 0, "NOCT": 0, "Tstc": 0}
        with self.assertRaises(DomainException):
            SolarPV(args)

        args = {"Pmax": 0, "GtotalTiltedPlane": 0, "Gstc": 1, "TempCoef": -1, "Ta": 0, "NOCT": 0, "Tstc": 0}
        with self.assertRaises(DomainException):
            SolarPV(args)

        args = {"Pmax": 0, "GtotalTiltedPlane": 0, "Gstc": 1, "TempCoef": 0, "Ta": -51, "NOCT": 0, "Tstc": 0}
        with self.assertRaises(DomainException):
            SolarPV(args)

        args = {"Pmax": 0, "GtotalTiltedPlane": 0, "Gstc": 1, "TempCoef": 0, "Ta": 0, "NOCT": -3, "Tstc": 0}
        with self.assertRaises(DomainException):
            SolarPV(args)

        args = {"Pmax": 0, "GtotalTiltedPlane": 0, "Gstc": 1, "TempCoef": 0, "Ta": 0, "NOCT": 0, "Tstc": -4}
        with self.assertRaises(DomainException):
            SolarPV(args)

    def test_the_estimation_should_be_correct_case1(self):
        # Put some values here
        args = {"Pmax": 0, "GtotalTiltedPlane": 0, "Gstc": 1, "TempCoef": 0, "Ta": 0, "NOCT": 0, "Tstc": 0}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 0
        }

        actual = SolarPV(args).calculate()

        self.assertAlmostEqual(expected["ElectricOutputPower"], actual["ElectricOutputPower"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case2(self):
        # Put some values here
        args = {"Pmax": 0, "GtotalTiltedPlane": 200, "Gstc": 950, "TempCoef": 0.4, "Ta": 12, "NOCT": 40, "Tstc": 21}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 0
        }

        actual = SolarPV(args).calculate()

        self.assertAlmostEqual(expected["ElectricOutputPower"], actual["ElectricOutputPower"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case3(self):
        # Put some values here
        args = {"Pmax": 300, "GtotalTiltedPlane": 0, "Gstc": 950, "TempCoef": 0.4, "Ta": 12, "NOCT": 40, "Tstc": 21}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 0
        }

        actual = SolarPV(args).calculate()

        self.assertAlmostEqual(expected["ElectricOutputPower"], actual["ElectricOutputPower"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case4(self):
        # Put some values here
        args = {"Pmax": 15, "GtotalTiltedPlane": 14, "Gstc": 12, "TempCoef": 100, "Ta": 13, "NOCT": 20, "Tstc": 12}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 0
        }

        actual = SolarPV(args).calculate()

        self.assertAlmostEqual(expected["ElectricOutputPower"], actual["ElectricOutputPower"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case5(self):
        # Put some values here
        args = {"Pmax": 300, "GtotalTiltedPlane": 200, "Gstc": 950, "TempCoef": 0.4, "Ta": 12, "NOCT": 40, "Tstc": 21}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 64.168
        }

        actual = SolarPV(args).calculate()

        self.assertAlmostEqual(expected["ElectricOutputPower"], actual["ElectricOutputPower"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case6(self):
        # Put some values here
        args = {"Pmax": 300, "GtotalTiltedPlane": 200, "Ta": 12}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 62.025
        }

        actual = SolarPV(args).calculate()

        self.assertAlmostEqual(expected["ElectricOutputPower"], actual["ElectricOutputPower"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case7(self):
        # Put some values here
        args = {"Pmax": 270, "GtotalTiltedPlane": 800, "Ta": 21}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 193.32
        }

        actual = SolarPV(args).calculate()

        self.assertAlmostEqual(expected["ElectricOutputPower"], actual["ElectricOutputPower"], places=2, msg=None,
                               delta=None)