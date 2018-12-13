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
