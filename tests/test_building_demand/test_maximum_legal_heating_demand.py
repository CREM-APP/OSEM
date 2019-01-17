
from osem.general.enerapi.base.base import Base


from osem.building_demand.maximum_legal_heating_demand import MaximumLegalHeatingDemand





class TestQhli():




    def test_the_estimation_should_be_correct_case(self):
        args = {"Ath": 450, "Ae": 150, "Affect": 1, "Weather_Station": 5, "project_nature": 4}
        expected = {
            "Qhli": 272.5
        }

        actual = MaximumLegalHeatingDemand(args).calculate()


        assert expected["Qhli"] == actual["Qhli"]


    def test_get_reference(self):
        args = {"Ath": 450, "Ae": 150, "Affect": 1, "Weather_Station": 5, "project_nature": 4}
        actual = MaximumLegalHeatingDemand(args).get_reference()
        assert actual == "SIA 380/1 Norm, heating thermal energy in buildings, edition 2009"

