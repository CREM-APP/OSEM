
from osem.energy_conversion.solar_pv.solar_pv import SolarPV


class TestSolarPV():

    def test_the_estimation_should_be_correct_case1(self):
        # Put some values here
        args = {"Pmax": 0, "GtotalTiltedPlane": 0, "Gstc": 1, "TempCoef": 0, "Ta": 0, "NOCT": 0, "Tstc": 0}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 0
        }

        actual = SolarPV(args).calculate()

        assert expected["ElectricOutputPower"] == actual["ElectricOutputPower"]


    def test_the_estimation_should_be_correct_case2(self):
        # Put some values here
        args = {"Pmax": 0, "GtotalTiltedPlane": 200, "Gstc": 950, "TempCoef": 0.4, "Ta": 12, "NOCT": 40, "Tstc": 21}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 0
        }

        actual = SolarPV(args).calculate()

        assert expected["ElectricOutputPower"] == actual["ElectricOutputPower"]

    def test_the_estimation_should_be_correct_case3(self):
        # Put some values here
        args = {"Pmax": 300, "GtotalTiltedPlane": 0, "Gstc": 950, "TempCoef": 0.4, "Ta": 12, "NOCT": 40, "Tstc": 21}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 0
        }

        actual = SolarPV(args).calculate()

        assert expected["ElectricOutputPower"] == actual["ElectricOutputPower"]

    def test_the_estimation_should_be_correct_case4(self):
        # Put some values here
        args = {"Pmax": 15, "GtotalTiltedPlane": 14, "Gstc": 12, "TempCoef": 100, "Ta": 13, "NOCT": 20, "Tstc": 12}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 0
        }

        actual = SolarPV(args).calculate()

        assert expected["ElectricOutputPower"] == actual["ElectricOutputPower"]

    def test_the_estimation_should_be_correct_case5(self):
        # Put some values here
        args = {"Pmax": 300, "GtotalTiltedPlane": 200, "Gstc": 950, "TempCoef": 0.4, "Ta": 12, "NOCT": 40, "Tstc": 21}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 64.16842105263157
        }

        actual = SolarPV(args).calculate()

        assert expected["ElectricOutputPower"] == actual["ElectricOutputPower"]

    def test_the_estimation_should_be_correct_case6(self):
        # Put some values here
        args = {"Pmax": 300, "GtotalTiltedPlane": 200, "Ta": 12}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 62.025
        }

        actual = SolarPV(args).calculate()

        assert expected["ElectricOutputPower"] == actual["ElectricOutputPower"]

    def test_the_estimation_should_be_correct_case7(self):
        # Put some values here
        args = {"Pmax": 270, "GtotalTiltedPlane": 800, "Ta": 21}

        # Fill this with the expected outcome
        expected = {
            "ElectricOutputPower": 193.32
        }

        actual = SolarPV(args).calculate()

        assert expected["ElectricOutputPower"] == actual["ElectricOutputPower"]