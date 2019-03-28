import unittest

from Ener.NaturalResources.GeoThermal.GeoThermal import GeoThermal

from Ener.common import DomainException

__author__ = 'tbernhard'


class TestGeoThermal(unittest.TestCase):
    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        args = {"altitude": 400,  "available_area": 25}
        GeoThermal(args)

    def test_if_a_required_argument_is_missing_an_exception_should_be_raised(self):
        args = {"altitude": 400}
        with self.assertRaises(DomainException):
            GeoThermal(args)

        args = {"available_area": 25}
        with self.assertRaises(DomainException):
            GeoThermal(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):
        args = {"altitude": -400,  "available_area": 25}
        with self.assertRaises(DomainException):
            GeoThermal(args)

        args = {"altitude": 400,  "available_area": -25}
        with self.assertRaises(DomainException):
            GeoThermal(args)

        args = {"altitude": 400,  "available_area": 25, "ground_conductivity": -2}
        with self.assertRaises(DomainException):
            GeoThermal(args)

        args = {"altitude": 400,  "available_area": 25, "maximum_depth": 5000}
        with self.assertRaises(DomainException):
            GeoThermal(args)

    def test_the_estimation_should_be_correct_case1(self):
        args = {"ground_conductivity": 2.0, "altitude": 400, "maximum_depth": 400, "available_area": 625}

        expected = {
            "Geothermal specific power": 40,
            "Geothermal power": 16,
            "Geothermal energy": 36
        }

        actual = GeoThermal(args).calculate()

        self.assertAlmostEqual(expected["Geothermal specific power"], actual["Geothermal specific power"], places=0,
                               msg=None, delta=None)
        self.assertAlmostEqual(expected["Geothermal power"], actual["Geothermal power"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["Geothermal energy"], actual["Geothermal energy"], places=0, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case2(self):
        args = {"ground_conductivity": 1.0, "altitude": 400, "maximum_depth": 100, "available_area": 625.0}

        expected = {
            "Geothermal specific power": 29.8,
            "Geothermal power": 3.0,
            "Geothermal energy": 6.6
        }

        actual = GeoThermal(args).calculate()

        self.assertAlmostEqual(expected["Geothermal specific power"], actual["Geothermal specific power"], places=0,
                               msg=None, delta=None)
        self.assertAlmostEqual(expected["Geothermal power"], actual["Geothermal power"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["Geothermal energy"], actual["Geothermal energy"], places=0, msg=None,
                               delta=None)

    def test_the_estimation_should_be_correct_case3(self):
        args = {"ground_conductivity": 1.0, "altitude": 400, "maximum_depth": 100, "available_area": 625.0}

        expected = {
            "Geothermal specific power": 29.8,
            "Geothermal power": 3.0,
            "Geothermal energy": 6.6
        }

        actual = GeoThermal(args).calculate()

        self.assertAlmostEqual(expected["Geothermal specific power"], actual["Geothermal specific power"], places=0,
                               msg=None, delta=None)
        self.assertAlmostEqual(expected["Geothermal power"], actual["Geothermal power"], places=0, msg=None, delta=None)
        self.assertAlmostEqual(expected["Geothermal energy"], actual["Geothermal energy"], places=0, msg=None,
                               delta=None)
