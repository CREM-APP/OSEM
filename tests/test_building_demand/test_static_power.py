



from osem.general.enerapi.base.base import Base
from osem.building_demand.static_heating_cooling_Power import StaticHeatingCoolingPower




class TestICT():



    def test_the_estimation_should_be_correct_case1(self):
        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [23], "irr_south": [700]}

        expected = {
            "Penvelope_heating": [2354.1000000000004],
            "Penvelope_cooling": [-2354.1000000000004],
            "Psol": [25200],
            "Pocc": [233.33333333333334],
            "Ptot_heating": [0],
            "Ptot_cooling": [23079.233333333334]
        }

        actual = StaticHeatingCoolingPower(args).calculate()

        assert expected["Penvelope_heating"] == actual["Penvelope_heating"]
        assert expected["Penvelope_cooling"] == actual["Penvelope_cooling"]
        assert expected["Psol"] == actual["Psol"]
        assert expected["Pocc"] == actual["Pocc"]
        assert expected["Ptot_heating"] == actual["Ptot_heating"]
        assert expected["Ptot_cooling"] == actual["Ptot_cooling"]



    def test_the_estimation_should_be_correct_case2(self):
        args = {"period": 8011, "affectation": 2, "sre": 200, "s_wall": 255, "s_window": 45, "s_roof": 100,
                "s_floor": 100, "esa": 45, "t_ext": [15, 30], "irr_south": [100, 200]}

        expected = {
            "Penvelope_heating": [-3923.5, 7847.0],
            "Penvelope_cooling": [-8631.7, 3138.8],
            "Psol": [3600, 7200.0],
            "Pocc": [233.33333333333334, 233.33333333333334],
            "Ptot_heating": [ 90.16666666666666, 0],
            "Ptot_cooling": [0, 10572.133333333333]
        }

        actual = StaticHeatingCoolingPower(args).calculate()

        assert expected["Penvelope_heating"][0] == actual["Penvelope_heating"][0]
        assert expected["Penvelope_cooling"][0]  == actual["Penvelope_cooling"][0]
        assert expected["Psol"][0]  == actual["Psol"][0]
        assert expected["Pocc"][0]  == actual["Pocc"][0]
        assert expected["Ptot_heating"][0]  == actual["Ptot_heating"][0]
        assert expected["Ptot_cooling"][0]  == actual["Ptot_cooling"][0]

        assert expected["Penvelope_heating"][1] == actual["Penvelope_heating"][1]
        assert expected["Penvelope_cooling"][1]  == actual["Penvelope_cooling"][1]
        assert expected["Psol"][1]  == actual["Psol"][1]
        assert expected["Pocc"][1]  == actual["Pocc"][1]
        assert expected["Ptot_heating"][1]  == actual["Ptot_heating"][1]
        assert expected["Ptot_cooling"][1]  == actual["Ptot_cooling"][1]


