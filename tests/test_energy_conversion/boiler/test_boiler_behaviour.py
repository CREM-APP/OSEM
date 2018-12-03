"""import unittest

from osem.general.enerapi.base.base import Base
from osem.energy_conversion.boiler.boiler_behaviour import BoilerBehaviour
from data.InMemoryFileCache import InMemoryFileCache

from osem.general.enerapi.common import DomainException
from osem.general.enerapi.common import FeatureBroker


class MockCache(InMemoryFileCache):
    def __init__(self):
        super(MockCache, self).__init__()
        self.ReadCount = 0

    # override
    def _load_file_from_disk(self, filename):
        techno = '{"data": {\
            "Gaz": {\
                "GENHZ-WW": 7203,\
                "efficiency": 0.9\
        }}}'

        mock_data = {}

        if filename == "boiler_techno.json":
            mock_data = techno
        return mock_data


class TestBoilerBehaviour(unittest.TestCase):
    @staticmethod
    def setUpClass():
        Base.features = FeatureBroker()
        Base.features.Provide("Cache", MockCache)

    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        args = {"p_consumed": 100, "techno_id": 7203}
        BoilerBehaviour(args)

        args = {"p_supplied": 100, "techno_id": 7203}
        BoilerBehaviour(args)

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        args = {"techno_id": 7203}
        with self.assertRaises(DomainException):
            BoilerBehaviour(args)

        args = {"p_consumed": 100}
        with self.assertRaises(DomainException):
            BoilerBehaviour(args)

        args = {"p_supplied": 100, "p_consumed": 100, "techno_id": 7203}
        with self.assertRaises(DomainException):
            BoilerBehaviour(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):
        args = {"p_supplied": -10, "techno_id": 7203}
        with self.assertRaises(DomainException):
            BoilerBehaviour(args)

        args = {"p_consumed": -10, "techno_id": 7203}
        with self.assertRaises(DomainException):
            BoilerBehaviour(args)

        args = {"p_consumed": 100, "techno_id": "test"}
        with self.assertRaises(DomainException):
            BoilerBehaviour(args)

    def test_the_estimation_should_be_correct_case1(self):
        args = {"p_supplied": 100, "techno_id": 7203}

        expected = {
            "p_supplied": 100,
            "p_consumed": 111.11
        }

        actual = BoilerBehaviour(args).calculate()

        self.assertAlmostEqual(expected["p_supplied"], actual["p_supplied"], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_consumed"], actual["p_consumed"], places=2, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case2(self):
        args = {"p_consumed": 100, "techno_id": 7203}

        expected = {
            "p_supplied": 90,
            "p_consumed": 100
        }

        actual = BoilerBehaviour(args).calculate()

        self.assertAlmostEqual(expected["p_supplied"], actual["p_supplied"], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_consumed"], actual["p_consumed"], places=2, msg=None, delta=None)
"""