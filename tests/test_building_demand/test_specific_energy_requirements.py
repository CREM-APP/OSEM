"""import unittest

from osem.general.enerapi.base.base import Base
from data.InMemoryFileCache import InMemoryFileCache

from Ener.BuildingDemand.SpecificEnergyRequirements import SpecificEnergyRequirements
from Ener.common import DomainException
from Ener.common import FeatureBroker


class MockCache(InMemoryFileCache):
    def __init__(self):
        super(MockCache, self).__init__()
        self.ReadCount = 0

    # override
    def _load_file_from_disk(self, filename):
        periods = '{"2001-2005": {\
            "GBAUP": 8020,\
            "hS_ratio": 1.587,\
            "em_techno": "RBT",\
            "t_supply": 40,\
            "em_techno_coef": 1.3\
        }}'

        affects = '{"Lgt_Coll.": {\
            "SIA_cat": 1,\
            "hS_ratio": 1,\
            "hW_ratio": 1,\
            "elec_ratio": 1,\
            "h_full_ch": 2300\
        }}'

        ratio_base = '{"std_ratio": {\
                "SIA": 1,\
                "Minergie": 0.9,\
                "MinergieP": 0.6\
        },\
            "base_value": {\
                "hS": 39,\
                "hW": 21,\
                "elec": 28\
            },\
            "refurbished_ratio": 1.25\
        }'

        mock_data = {}

        if filename == "period_RegBL.json":
            mock_data = periods
        if filename == "affect_RegBL.json":
            mock_data = affects
        if filename == "ratio_base.json":
            mock_data = ratio_base
        return mock_data


class TestSpecNeedsHFC(unittest.TestCase):
    @staticmethod
    def setUpClass():
        Base.features = FeatureBroker()
        Base.features.Provide("Cache", MockCache)

    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        args = {"affectation": 1, "period": 8020}
        SpecificEnergyRequirements(args)

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        args = {"affectation": 1}
        with self.assertRaises(DomainException):
            SpecificEnergyRequirements(args)

        args = {"period": 8020}
        with self.assertRaises(DomainException):
            SpecificEnergyRequirements(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):
        args = {"affectation": 0, "period": 8020}
        with self.assertRaises(DomainException):
            SpecificEnergyRequirements(args)

        args = {"affectation": 1, "period": 0}
        with self.assertRaises(DomainException):
            SpecificEnergyRequirements(args)

        args = {"affectation": 1, "period": 8020, "standard": "Test"}
        with self.assertRaises(DomainException):
            SpecificEnergyRequirements(args)

        args = {"affectation": 1, "period": 8020, "refurbished": "Test"}
        with self.assertRaises(DomainException):
            SpecificEnergyRequirements(args)

    def test_the_estimation_should_be_correct_case1(self):
        args = {"affectation": 1, "period": 8020}

        expected = {
            "hS": 61.89,
            "hW": 21,
            "elec": 28,
            "h_full_ch": 2300
        }

        actual = SpecificEnergyRequirements(args).calculate()

        self.assertAlmostEqual(expected["hS"], actual["hS"], places=3, msg=None, delta=None)
        self.assertAlmostEqual(expected["hW"], actual["hW"], places=3, msg=None, delta=None)
        self.assertAlmostEqual(expected["elec"], actual["elec"], places=3, msg=None, delta=None)
        self.assertAlmostEqual(expected["h_full_ch"], actual["h_full_ch"], places=0, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case2(self):
        args = {"affectation": 1, "period": 8020, "standard": "MinergieP"}
        expected = {
            "hS": 37.14,
            "hW": 21,
            "elec": 28,
            "h_full_ch": 2300
        }
        actual = SpecificEnergyRequirements(args).calculate()
        self.assertAlmostEqual(expected["hS"], actual["hS"], places=3, msg=None, delta=None)
        self.assertAlmostEqual(expected["hW"], actual["hW"], places=3, msg=None, delta=None)
        self.assertAlmostEqual(expected["elec"], actual["elec"], places=3, msg=None, delta=None)
        self.assertAlmostEqual(expected["h_full_ch"], actual["h_full_ch"], places=0, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case3(self):
        args = {"affectation": 1, "period": 8020, "standard": "MinergieP", "refurbished": True}
        expected = {
            "hS": 46.420,
            "hW": 21,
            "elec": 28,
            "h_full_ch": 2300
        }
        actual = SpecificEnergyRequirements(args).calculate()
        self.assertAlmostEqual(expected["hS"], actual["hS"], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["hW"], actual["hW"], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["elec"], actual["elec"], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["h_full_ch"], actual["h_full_ch"], places=0, msg=None, delta=None)
"""