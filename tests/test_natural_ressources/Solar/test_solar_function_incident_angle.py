import unittest

from Ener.NaturalResources.Solar.SolarFunctionIncidentAngle import SolarFunctionIncidentAngle


class TestSolarFunction(unittest.TestCase):
    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        # nothing to do, this test is complete
        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0}
        SolarFunctionIncidentAngle(args)
        pass

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        # complete set of args. Use this and remove an arg for each test case

        args = {"dayOfYear": 1, "solarTime": 1, "slope": 1, "orientation": 1}
        with self.assertRaises(DomainException):
            SolarFunctionIncidentAngle(args)

        args = {"latitude": 1, "solarTime": 1, "slope": 1, "orientation": 1}
        with self.assertRaises(DomainException):
            SolarFunctionIncidentAngle(args)

        args = {"latitude": 1, "dayOfYear": 1, "slope": 1, "orientation": 1}
        with self.assertRaises(DomainException):
            SolarFunctionIncidentAngle(args)

        args = {"latitude": 1, "dayOfYear": 1, "solarTime": 1, "orientation": 1}
        with self.assertRaises(DomainException):
            SolarFunctionIncidentAngle(args)

        args = {"latitude": 1, "dayOfYear": 1, "solarTime": 1, "slope": 1}
        with self.assertRaises(DomainException):
            SolarFunctionIncidentAngle(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):
        args = {"latitude": -91, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0}
        with self.assertRaises(DomainException):
            SolarFunctionIncidentAngle(args)

        args = {"latitude": 1, "dayOfYear": 0, "solarTime": 0, "slope": 0, "orientation": 0}
        with self.assertRaises(DomainException):
            SolarFunctionIncidentAngle(args)

        args = {"latitude": 1, "dayOfYear": 1, "solarTime": 24, "slope": 0, "orientation": 0}
        with self.assertRaises(DomainException):
            SolarFunctionIncidentAngle(args)

        args = {"latitude": 1, "dayOfYear": 1, "solarTime": 1, "slope": -2, "orientation": 0}
        with self.assertRaises(DomainException):
            SolarFunctionIncidentAngle(args)

        args = {"latitude": 1, "dayOfYear": 1, "solarTime": 1, "slope": 0, "orientation": -181}
        with self.assertRaises(DomainException):
            SolarFunctionIncidentAngle(args)


    def test_the_estimation_should_be_correct_case1(self):
        # Put some values here
        args = {"latitude": 43, "dayOfYear": 44, "solarTime": 9.5, "slope": 45, "orientation": 15}

        # Fill this with the expected outcome
        expected = {
            "zenithAngle": 66.5,
            "solarAzimuthAngle": -40,
            "incidentAngle": 49,
            "tranIncidentAngle": -49.00,
            "longIncidentAngle": -7.27
        }

        actual = SolarFunctionIncidentAngle(args).calculate()

        self.assertAlmostEqual(expected["zenithAngle"], actual["zenithAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["solarAzimuthAngle"], actual["solarAzimuthAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["incidentAngle"], actual["incidentAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["tranIncidentAngle"], actual["tranIncidentAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["longIncidentAngle"], actual["longIncidentAngle"], places=0, msg=None,
                               delta=None)

        pass

    def test_the_estimation_should_be_correct_case2(self):
        # Put some values here
        args = {"latitude": 43, "dayOfYear": 182, "solarTime": 18.5, "slope": 45, "orientation": 15}

        # Fill this with the expected outcome
        expected = {
            "zenithAngle": 79.6,
            "solarAzimuthAngle": 112.0,
            "incidentAngle": 87.59,
            "tranIncidentAngle": 87.35,
            "longIncidentAngle": 78.86
        }

        actual = SolarFunctionIncidentAngle(args).calculate()

        self.assertAlmostEqual(expected["zenithAngle"], actual["zenithAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["solarAzimuthAngle"], actual["solarAzimuthAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["incidentAngle"], actual["incidentAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["tranIncidentAngle"], actual["tranIncidentAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["longIncidentAngle"], actual["longIncidentAngle"], places=0, msg=None,
                               delta=None)

        pass

    def test_the_estimation_should_be_correct_case3(self):
        # Put some values here
        args = {"latitude": 20, "dayOfYear": 243, "solarTime": 14.5, "slope": 23, "orientation": 35}

        # Fill this with the expected outcome
        expected = {
            "zenithAngle": 37.855,
            "solarAzimuthAngle": 78.516,
            "incidentAngle": 25.752,
            "tranIncidentAngle": 25.133,
            "longIncidentAngle": -6.407
        }

        actual = SolarFunctionIncidentAngle(args).calculate()

        self.assertAlmostEqual(expected["zenithAngle"], actual["zenithAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["solarAzimuthAngle"], actual["solarAzimuthAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["incidentAngle"], actual["incidentAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["tranIncidentAngle"], actual["tranIncidentAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["longIncidentAngle"], actual["longIncidentAngle"], places=0, msg=None,
                               delta=None)

        pass

    def test_the_estimation_should_be_correct_case4(self):
        # Put some values here
        args = {"latitude": 20, "dayOfYear": 243, "solarTime": 2.3, "slope": 23, "orientation": 35}

        # Fill this with the expected outcome
        expected = {
            "zenithAngle": 135.393,
            "solarAzimuthAngle": -127.175,
            "incidentAngle": 156.428,
            "tranIncidentAngle": 90,
            "longIncidentAngle": 90
        }

        actual = SolarFunctionIncidentAngle(args).calculate()

        self.assertAlmostEqual(expected["zenithAngle"], actual["zenithAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["solarAzimuthAngle"], actual["solarAzimuthAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["incidentAngle"], actual["incidentAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["tranIncidentAngle"], actual["tranIncidentAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["longIncidentAngle"], actual["longIncidentAngle"], places=0, msg=None,
                               delta=None)

        pass

    def test_the_estimation_should_be_correct_case5(self):
        # Put some values here
        args = {"latitude": 12, "dayOfYear": 49, "solarTime": 22.8, "slope": 12, "orientation": 13.5}

        # Fill this with the expected outcome
        expected = {
            "zenithAngle": 162.393,
            "solarAzimuthAngle": 88.404,
            "incidentAngle": 156.34,
            "tranIncidentAngle": 90,
            "longIncidentAngle": 90
        }

        actual = SolarFunctionIncidentAngle(args).calculate()

        self.assertAlmostEqual(expected["zenithAngle"], actual["zenithAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["solarAzimuthAngle"], actual["solarAzimuthAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["incidentAngle"], actual["incidentAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["tranIncidentAngle"], actual["tranIncidentAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["longIncidentAngle"], actual["longIncidentAngle"], places=0, msg=None,
                               delta=None)

        pass

    def test_the_estimation_should_be_correct_case6(self):
        # Put some values here
        args = {"latitude": 43, "dayOfYear": 1, "solarTime": 12, "slope": 0, "orientation": 0}

        # Fill this with the expected outcome
        expected = {
            "zenithAngle": 66.06,
            "solarAzimuthAngle": 0,
            "incidentAngle": 66.06,
            "tranIncidentAngle": 0,
            "longIncidentAngle": -66.06
        }

        actual = SolarFunctionIncidentAngle(args).calculate()

        self.assertAlmostEqual(expected["zenithAngle"], actual["zenithAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["solarAzimuthAngle"], actual["solarAzimuthAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["incidentAngle"], actual["incidentAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["tranIncidentAngle"], actual["tranIncidentAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["longIncidentAngle"], actual["longIncidentAngle"], places=0, msg=None,
                               delta=None)

        pass

    def test_the_estimation_should_be_correct_case7(self):
        # Put some values here
        args = {"latitude": 43, "dayOfYear": 28, "solarTime": 12, "slope": 0, "orientation": 0}

        # Fill this with the expected outcome
        expected = {
            "zenithAngle": 61.42,
            "solarAzimuthAngle": 0,
            "incidentAngle": 61.42,
            "tranIncidentAngle": 0,
            "longIncidentAngle": -61.42
        }

        actual = SolarFunctionIncidentAngle(args).calculate()

        self.assertAlmostEqual(expected["zenithAngle"], actual["zenithAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["solarAzimuthAngle"], actual["solarAzimuthAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["incidentAngle"], actual["incidentAngle"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["tranIncidentAngle"], actual["tranIncidentAngle"], places=0, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["longIncidentAngle"], actual["longIncidentAngle"], places=0, msg=None,
                               delta=None)

        pass