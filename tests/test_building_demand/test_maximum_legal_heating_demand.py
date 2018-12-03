"""import unittest

from osem.general.enerapi.base.base import Base
from data.InMemoryFileCache import InMemoryFileCache

from Ener.BuildingDemand.MaximumLegalHeatingDemand import MaximumLegalHeatingDemand
from Ener.common import DomainException


class MockCache(InMemoryFileCache):
    def __init__(self):
        super(MockCache, self).__init__()
        self.ReadCount = 0

    # override
    def _load_file_from_disk(self, filename):
        data_qhli = '{"data": {\
		    "lgt_Coll.": {\
			    "SIA_cat": 1,\
			    "Qhli0": 55,\
			    "DQhli": 65\
        }}}'

        meteo = '{"data": {\
		    "Sion": {\
			    "Weather_Station_ref": 5,\
			    "Text_Min": -12.1,\
			    "Text_Moy": 10.1\
        }}}'

        project_nature = '{"data": {\
		    "Refurbishment": {\
			    "project_nature": 4,\
			    "Coef_nature": 1.25\
        }}}'

        mock_data = {}

        if filename == "Meteo2028.json":
            mock_data = meteo
        if filename == "Data_Qhli.json":
            mock_data = data_qhli
        if filename == "Data_Project_Nature.json":
            mock_data = project_nature
        return mock_data


class TestQhli(unittest.TestCase):
    @staticmethod
    def setUpClass():
        Base.features = FeatureBroker()
        Base.features.Provide("Cache", MockCache)

    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        args = {"Ath": 450, "Ae": 150, "Affect": 1, "Weather_Station": 5, "project_nature": 4}
        MaximumLegalHeatingDemand(args)

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        args = {"Ae": 150, "Affect": 1, "Weather_Station": 5, "project_nature": 4}
        with self.assertRaises(DomainException):
            MaximumLegalHeatingDemand(args)

        args = {"Ath": 450, "Affect": 1, "Weather_Station": 5, "project_nature": 4}
        with self.assertRaises(DomainException):
            MaximumLegalHeatingDemand(args)

        args = {"Ath": 450, "Ae": 150, "Weather_Station": 5, "project_nature": 4}
        with self.assertRaises(DomainException):
            MaximumLegalHeatingDemand(args)

        args = {"Ath": 450, "Ae": 150, "Affect": 1, "project_nature": 4}
        with self.assertRaises(DomainException):
            MaximumLegalHeatingDemand(args)

        args = {"Ath": 450, "Ae": 150, "Affect": 1, "Weather_Station": 5}
        with self.assertRaises(DomainException):
            MaximumLegalHeatingDemand(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):
        args = {"Ath": -450, "Ae": 150, "Affect": 1, "Weather_Station": 5, "project_nature": 4}
        with self.assertRaises(DomainException):
            MaximumLegalHeatingDemand(args)

        args = {"Ath": 450, "Ae": -150, "Affect": 1, "Weather_Station": 5, "project_nature": 4}
        with self.assertRaises(DomainException):
            MaximumLegalHeatingDemand(args)

        args = {"Ath": 450, "Ae": 150, "Affect": -1, "Weather_Station": 5, "project_nature": 4}
        with self.assertRaises(DomainException):
            MaximumLegalHeatingDemand(args)

        args = {"Ath": 450, "Ae": 150, "Affect": 1, "Weather_Station": -5, "project_nature": 4}
        with self.assertRaises(DomainException):
            MaximumLegalHeatingDemand(args)

        args = {"Ath": 450, "Ae": 150, "Affect": 1, "Weather_Station": 5, "project_nature": -4}
        with self.assertRaises(DomainException):
            MaximumLegalHeatingDemand(args)

    def test_the_estimation_should_be_correct_case(self):
        args = {"Ath": 450, "Ae": 150, "Affect": 1, "Weather_Station": 5, "project_nature": 4}
        expected = {
            "Qhli": 272.5
        }

        actual = MaximumLegalHeatingDemand(args).calculate()

        self.assertAlmostEqual(expected["Qhli"], actual["Qhli"], places=2, msg=None, delta=None)

"""