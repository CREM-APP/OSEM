import pytest
from osem.general.enerapi.base.base import Base
from osem.building_demand import HeatPowerSupplyTemp




class TestHeatPowerSupplyTemp():




    def test_the_estimation_should_be_correct_case1(self):
        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [15], "ae": 7201}

        expected = {
            "p_heating": [0],
            "t_supply": [0],
            "t_return": [0],
            "p_installed": 2.7
        }

        actual = HeatPowerSupplyTemp(args).calculate()


        assert expected["p_heating"][0] == actual["p_heating"][0]
        assert expected["t_supply"][0] == actual["t_supply"][0]
        assert expected["t_return"][0] == actual["t_return"][0]
        assert expected["p_installed"] == actual["p_installed"]
    def test_the_estimation_should_be_correct_case2(self):
        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [0], "ae": 7201}

        expected = {
            "p_heating": [1.79],
            "t_supply": [29.0],
            "t_return": [23.0],
            "p_installed": 2.7
        }

        actual = HeatPowerSupplyTemp(args).calculate()

        assert expected["p_heating"][0] == actual["p_heating"][0]
        assert expected["t_supply"][0] == actual["t_supply"][0]
        assert expected["t_return"][0] == actual["t_return"][0]
        assert expected["p_installed"] == actual["p_installed"]


    def test_the_estimation_should_be_correct_case3(self):
        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [-10], "ae": 7201}

        expected = {
            "p_heating": [2.69],
            "t_supply": [35.0],
            "t_return": [25.0],
            "p_installed": 2.7
        }

        actual = HeatPowerSupplyTemp(args).calculate()


        assert expected["p_heating"][0] == actual["p_heating"][0]
        assert expected["t_supply"][0] == actual["t_supply"][0]
        assert expected["t_return"][0] == actual["t_return"][0]
        assert expected["p_installed"] == actual["p_installed"]


    def test_the_estimation_should_be_correct_case4(self):
        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [14], "ae": 7201}

        expected = {
            "p_heating": [0.54],
            "t_supply": [20.6],
            "t_return": [20.2],
            "p_installed": 2.7
        }

        actual = HeatPowerSupplyTemp(args).calculate()

        assert expected["p_heating"][0] == actual["p_heating"][0]
        assert expected["t_supply"][0] == actual["t_supply"][0]
        assert expected["t_return"][0] == actual["t_return"][0]
        assert expected["p_installed"] == actual["p_installed"]

    def test_the_estimation_should_be_correct_case5(self):
        args = {"affectation": 1, "period": 8020, "SRE": 100, "t_ext": [12, 14], "ae": 7201}
        expected = {
            "p_heating": [0.72, 0.54],
            "t_supply": [21.8, 20.6],
            "t_return": [20.6, 20.2],
            "p_installed": 2.7
        }

        actual = HeatPowerSupplyTemp(args).calculate()

        assert expected["p_heating"][0] == actual["p_heating"][0]
        assert expected["t_supply"][0] == actual["t_supply"][0]
        assert expected["t_return"][0] == actual["t_return"][0]

        assert expected["p_heating"][1] == actual["p_heating"][1]
        assert expected["t_supply"][1] == actual["t_supply"][1]
        assert expected["t_return"][1] == actual["t_return"][1]

        assert expected["p_installed"] == actual["p_installed"]

