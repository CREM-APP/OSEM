import unittest

from osem.energy_conversion.solar_thermal.solar_thermal_production_from_radiation import \
    SolarThermalProductionFromRadiation


class TestSolarThermal(unittest.TestCase):
    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        # nothing to do, this test is complete
        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "albedo": 0.1, "surface": 0, "Ta": 0, "Tin": 1, "Tout": 2, "F": 0, "c1": 0, "c2": 0}
        SolarThermalProductionFromRadiation(args)
        pass

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        # complete set of args. Use this and remove an arg for each test case

        args = {"dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "albedo": 0.1, "surface": 0, "Ta": 0, "Tin": 1, "Tout": 2, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermalProductionFromRadiation(args)

        args = {"latitude": 0, "solarTime": 0, "slope": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "albedo": 0.1, "surface": 0, "Ta": 0, "Tin": 1, "Tout": 2, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermalProductionFromRadiation(args)

        args = {"latitude": 0, "dayOfYear": 1, "slope": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "albedo": 0.1, "surface": 0, "Ta": 0, "Tin": 1, "Tout": 2, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermalProductionFromRadiation(args)

        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "albedo": 0.1, "surface": 0, "Ta": 0, "Tin": 1, "Tout": 2, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermalProductionFromRadiation(args)

        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "GbeamH": 0,
                "GdiffuseH": 0, "albedo": 0.1, "surface": 0, "Ta": 0, "Tin": 1, "Tout": 2, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermalProductionFromRadiation(args)

        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0,
                "GdiffuseH": 0, "albedo": 0.1, "surface": 0, "Ta": 0, "Tin": 1, "Tout": 2, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermalProductionFromRadiation(args)

        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0, "GbeamH": 0,
                "albedo": 0.1, "surface": 0, "Ta": 0, "Tin": 1, "Tout": 2, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermalProductionFromRadiation(args)

        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "albedo": 0.1, "Ta": 0, "Tin": 1, "Tout": 2, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermalProductionFromRadiation(args)

        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "albedo": 0.1, "surface": 0, "Tin": 1, "Tout": 2, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermalProductionFromRadiation(args)

        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "albedo": 0.1, "surface": 0, "Ta": 0, "Tout": 2, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermalProductionFromRadiation(args)

        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "albedo": 0.1, "surface": 0, "Ta": 0, "Tin": 1, "F": 0, "c1": 0, "c2": 0}
        with self.assertRaises(DomainException):
            SolarThermalProductionFromRadiation(args)

    # integration test
    def test_the_estimation_should_be_correct_case(self):
        # Put some values here
        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "surface": 0, "Ta": 0, "Tin": 1, "Tout": 2}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 0,
            "IAMbeam": 0,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermalProductionFromRadiation(args).calculate()

        self.assertAlmostEqual(expected["usefulOutputPower"], actual["usefulOutputPower"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMbeam"], actual["IAMbeam"], places=2, msg=None,
                               delta=None)
        self.assertAlmostEqual(expected["IAMdiffuse"], actual["IAMdiffuse"], places=2, msg=None,
                               delta=None)
