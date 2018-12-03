import unittest

from osem.energy_conversion.solar_thermal.solar_thermal import SolarThermal


class TestSolarThermal(unittest.TestCase):
    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        # nothing to do, this test is complete
        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 2,
                 "Tout": 3, "F": 0, "c1": 0, "c2": 0}
        SolarThermal(args)
        pass

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        # complete set of args. Use this and remove an arg for each test case

        args = {"GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 2,
                 "Tout": 3}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 2,
                 "Tout": 3}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "surface": 0, "Ta": 1, "Tin": 2,
                 "Tout": 3}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "Ta": 1, "Tin": 2,
                 "Tout": 3}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Tin": 2,
                 "Tout": 3}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1,
                 "Tout": 3}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 2}
        with self.assertRaises(DomainException):
            SolarThermal(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):

        args = {"GbeamTiltedPlane": -1, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 2,
                 "Tout": 3, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": -2, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 2,
                 "Tout": 3, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 181, "surface": -3, "Ta": 1, "Tin": 2,
                 "Tout": 3, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 2,
                 "Tout": -1, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 5,
                 "Tout": 4, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 2,
                 "Tout": 3, "F": -1, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 2,
                 "Tout": 3, "F": 0, "c1": -2, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermal(args)

        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 2,
                 "Tout": 3, "F": 0, "c1": 0, "c2": -3}
        with self.assertRaises(DomainException):
            SolarThermal(args)

    def test_the_estimation_should_be_correct_case1(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 0, "Ta": 1, "Tin": 2,
                 "Tout": 3, "F": 0, "c1": 0, "c2": 0}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 0,
            "IAMbeam": 1,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case2(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 0, "incidentAngle": 82.5, "surface": 3, "Ta": 10, "Tin": 20,
                 "Tout": 40, "F": 0, "c1": 0, "c2": 0}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 0,
            "IAMbeam": 0.32795,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case3(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 1, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 1, "Ta": 10, "Tin": 20,
                 "Tout": 40, "F": 1, "c1": 0, "c2": 0}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 1,
            "IAMbeam": 1,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case4(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 1, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 2.5, "Ta": 10, "Tin": 20,
                 "Tout": 40, "F": 1, "c1": 0, "c2": 0}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 2.5,
            "IAMbeam": 1,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case5(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 1, "GdiffuseTiltedPlane": 0, "incidentAngle": 45, "surface": 1, "Ta": 10, "Tin": 20,
                 "Tout": 40, "F": 1, "c1": 0, "c2": 0}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 0.9645,
            "IAMbeam": 0.9645,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case6(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 1, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 1, "Ta": 10, "Tin": 20,
                 "Tout": 40, "c1": 0, "c2": 0}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 0.7313,
            "IAMbeam": 1,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case7(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 0, "GdiffuseTiltedPlane": 1, "incidentAngle": 0, "surface": 1, "Ta": 10, "Tin": 20,
                 "Tout": 40, "F": 1, "c1": 0, "c2": 0}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 0.8548,
            "IAMbeam": 1,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case8(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 10, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 1, "Ta": 29, "Tin": 20,
                 "Tout": 40, "F": 1, "c1": 3.5, "c2": 0}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 6.5,
            "IAMbeam": 1,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case9(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 10, "GdiffuseTiltedPlane": 0, "incidentAngle": 0, "surface": 1, "Ta": 28, "Tin": 20,
                 "Tout": 40, "F": 1, "c1": 0, "c2": 2}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 2,
            "IAMbeam": 1,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case10(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 10, "GdiffuseTiltedPlane": 10, "incidentAngle": 0, "surface": 1, "Ta": -5, "Tin": 20,
                 "Tout": 40}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 0,
            "IAMbeam": 1,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case11(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 1000, "GdiffuseTiltedPlane": 0, "incidentAngle": 90, "surface": 3, "Ta": 10,
                "Tin": 20, "Tout": 60, "F": 1, "c1": 0, "c2": 0}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 0,
            "IAMbeam": 0,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)
    def test_the_estimation_should_be_correct_case12(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 1000, "GdiffuseTiltedPlane": 0, "incidentAngle": 100, "surface": 3, "Ta": 10,
                "Tin": 20, "Tout": 60, "F": 1, "c1": 0, "c2": 0}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 0,
            "IAMbeam": 0,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case13(self):
        # Put some values here
        args = {"GbeamTiltedPlane": 1000, "GdiffuseTiltedPlane": 100, "incidentAngle": 50, "surface": 1, "Ta": 10,
                "Tin": 20, "Tout": 60}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 631.55,
            "IAMbeam": 0.9409,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermal(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)