

from osem.general.enerapi.base.base import Base

from osem.building_demand.specific_energy_requirements import SpecificEnergyRequirements






class TestSpecNeedsHFC():




    def test_the_estimation_should_be_correct_case1(self):
        args = {"affectation": 1, "period": 8020}

        expected = {
            "hS": 61.89,
            "hW": 21,
            "elec": 28,
            "h_full_ch": 2300
        }

        actual = SpecificEnergyRequirements(args).calculate()



        assert expected["hS"] == actual["hS"]
        assert expected["hW"] == actual["hW"]
        assert expected["elec"] == actual["elec"]
        assert expected["h_full_ch"] == actual["h_full_ch"]

    def test_the_estimation_should_be_correct_case2(self):
        args = {"affectation": 1, "period": 8020, "standard": "MinergieP"}
        expected = {
            "hS": 37.14,
            "hW": 21,
            "elec": 28,
            "h_full_ch": 2300
        }
        actual = SpecificEnergyRequirements(args).calculate()
        assert expected["hS"] == actual["hS"]
        assert expected["hW"] == actual["hW"]
        assert expected["elec"] == actual["elec"]
        assert expected["h_full_ch"] == actual["h_full_ch"]


    def test_the_estimation_should_be_correct_case3(self):
            args = {"affectation": 1, "period": 8020, "standard": "MinergieP", "refurbished": True}
            expected = {
                "hS": 46.420,
                "hW": 21,
                "elec": 28,
                "h_full_ch": 2300
            }
            actual = SpecificEnergyRequirements(args).calculate()
            assert expected["hS"] == actual["hS"]
            assert expected["hW"] == actual["hW"]
            assert expected["elec"] == actual["elec"]
            assert expected["h_full_ch"] == actual["h_full_ch"]
            
    def test_get_reference(self):
        args = {"affectation": 1, "period": 8020, "standard": "MinergieP", "refurbished": True}
        actual = SpecificEnergyRequirements(args).get_reference()
        assert actual == "Novatlantis, Steps towards a sustainable development, a White Book for R&D of energy-efficient " \
                         "technologies, February 2004 and L.Girardin, A GIS-based Methodology for the Evaluation of " \
                         "Integrated Energy Systems in Urban Area, PhD thesis, EPFL, Lausanne, 2012"