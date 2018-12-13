

from osem.energy_conversion.solar_thermal.solar_thermal_production_from_radiation import \
    SolarThermalProductionFromRadiation


class TestSolarThermal():

    # integration test
    def test_the_estimation_should_be_correct_case(self):
        # Put some values here
        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "surface": 0, "Ta": 0, "Tin": 1, "Tout": 2}

        # Fill this with the expected outcome
        expected = {
            "usefulOutputPower": 0,
            "IAMbeam": 0,
            "IAMdiffuse": 0.8548
        }

        actual = SolarThermalProductionFromRadiation(args).calculate()
        assert expected["usefulOutputPower"] == actual["usefulOutputPower"]
        assert expected["IAMbeam"] == actual["IAMbeam"]
        assert expected["IAMdiffuse"] == actual["IAMdiffuse"]