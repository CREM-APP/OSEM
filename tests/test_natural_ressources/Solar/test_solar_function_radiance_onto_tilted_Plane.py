import unittest

from Ener.NaturalResources.Solar.SolarFunctionRadianceOntoTiltedPlane import SolarFunctionRadianceOntoTiltedPlane


class TestSolarFunctionRadianceOntoTiltedPlane(unittest.TestCase):
    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        # nothing to do, this test is complete
        args = {"GbeamH": 0, "GdiffuseH": 1, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 0, "slope": 0,
                "albedo": 0.1}
        SolarFunctionRadianceOntoTiltedPlane(args)
        pass

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        # complete set of args. Use this and remove an arg for each test case

        args = {"GdiffuseH": 1, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 0, "slope": 0,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

        args = {"GbeamH": 0, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 0, "slope": 0,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

        args = {"GbeamH": 0, "GdiffuseH": 1,  "incidentAngle": 0, "zenithAngle": 0, "slope": 0,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

        args = {"GbeamH": 0, "GdiffuseH": 1, "dayOfYear": 1, "zenithAngle": 0, "slope": 0,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

        args = {"GbeamH": 0, "GdiffuseH": 1, "dayOfYear": 1, "incidentAngle": 0, "slope": 0,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

        args = {"GbeamH": 0, "GdiffuseH": 1, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 0,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):

        args = {"GbeamH": -1, "GdiffuseH": 1, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 0, "slope": 0,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

        args = {"GbeamH": 0, "GdiffuseH": -2, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 0, "slope": 0,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

        args = {"GbeamH": 0, "GdiffuseH": 1, "dayOfYear": 0, "incidentAngle": 0, "zenithAngle": 0, "slope": 0,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

        args = {"GbeamH": 0, "GdiffuseH": 1, "dayOfYear": 1, "incidentAngle": -1, "zenithAngle": 0, "slope": 0,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

        args = {"GbeamH": 0, "GdiffuseH": 1, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 181, "slope": 0,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

        args = {"GbeamH": 0, "GdiffuseH": 1, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 0, "slope": -1,
                "albedo": 0.1}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

        args = {"GbeamH": 0, "GdiffuseH": 1, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 0, "slope": 0,
                "albedo": 0}
        with self.assertRaises(DomainException):
            SolarFunctionRadianceOntoTiltedPlane(args)

    def test_the_estimation_should_be_correct_case1(self):
        # Put some values here
        args = {"GbeamH": 0, "GdiffuseH": 0, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 0, "slope": 0,
                "albedo": 0.1}
        
        # Fill this with the expected outcome
        expected = {
            "GbeamTiltedPlane": 0,
            "GdiffuseTiltedPlane": 0,
            "GtotalTiltedPlane": 0
        }

        actual = SolarFunctionRadianceOntoTiltedPlane(args).calculate()
        self.assertAlmostEqual(expected["GbeamTiltedPlane"], actual["GbeamTiltedPlane"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["GdiffuseTiltedPlane"], actual["GdiffuseTiltedPlane"], places=0, msg=None,
                               delta=None)
        pass

    def test_the_estimation_should_be_correct_case2(self):
        # Put some values here
        args = {"GbeamH": 1200, "GdiffuseH": 0, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 0, "slope": 0,
                "albedo": 0.2}

        # Fill this with the expected outcome
        expected = {
            "GbeamTiltedPlane": 1200,
            "GdiffuseTiltedPlane": 0,
            "GtotalTiltedPlane": 1200
        }

        actual = SolarFunctionRadianceOntoTiltedPlane(args).calculate()
        self.assertAlmostEqual(expected["GbeamTiltedPlane"], actual["GbeamTiltedPlane"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["GdiffuseTiltedPlane"], actual["GdiffuseTiltedPlane"], places=0, msg=None,
                               delta=None)
        pass

    def test_the_estimation_should_be_correct_case3(self):
        # Put some values here
        args = {"GbeamH": 1200, "GdiffuseH": 0, "dayOfYear": 1, "incidentAngle": 0, "zenithAngle": 25, "slope": 30,
                "albedo": 0.2}

        # Fill this with the expected outcome
        expected = {
            "GbeamTiltedPlane": 1324.054,
            "GdiffuseTiltedPlane": 16.077,
            "GtotalTiltedPlane": 1340.131
        }

        actual = SolarFunctionRadianceOntoTiltedPlane(args).calculate()
        self.assertAlmostEqual(expected["GbeamTiltedPlane"], actual["GbeamTiltedPlane"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["GdiffuseTiltedPlane"], actual["GdiffuseTiltedPlane"], places=0, msg=None,
                               delta=None)
        pass

    def test_the_estimation_should_be_correct_case4(self):
        # Put some values here
        args = {"GbeamH": 1200, "GdiffuseH": 0, "dayOfYear": 143, "incidentAngle": 0, "zenithAngle": 25, "slope": 35,
                "albedo": 0.2}

        # Fill this with the expected outcome
        expected = {
            "GbeamTiltedPlane": 1324.054,
            "GdiffuseTiltedPlane": 21.702,
            "GtotalTiltedPlane": 1345.756
        }

        actual = SolarFunctionRadianceOntoTiltedPlane(args).calculate()
        self.assertAlmostEqual(expected["GbeamTiltedPlane"], actual["GbeamTiltedPlane"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["GdiffuseTiltedPlane"], actual["GdiffuseTiltedPlane"], places=0, msg=None,
                               delta=None)
        pass

    def test_the_estimation_should_be_correct_case5(self):
        # Put some values here
        args = {"GbeamH": 1200, "GdiffuseH": 0, "dayOfYear": 143, "incidentAngle": 51, "zenithAngle": 25, "slope": 35,
                "albedo": 0.2}

        # Fill this with the expected outcome
        expected = {
            "GbeamTiltedPlane": 833.254,
            "GdiffuseTiltedPlane": 21.702,
            "GtotalTiltedPlane": 854.956
        }

        actual = SolarFunctionRadianceOntoTiltedPlane(args).calculate()
        self.assertAlmostEqual(expected["GbeamTiltedPlane"], actual["GbeamTiltedPlane"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["GdiffuseTiltedPlane"], actual["GdiffuseTiltedPlane"], places=0, msg=None,
                               delta=None)
        pass

    def test_the_estimation_should_be_correct_case6(self):
        # Put some values here
        args = {"GbeamH": 1200, "GdiffuseH": 370, "dayOfYear": 143, "incidentAngle": 51, "zenithAngle": 25, "slope": 35,
                "albedo": 0.2}

        # Fill this with the expected outcome
        expected = {
            "GbeamTiltedPlane": 833.254,
            "GdiffuseTiltedPlane": 285.783,
            "GtotalTiltedPlane": 1119.037
        }

        actual = SolarFunctionRadianceOntoTiltedPlane(args).calculate()
        self.assertAlmostEqual(expected["GbeamTiltedPlane"], actual["GbeamTiltedPlane"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["GdiffuseTiltedPlane"], actual["GdiffuseTiltedPlane"], places=0, msg=None,
                               delta=None)
        pass

    def test_the_estimation_should_be_correct_case7(self):
        # Put some values here
        args = {"GbeamH": 1200, "GdiffuseH": 370, "dayOfYear": 143, "incidentAngle": 91, "zenithAngle": 25, "slope": 35,
                "albedo": 0.2}

        # Fill this with the expected outcome
        expected = {
            "GbeamTiltedPlane": 0,
            "GdiffuseTiltedPlane": 30.381,
            "GtotalTiltedPlane": 30.381
        }

        actual = SolarFunctionRadianceOntoTiltedPlane(args).calculate()
        self.assertAlmostEqual(expected["GbeamTiltedPlane"], actual["GbeamTiltedPlane"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["GdiffuseTiltedPlane"], actual["GdiffuseTiltedPlane"], places=0, msg=None,
                               delta=None)
        pass

    def test_the_estimation_should_be_correct_case8(self):
        # Put some values here
        args = {"GbeamH": 1200, "GdiffuseH": 370, "dayOfYear": 143, "incidentAngle": 51, "zenithAngle": 100, "slope": 35,
                "albedo": 0.2}

        # Fill this with the expected outcome
        expected = {
            "GbeamTiltedPlane": 0,
            "GdiffuseTiltedPlane": 2111.052,
            "GtotalTiltedPlane": 2111.052
        }

        actual = SolarFunctionRadianceOntoTiltedPlane(args).calculate()
        self.assertAlmostEqual(expected["GbeamTiltedPlane"], actual["GbeamTiltedPlane"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["GdiffuseTiltedPlane"], actual["GdiffuseTiltedPlane"], places=0, msg=None,
                               delta=None)
        pass