
"""import unittest

from osem.general.enerapi.base.base import Base


from Ener.BuildingDemand.HeatPowerSupplyTemp import HeatPowerSupplyTemp
from Ener.common import DomainException
from Ener.common import FeatureBroker


class MockCache(InMemoryFileCache):
    def __init__(self):
        super(MockCache, self).__init__()
        self.ReadCount = 0

    # override
    def _load_file_from_disk(self, filename):
        data_sia = '{"data": {\
            "Lgt_Coll.": {\
                "SIA_cat": 1,\
                "t_heat_set_point": 20,\
                "surf_pers": 40,\
                "heat_pers": 70,\
                "pres_pers": 12,\
                "elec_cons": 28,\
                "elec_heat_fac": 0.7,\
                "air_flow": 0.7,\
                "hw_needs": 21\
        }}}'

        data_em_sys = '{"data": {\
            "2001-2005": {\
                "GBAUP": 8020,\
                "Mazout": {\
                    "GENHZ-WW": 7201,\
                    "niv_t": 40,\
                    "n": 0.7,\
                    "em_techno": "Chauff_sol"\
        }}}}'

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
        if filename == "affect_RegBL.json":
            mock_data = affects
        if filename == "ratio_base.json":
            mock_data = ratio_base
        if filename == "period_RegBL.json":
            mock_data = periods
        if filename == 'data_SIA_380-1.json':
            mock_data = data_sia
        if filename == 'em_system.json':
            mock_data = data_em_sys
        return mock_data


class TestHeatPowerSupplyTemp(unittest.TestCase):
    @staticmethod
    def setUpClass():
        Base.features = FeatureBroker()
        Base.features.Provide("Cache", MockCache)

    def test_if_all_arguments_are_here_no_exception_should_be_raised(self):
        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [0], "ae": 7201}
        HeatPowerSupplyTemp(args)

    def test_if_any_required_argument_is_missing_an_exception_should_be_raised(self):
        args = {"affectation": 1, "SRE": 100, "t_ext": [0], "ae": 7201}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"period": 8020, "SRE": 100, "t_ext": [0], "ae": 7201}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"affectation": 1, "period": 8020, "t_ext": [0], "ae": 7201}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"affectation": 1, "period": 8020, "SRE": 100, "ae": 7201}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [0]}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

    def test_if_an_argument_has_an_incorrect_value_an_exception_should_be_raised(self):
        args = {"affectation": 0, "period": 8020, "SRE": 100, "t_ext": [0], "ae": 7201}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"affectation": 1, "period": 10000, "SRE": 100, "t_ext": [0], "ae": 7201}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"affectation": 1, "period": 8020, "SRE": -1, "t_ext": [0], "ae": 7201}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [100], "ae": 7201}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [0], "ae": 10000}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [0], "ae": 7201, "standard": "Test"}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [0], "ae": 7201, "refurbished": "Test"}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [0], "ae": 7201, "dh_max": -1}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [0], "ae": 7201, "t_max_heat": -1, "t_dim": 0}
        with self.assertRaises(DomainException):
            HeatPowerSupplyTemp(args)

    def test_the_estimation_should_be_correct_case1(self):
        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [15], "ae": 7201}

        expected = {
            "p_heating": [0],
            "t_supply": [0],
            "t_return": [0],
            "p_installed": 2.7
        }

        actual = HeatPowerSupplyTemp(args).calculate()

        self.assertAlmostEqual(expected["p_heating"][0], actual["p_heating"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_supply"][0], actual["t_supply"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_return"][0], actual["t_return"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_installed"], actual["p_installed"], places=1, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case2(self):
        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [0], "ae": 7201}

        expected = {
            "p_heating": [1.79],
            "t_supply": [32.0],
            "t_return": [26.0],
            "p_installed": 2.7
        }

        actual = HeatPowerSupplyTemp(args).calculate()

        self.assertAlmostEqual(expected["p_heating"][0], actual["p_heating"][0], places=2, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_supply"][0], actual["t_supply"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_return"][0], actual["t_return"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_installed"], actual["p_installed"], places=1, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case3(self):
        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [-10], "ae": 7201}

        expected = {
            "p_heating": [2.7],
            "t_supply": [40],
            "t_return": [30],
            "p_installed": 2.7
        }

        actual = HeatPowerSupplyTemp(args).calculate()

        self.assertAlmostEqual(expected["p_heating"][0], actual["p_heating"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_supply"][0], actual["t_supply"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_return"][0], actual["t_return"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_installed"], actual["p_installed"], places=1, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case4(self):
        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [14], "ae": 7201}

        expected = {
            "p_heating": [0.52],
            "t_supply": [20.8],
            "t_return": [20.4],
            "p_installed": 2.7
        }

        actual = HeatPowerSupplyTemp(args).calculate()

        self.assertAlmostEqual(expected["p_heating"][0], actual["p_heating"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_supply"][0], actual["t_supply"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_return"][0], actual["t_return"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["p_installed"], actual["p_installed"], places=1, msg=None, delta=None)

    def test_the_estimation_should_be_correct_case5(self):
        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [12, 14], "ae": 7201}

        expected = {
            "p_heating": [0.72, 0.52],
            "t_supply": [22.4, 20.8],
            "t_return": [21.2, 20.4],
            "p_installed": 2.7
        }

        actual = HeatPowerSupplyTemp(args).calculate()

        self.assertAlmostEqual(expected["p_heating"][0], actual["p_heating"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_supply"][0], actual["t_supply"][0], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_return"][0], actual["t_return"][0], places=1, msg=None, delta=None)

        self.assertAlmostEqual(expected["p_heating"][1], actual["p_heating"][1], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_supply"][1], actual["t_supply"][1], places=1, msg=None, delta=None)
        self.assertAlmostEqual(expected["t_return"][1], actual["t_return"][1], places=1, msg=None, delta=None)

        self.assertAlmostEqual(expected["p_installed"], actual["p_installed"], places=1, msg=None, delta=None)
"""