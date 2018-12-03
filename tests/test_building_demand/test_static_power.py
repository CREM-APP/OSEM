"""import unittest

from data.InMemoryFileCache import InMemoryFileCache

from osem.general.enerapi.base.base import Base
from Ener.BuildingDemand.StaticPower import StaticHeatingCoolingPower
from Ener.common import DomainException


class MockCache(InMemoryFileCache):
    def __init__(self):
        super(MockCache, self).__init__()
        self.ReadCount = 0

    # override
    def _load_file_from_disk(self, filename):
        sia_ref = '{"data": {\
            "Maison_Ind.": {\
                "SIA_cat": 2,\
                "t_heat_set_point": 20,\
                "t_cool_set_point": 26,\
                "surf_pers": 60,\
                "heat_pers": 70\
        }}}'

        construct_bat = '{"data": {\
            "Maison_Ind.": {\
                "SIA_cat": 2,\
                "Avant 1919": {\
                    "GBAUP": 8011,\
                    "Uroof": 1.6,\
                    "Uwall": 0.94,\
                    "Ufloor": 2.5,\
                    "Uwindow": 3,\
                    "g": 0.8,\
                    "Inert": 1\
        }}}}'

        mock_data = {}

        if filename == 'data_SIA_380-1.json':
            mock_data = sia_ref
        if filename == 'Construct_Bat.json':
            mock_data = construct_bat
        return mock_data


class TestICT(unittest.TestCase):
    @staticmethod
    def setUpClass():
        Base.features = FeatureBroker()
        Base.features.Provide("Cache", MockCache)

    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        StaticHeatingCoolingPower(args)

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        args = {"affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011,"sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2,"s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200,"s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255,"s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):
        args = {"period": "test", "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": "test", "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": -200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": -255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": -45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": -100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": -100, "esa": 45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": -45, "t_ext": [32], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [100], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32], "irr_south": [-700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [32, 30], "irr_south": [700]}
        with self.assertRaises(DomainException):
            StaticHeatingCoolingPower(args)

    def test_the_estimation_should_be_correct_case1(self):
        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [23], "irr_south": [700]}

        expected = {
            "Penvelope_heating": [2354.10],
            "Penvelope_cooling": [-2354.10],
            "Psol": [25200],
            "Pocc": [233.333],
            "Ptot_heating": [0],
            "Ptot_cooling": [23079.23]
        }

        actual = StaticHeatingCoolingPower(args).calculate()

        self.assertAlmostEqual(expected["Penvelope_heating"][0], actual["Penvelope_heating"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Penvelope_cooling"][0], actual["Penvelope_cooling"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Psol"][0], actual["Psol"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Pocc"][0], actual["Pocc"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Ptot_heating"][0], actual["Ptot_heating"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Ptot_cooling"][0], actual["Ptot_cooling"][0], places=2, msg=None, delta=None)

        pass

    def test_the_estimation_should_be_correct_case2(self):
        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [15, 30], "irr_south": [100, 200]}

        expected = {
            "Penvelope_heating": [-3923.5, 7847.0],
            "Penvelope_cooling": [-8631.7, 3138.8],
            "Psol": [3600, 7200.0],
            "Pocc": [233.333, 233.33],
            "Ptot_heating": [90.166, 0],
            "Ptot_cooling": [0, 10572.133]
        }

        actual = StaticHeatingCoolingPower(args).calculate()

        self.assertAlmostEqual(expected["Penvelope_heating"][0], actual["Penvelope_heating"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Penvelope_cooling"][0], actual["Penvelope_cooling"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Psol"][0], actual["Psol"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Pocc"][0], actual["Pocc"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Ptot_heating"][0], actual["Ptot_heating"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Ptot_cooling"][0], actual["Ptot_cooling"][0], places=2, msg=None, delta=None)

        self.assertAlmostEqual(expected["Penvelope_heating"][1], actual["Penvelope_heating"][1], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Penvelope_cooling"][1], actual["Penvelope_cooling"][1], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Psol"][1], actual["Psol"][1], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Pocc"][1], actual["Pocc"][1], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Ptot_heating"][1], actual["Ptot_heating"][1], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["Ptot_cooling"][1], actual["Ptot_cooling"][1], places=2, msg=None, delta=None)

        pass
"""