import unittest


from osem.energy_conversion.boiler.boiler_behaviour import BoilerBehaviour






class TestBoilerBehaviour():

    def test_the_estimation_should_be_correct_case1(self):
        args = {"p_supplied": 100, "techno_id": 7203}

        expected = {
            "p_supplied": 100,
            "p_consumed": 111.11
        }

        actual = BoilerBehaviour(args).calculate()
        assert expected["p_supplied"] == actual["p_supplied"]
        assert expected["p_consumed"] == actual["p_consumed"]


    def test_the_estimation_should_be_correct_case2(self):
        args = {"p_consumed": 100, "techno_id": 7203}

        expected = {
            "p_supplied": 90,
            "p_consumed": 100
        }

        actual = BoilerBehaviour(args).calculate()
        assert expected["p_supplied"] == actual["p_supplied"]
        assert expected["p_consumed"] == actual["p_consumed"]

    def test_get_reference(self):
        args = {"p_consumed": 100, "techno_id": 7203}
        actual = BoilerBehaviour(args).get_reference()
        assert actual == "L.Girardin, A GIS-based Methodology for the Evaluation of Integrated Energy Systems in Urban Area, " \
               "PhD thesis, EPFL, Lausanne, 2012"
