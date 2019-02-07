

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

    def test_get_reference(self):
        args = {"latitude": 0, "dayOfYear": 1, "solarTime": 0, "slope": 0, "orientation": 0, "GbeamH": 0,
                "GdiffuseH": 0, "surface": 0, "Ta": 0, "Tin": 1, "Tout": 2}

        actual = SolarThermalProductionFromRadiation(args).get_reference()

        assert actual == "Fischer, W. Heidemann, H. Muller-Steinhagen, B. Perers, P. Bergquist, and B. Hellstrom, " \
                       "Collector test method under quasi-dynamic conditions according to the European " \
                       "Standard EN 12975-2 Solar Energy, vol. 76, no. 1-3, pp. 117-123, Jan. 2004 and " \
                       "SPF, Institut Fur SolarTechnik, Collectors, http://www.spf.ch/index.php?id=111&L=6&no_cache=1"
